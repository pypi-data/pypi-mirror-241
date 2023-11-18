import multiprocessing
import os
import sys
import textwrap
import threading
import time
import enum
import inspect
import asyncio
import warnings

import psutil

import numpy as np

try:
    import numpy.typing as npt
except ImportError:
    npt = None

import pytest

from collections.abc import Callable

import tango.asyncio
import tango.constants
from tango import (
    AttrData,
    Attr,
    AttrDataFormat,
    AttrQuality,
    AttReqType,
    AttrWriteType,
    CmdArgType,
    DevBoolean,
    DevLong,
    DevDouble,
    DevFailed,
    DevEncoded,
    DevEnum,
    DevState,
    DevVoid,
    Device_4Impl,
    Device_5Impl,
    DeviceClass,
    DeviceProxy,
    EventType,
    ExtractAs,
    GreenMode,
    InfoIt,
    LatestDeviceImpl,
    PyTangoUserWarning,
    READ_WRITE,
    SCALAR,
    SPECTRUM,
    EncodedAttribute,
)
from tango.green import get_executor
from tango.server import BaseDevice, Device
from tango.pyutil import parse_args
from tango.server import command, attribute, device_property
from tango.test_utils import DeviceTestContext, MultiDeviceTestContext
from tango.test_utils import (
    GoodEnum,
    BadEnumNonZero,
    BadEnumSkipValues,
    BadEnumDuplicates,
)
from tango.test_utils import (
    assert_close,
    general_decorator,
    check_attr_type,
    check_read_attr,
    make_nd_value,
    DEVICE_SERVER_ARGUMENTS,
    convert_dtype_to_typing_hint,
    UTF8_STRING,
)
from tango.utils import (
    EnumTypeError,
    FROM_TANGO_TO_NUMPY_TYPE,
    TO_TANGO_TYPE,
    get_enum_labels,
    get_latest_device_class,
    is_pure_str,
    get_tango_type_format,
    parse_type_hint,
)

# Constants
WINDOWS = "nt" in os.name
TIMEOUT = 10.0

# Test implementation classes

WRONG_HINTS = (  # hint_caller, type_hint, error_reason
    ("property", tuple[tuple[int]], "Property does not support IMAGE type"),
    (
        "property",
        tuple[tuple[int, float], float],
        "Property does not support IMAGE type",
    ),
    ("property", tuple[int, float], "PyTango does not support mixed types"),
    ("attribute", tuple[int, float], "PyTango does not support mixed types"),
    (
        "attribute",
        tuple[tuple[int, float], float],
        "PyTango does not support mixed types",
    ),
    (
        "attribute",
        tuple[tuple[int, int], list[int, int]],
        "PyTango does not support mixed types",
    ),
    ("attribute", Callable[[int], None], "Cannot translate"),
)


@pytest.mark.parametrize("hint_caller, type_hint, error_reason", WRONG_HINTS)
def test_uncorrect_typing_hints(hint_caller, type_hint, error_reason):
    with pytest.raises(RuntimeError, match=error_reason):
        dtype, dformat, max_x, max_y = parse_type_hint(type_hint, caller=hint_caller)
        get_tango_type_format(dtype, dformat, hint_caller)


def test_device_classes_use_latest_implementation():
    assert issubclass(LatestDeviceImpl, get_latest_device_class())
    assert issubclass(BaseDevice, LatestDeviceImpl)
    assert issubclass(Device, BaseDevice)


# Test state/status


def test_empty_device(server_green_mode):
    class TestDevice(Device):
        green_mode = server_green_mode

    with DeviceTestContext(TestDevice) as proxy:
        assert proxy.state() == DevState.UNKNOWN
        assert proxy.status() == "The device is in UNKNOWN state."


def test_set_state(state, server_green_mode):
    status = f"The device is in {state!s} state."

    class TestDevice(Device):
        green_mode = server_green_mode

        def init_device(self):
            self.set_state(state)

    with DeviceTestContext(TestDevice) as proxy:
        assert proxy.state() == state
        assert proxy.status() == status


def test_user_dev_state_status(server_green_mode):
    state = DevState.MOVING
    status = "Device is MOVING"

    if server_green_mode == GreenMode.Asyncio:

        class TestDevice(Device):
            green_mode = server_green_mode

            async def dev_state(self):
                return state

            async def dev_status(self):
                return status

    else:

        class TestDevice(Device):
            green_mode = server_green_mode

            def dev_state(self):
                return state

            def dev_status(self):
                return status

    with DeviceTestContext(TestDevice) as proxy:
        assert proxy.state() == state
        assert proxy.status() == status


def test_set_status(server_green_mode):
    status = "\n".join(
        (
            "This is a multiline status",
            "with special characters such as",
            "Café à la crème",
        )
    )

    class TestDevice(Device):
        green_mode = server_green_mode

        def init_device(self):
            self.set_state(DevState.ON)
            self.set_status(status)

    with DeviceTestContext(TestDevice) as proxy:
        assert proxy.state() == DevState.ON
        assert proxy.status() == status


def test_attr_quality_checked_with_state(server_green_mode):
    class TestDevice(Device):
        green_mode = server_green_mode

        read_attr_hardware_was_called = False
        always_executed_hook_was_called = False

        @command(dtype_out=bool)
        def check_sub_function_was_called(self):
            return (
                self.read_attr_hardware_was_called
                and self.always_executed_hook_was_called
            )

        sync_code = textwrap.dedent(
            """
            def init_device(self):
                Device.init_device(self)
                self.set_state(DevState.ON)
            
            def read_attr_hardware(self, attr_list):
                self.read_attr_hardware_was_called = True
                return Device.read_attr_hardware(self, attr_list)

            def always_executed_hook(self):
                self.always_executed_hook_was_called = True
            
            @attribute(max_alarm=0)
            def test_attribute(self):
                return 42
                """
        )

        if server_green_mode == GreenMode.Asyncio:
            exec(
                sync_code.replace("def", "async def").replace("Device", "await Device")
            )
        else:
            exec(sync_code)

    with DeviceTestContext(TestDevice) as proxy:
        assert proxy.state() == DevState.ALARM
        assert proxy.check_sub_function_was_called()


# Test commands


def test_identity_command(command_typed_values, server_green_mode):
    dtype, values, expected = command_typed_values

    if dtype == (bool,):
        pytest.xfail("Not supported for some reasons")

    class TestDevice(Device):
        green_mode = server_green_mode

        @command(dtype_in=dtype, dtype_out=dtype)
        def identity(self, arg):
            return arg

    with DeviceTestContext(TestDevice) as proxy:
        for value in values:
            assert_close(proxy.identity(value), expected(value))


def test_identity_command_with_typing(command_typed_values):
    dtype, values, expected = command_typed_values
    tuple_hint, list_hint, _, _ = convert_dtype_to_typing_hint(dtype)

    if dtype == (bool,):
        pytest.xfail("Not supported for some reasons")

    class TestDevice(Device):
        @command()
        def command_tuple_hint(self, arg: tuple_hint) -> tuple_hint:
            return arg

        @command()
        def command_list_hint(self, arg: list_hint) -> list_hint:
            return arg

        @command(dtype_in=dtype, dtype_out=dtype)
        def command_user_type_has_priority(self, arg: dict) -> dict:
            return arg

    with DeviceTestContext(TestDevice) as proxy:
        for value in values:
            assert_close(proxy.command_tuple_hint(value), expected(value))
            assert_close(proxy.command_list_hint(value), expected(value))
            assert_close(proxy.command_user_type_has_priority(value), expected(value))


def test_devstate_command_with_typing():
    class TestDevice(Device):
        @command
        def arbitrary_devstate_command(self, arg_in: DevState) -> DevState:
            return arg_in

    with DeviceTestContext(TestDevice) as proxy:
        assert proxy.arbitrary_devstate_command(DevState.MOVING) == DevState.MOVING


def test_command_self_typed_with_not_defined_name():
    class TestDevice(Device):
        @command
        def identity(self: "TestDevice", arg_in: int) -> int:
            return arg_in

        def dynamic_identity(self: "TestDevice", arg_in: int) -> int:
            return arg_in

        @command()
        def add_dyn_cmd(self: "TestDevice"):
            cmd = command(f=self.dynamic_identity)
            self.add_command(cmd)

    with DeviceTestContext(TestDevice) as proxy:
        proxy.add_dyn_cmd()
        assert 1 == proxy.identity(1)
        assert 1 == proxy.dynamic_identity(1)


def test_decorated_command(server_green_mode):
    class TestDevice(Device):
        green_mode = server_green_mode
        is_allowed = None

        @general_decorator()
        @command(dtype_in=int, dtype_out=int)
        def identity(self, arg):
            return arg

        @general_decorator
        def is_identity_allowed(self):
            return self.is_allowed

        @command(dtype_in=bool)
        def make_allowed(self, yesno):
            self.is_allowed = yesno

    with DeviceTestContext(TestDevice) as proxy:
        proxy.make_allowed(True)
        assert_close(proxy.identity(123), 123)

        proxy.make_allowed(False)
        with pytest.raises(DevFailed):
            proxy.identity(1)


def test_command_isallowed(server_green_mode):
    is_allowed = None

    def sync_allowed(device):
        assert isinstance(device, TestDevice)
        return is_allowed

    async def async_allowed(device):
        assert isinstance(device, TestDevice)
        return is_allowed

    class IsAllowedCallableClass:
        def __init__(self):
            self._is_allowed = None

        def __call__(self, device):
            assert isinstance(device, TestDevice)
            return self._is_allowed

        def make_allowed(self, yesno):
            self._is_allowed = yesno

    is_allowed_callable_class = IsAllowedCallableClass()

    class TestDevice(Device):
        green_mode = server_green_mode

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._is_allowed = True

        @command(dtype_in=int, dtype_out=int)
        def identity(self, arg):
            return arg

        @command(dtype_in=int, dtype_out=int, fisallowed="is_identity_allowed")
        def identity_kwarg_string(self, arg):
            return arg

        @command(
            dtype_in=int,
            dtype_out=int,
            fisallowed=sync_allowed
            if server_green_mode != GreenMode.Asyncio
            else async_allowed,
        )
        def identity_kwarg_callable(self, arg):
            return arg

        @command(dtype_in=int, dtype_out=int, fisallowed=is_allowed_callable_class)
        def identity_kwarg_callable_class(self, arg):
            return arg

        @command(dtype_in=int, dtype_out=int)
        def identity_always_allowed(self, arg):
            return arg

        @command(dtype_in=bool)
        def make_allowed(self, yesno):
            self._is_allowed = yesno

        synchronous_code = textwrap.dedent(
            """\
            def is_identity_allowed(self):
                return self._is_allowed
            """
        )

        asynchronous_code = synchronous_code.replace("def ", "async def ")

        if server_green_mode != GreenMode.Asyncio:
            exec(synchronous_code)
        else:
            exec(asynchronous_code)

    with DeviceTestContext(TestDevice) as proxy:
        proxy.make_allowed(True)
        is_allowed_callable_class.make_allowed(True)
        is_allowed = True

        assert_close(proxy.identity(1), 1)
        assert_close(proxy.identity_kwarg_string(1), 1)
        assert_close(proxy.identity_kwarg_callable(1), 1)
        assert_close(proxy.identity_kwarg_callable_class(1), 1)
        assert_close(proxy.identity_always_allowed(1), 1)

        proxy.make_allowed(False)
        is_allowed_callable_class.make_allowed(False)
        is_allowed = False

        with pytest.raises(DevFailed):
            proxy.identity(1)

        with pytest.raises(DevFailed):
            proxy.identity_kwarg_string(1)

        with pytest.raises(DevFailed):
            proxy.identity_kwarg_callable(1)

        with pytest.raises(DevFailed):
            proxy.identity_kwarg_callable_class(1)

        assert_close(proxy.identity_always_allowed(1), 1)


@pytest.mark.parametrize("device_command_level", [True, False])
def test_dynamic_command(server_green_mode, device_command_level):
    is_allowed = None

    def sync_allowed(device):
        assert isinstance(device, TestDevice)
        return is_allowed

    async def async_allowed(device):
        assert isinstance(device, TestDevice)
        return is_allowed

    class IsAllowedCallable:
        def __init__(self):
            self._is_allowed = None

        def __call__(self, device):
            assert isinstance(device, TestDevice)
            return self._is_allowed

        def make_allowed(self, yesno):
            self._is_allowed = yesno

    is_allowed_callable_class = IsAllowedCallable()

    class TestDevice(Device):
        green_mode = server_green_mode

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self._is_allowed = True

        def identity(self, arg):
            return arg

        def identity_kwarg_string(self, arg):
            return arg

        def identity_kwarg_callable(self, arg):
            return arg

        def identity_kwarg_callable_outside_class(self, arg):
            return arg

        def identity_kwarg_callable_class(self, arg):
            return arg

        def identity_always_allowed(self, arg):
            return arg

        @command()
        def add_dyn_cmd(self):
            cmd = command(f=self.identity, dtype_in=int, dtype_out=int)
            self.add_command(cmd, device_command_level)

            cmd = command(
                f=self.identity_kwarg_string,
                dtype_in=int,
                dtype_out=int,
                fisallowed="is_identity_allowed",
            )
            self.add_command(cmd, device_command_level)

            cmd = command(
                f=self.identity_kwarg_callable,
                dtype_in=int,
                dtype_out=int,
                fisallowed=self.is_identity_allowed,
            )
            self.add_command(cmd, device_command_level)

            cmd = command(
                f=self.identity_kwarg_callable_outside_class,
                dtype_in=int,
                dtype_out=int,
                fisallowed=sync_allowed
                if server_green_mode != GreenMode.Asyncio
                else async_allowed,
            )
            self.add_command(cmd, device_command_level)

            cmd = command(
                f=self.identity_kwarg_callable_class,
                dtype_in=int,
                dtype_out=int,
                fisallowed=is_allowed_callable_class,
            )
            self.add_command(cmd, device_command_level)

            cmd = command(f=self.identity_always_allowed, dtype_in=int, dtype_out=int)
            self.add_command(cmd, device_command_level)

        @command(dtype_in=bool)
        def make_allowed(self, yesno):
            self._is_allowed = yesno

        synchronous_code = textwrap.dedent(
            """\
                def is_identity_allowed(self):
                    return self._is_allowed
                """
        )

        asynchronous_code = synchronous_code.replace("def ", "async def ")

        if server_green_mode != GreenMode.Asyncio:
            exec(synchronous_code)
        else:
            exec(asynchronous_code)

    with DeviceTestContext(TestDevice) as proxy:
        proxy.add_dyn_cmd()

        proxy.make_allowed(True)
        is_allowed_callable_class.make_allowed(True)
        is_allowed = True

        assert_close(proxy.identity(1), 1)
        assert_close(proxy.identity_kwarg_string(1), 1)
        assert_close(proxy.identity_kwarg_callable(1), 1)
        assert_close(proxy.identity_kwarg_callable_outside_class(1), 1)
        assert_close(proxy.identity_kwarg_callable_class(1), 1)
        assert_close(proxy.identity_always_allowed(1), 1)

        proxy.make_allowed(False)
        is_allowed_callable_class.make_allowed(False)
        is_allowed = False

        with pytest.raises(DevFailed):
            proxy.identity(1)

        with pytest.raises(DevFailed):
            proxy.identity_kwarg_string(1)

        with pytest.raises(DevFailed):
            proxy.identity_kwarg_callable(1)

        with pytest.raises(DevFailed):
            proxy.identity_kwarg_callable_outside_class(1)

        with pytest.raises(DevFailed):
            proxy.identity_kwarg_callable_class(1)

        assert_close(proxy.identity_always_allowed(1), 1)


def test_identity_dynamic_command_with_typing(command_typed_values):
    dtype, values, expected = command_typed_values
    tuple_hint, list_hint, _, _ = convert_dtype_to_typing_hint(dtype)

    if dtype == (bool,):
        pytest.xfail("Not supported for some reasons")

    class TestDevice(Device):
        def command_tuple_hint(self, arg: tuple_hint) -> tuple_hint:
            return arg

        def command_list_hint(self, arg: list_hint) -> list_hint:
            return arg

        def command_user_type_has_priority(self, arg: dict) -> dict:
            return arg

        @command()
        def add_dyn_cmd(self):
            cmd = command(f=self.command_tuple_hint)
            self.add_command(cmd)

            cmd = command(f=self.command_list_hint)
            self.add_command(cmd)

            cmd = command(
                f=self.command_user_type_has_priority, dtype_in=dtype, dtype_out=dtype
            )
            self.add_command(cmd)

    with DeviceTestContext(TestDevice) as proxy:
        proxy.add_dyn_cmd()
        for value in values:
            assert_close(proxy.command_tuple_hint(value), expected(value))
            assert_close(proxy.command_list_hint(value), expected(value))
            assert_close(proxy.command_user_type_has_priority(value), expected(value))


if npt:

    def test_identity_commands_with_numpy_typing(command_numpy_typed_values):
        type_hint, dformat, value, expected = command_numpy_typed_values
        if type_hint == np.uint8:
            pytest.xfail("Does not work for some reason")

        class TestDevice(Device):
            def identity_dynamic_command(self, arg: type_hint) -> type_hint:
                return arg

            @command
            def identity_static_command(self, arg: type_hint) -> type_hint:
                return arg

            @command()
            def add_dyn_cmd(self):
                cmd = command(f=self.identity_dynamic_command)
                self.add_command(cmd)

        with DeviceTestContext(TestDevice) as proxy:
            proxy.add_dyn_cmd()
            assert_close(proxy.identity_static_command(value), expected(value))
            assert_close(proxy.identity_dynamic_command(value), expected(value))


def test_polled_command(server_green_mode):
    dct = {"Polling1": 100, "Polling2": 100000, "Polling3": 500}

    class TestDevice(Device):
        green_mode = server_green_mode

        @command(polling_period=dct["Polling1"])
        def Polling1(self):
            pass

        @command(polling_period=dct["Polling2"])
        def Polling2(self):
            pass

        @command(polling_period=dct["Polling3"])
        def Polling3(self):
            pass

    with DeviceTestContext(TestDevice) as proxy:
        ans = proxy.polling_status()

    for info in ans:
        lines = info.split("\n")
        comm = lines[0].split("= ")[1]
        period = int(lines[1].split("= ")[1])
        assert dct[comm] == period


def test_wrong_command_result(server_green_mode):
    class TestDevice(Device):
        green_mode = server_green_mode

        @command(dtype_out=str)
        def cmd_str_err(self):
            return 1.2345

        @command(dtype_out=int)
        def cmd_int_err(self):
            return "bla"

        @command(dtype_out=[str])
        def cmd_str_list_err(self):
            return ["hello", 55]

    with DeviceTestContext(TestDevice) as proxy:
        with pytest.raises(DevFailed):
            proxy.cmd_str_err()
        with pytest.raises(DevFailed):
            proxy.cmd_int_err()
        with pytest.raises(DevFailed):
            proxy.cmd_str_list_err()


# Test attributes
def test_read_write_attribute(attribute_typed_values, server_green_mode):
    dtype, values, expected = attribute_typed_values

    class TestDevice(Device):
        green_mode = server_green_mode
        _is_allowed = None

        @attribute(
            dtype=dtype, max_dim_x=3, max_dim_y=3, access=AttrWriteType.READ_WRITE
        )
        def attr(self):
            return self.attr_value

        @attr.write
        def attr(self, value):
            self.attr_value = value

        def is_attr_allowed(self, req_type):
            assert req_type in (AttReqType.READ_REQ, AttReqType.WRITE_REQ)
            return self._is_allowed

        @command(dtype_in=bool)
        def make_allowed(self, yesno):
            self._is_allowed = yesno

    with DeviceTestContext(TestDevice) as proxy:
        proxy.make_allowed(True)
        for value in values:
            proxy.attr = value
            assert_close(proxy.attr, expected(value))

        proxy.make_allowed(False)
        with pytest.raises(DevFailed):
            proxy.attr = value
        with pytest.raises(DevFailed):
            _ = proxy.attr


def test_wrong_encoding_string():
    class TestDevice(Device):
        @attribute(dtype=str)
        def wrong_string(self):
            return "�"

    with DeviceTestContext(TestDevice) as proxy:
        with pytest.raises(DevFailed, match="UnicodeError"):
            _ = proxy.wrong_string


@pytest.mark.parametrize("return_time_quality", [True, False])
def test_attribute_declared_with_typing(attribute_typed_values, return_time_quality):
    dtype, values, expected = attribute_typed_values
    tuple_hint, list_hint, check_x_dim, check_y_dim = convert_dtype_to_typing_hint(
        dtype
    )

    if return_time_quality:
        tuple_hint = tuple[tuple_hint, float, AttrQuality]
        list_hint = list[list_hint, float, AttrQuality]

    class TestDevice(Device):
        attr_value = None

        hint_with_tuple: tuple_hint = attribute(
            access=AttrWriteType.READ_WRITE, fget="read_attr", fset="write_attr"
        )

        user_size_priority_over_hint: tuple_hint = attribute(
            max_dim_x=5,
            max_dim_y=5,
            access=AttrWriteType.READ_WRITE,
            fget="read_attr",
            fset="write_attr",
        )

        hint_with_list: list_hint = attribute(
            max_dim_x=5,
            max_dim_y=5,
            access=AttrWriteType.READ_WRITE,
            fget="read_attr",
            fset="write_attr",
        )

        def read_attr(self):
            if return_time_quality:
                return self.attr_value, time.time(), AttrQuality.ATTR_VALID
            return self.attr_value

        def write_attr(self, value):
            self.attr_value = value

        @attribute(access=AttrWriteType.READ_WRITE)
        def decorator_tuple_hint(self) -> tuple_hint:
            if return_time_quality:
                return self.attr_value, time.time(), AttrQuality.ATTR_VALID
            return self.attr_value

        @decorator_tuple_hint.write
        def decorator_tuple_hint(self, value):
            self.attr_value = value

        @attribute(access=AttrWriteType.READ_WRITE)
        def decorator_tuple_hint_in_write(self):
            if return_time_quality:
                return self.attr_value, time.time(), AttrQuality.ATTR_VALID
            return self.attr_value

        @decorator_tuple_hint_in_write.write
        def decorator_tuple_hint_in_write(self, value: tuple_hint):
            self.attr_value = value

        @attribute(access=AttrWriteType.READ_WRITE, max_dim_x=5, max_dim_y=5)
        def decorator_user_size_priority_over_hint(self) -> tuple_hint:
            if return_time_quality:
                return self.attr_value, time.time(), AttrQuality.ATTR_VALID
            return self.attr_value

        @decorator_user_size_priority_over_hint.write
        def decorator_user_size_priority_over_hint(self, value):
            self.attr_value = value

        @attribute(access=AttrWriteType.READ_WRITE, max_dim_x=5, max_dim_y=5)
        def decorator_list_hint(self) -> list_hint:
            if return_time_quality:
                return self.attr_value, time.time(), AttrQuality.ATTR_VALID
            return self.attr_value

        @decorator_list_hint.write
        def decorator_list_hint(self, value: tuple_hint):
            self.attr_value = value

        @command()
        def reset(self):
            self.attr_value = None

    def check_attribute_with_size(proxy, attr, value, size_x, size_y):
        setattr(proxy, attr, value)
        assert_close(getattr(proxy, attr), expected(value))
        conf = proxy.get_attribute_config(attr)
        if check_x_dim:
            assert conf.max_dim_x == size_x
        if check_y_dim:
            assert conf.max_dim_y == size_y
        proxy.reset()

    with DeviceTestContext(TestDevice) as proxy:
        for value in values:
            check_attribute_with_size(proxy, "hint_with_tuple", value, 3, 2)
            check_attribute_with_size(
                proxy, "user_size_priority_over_hint", value, 5, 5
            )
            check_attribute_with_size(proxy, "hint_with_list", value, 5, 5)
            check_attribute_with_size(proxy, "decorator_tuple_hint", value, 3, 2)
            check_attribute_with_size(
                proxy, "decorator_tuple_hint_in_write", value, 3, 2
            )
            check_attribute_with_size(
                proxy, "decorator_user_size_priority_over_hint", value, 5, 5
            )
            check_attribute_with_size(proxy, "decorator_list_hint", value, 5, 5)


def test_attribute_self_typed_with_not_defined_name():
    _value = [None]

    def non_bound_read(device: "TestDevice") -> int:
        return _value[0]

    def non_bound_read_no_return_hint(device: "TestDevice"):
        return _value[0]

    def non_bound_write(device: "TestDevice", val_in: int):
        _value[0] = val_in

    class TestDevice(Device):
        _value = None

        assignment_attr: int = attribute(
            access=AttrWriteType.READ_WRITE, fget="read_attr", fset="write_attr"
        )

        non_bound_attr: int = attribute(
            access=AttrWriteType.READ_WRITE, fget=non_bound_read, fset=non_bound_write
        )

        non_bound_attr_in_write: int = attribute(
            access=AttrWriteType.READ_WRITE,
            fget=non_bound_read_no_return_hint,
            fset=non_bound_write,
        )

        def read_attr(self: "TestDevice"):
            return self._value

        def write_attr(self: "TestDevice", val_in):
            self._value = val_in

        @attribute
        def decorator_attr(self: "TestDevice") -> int:
            return self._value

        @decorator_attr.write
        def set_value(self: "TestDevice", val_in: int):
            self._value = val_in

        @attribute
        def decorator_attr_def_in_write(self: "TestDevice"):
            return self._value

        @decorator_attr_def_in_write.write
        def set_value_2(self: "TestDevice", val_in: int):
            self._value = val_in

    with DeviceTestContext(TestDevice) as proxy:
        proxy.assignment_attr = 1
        assert 1 == proxy.assignment_attr
        proxy.decorator_attr = 2
        assert 2 == proxy.decorator_attr
        proxy.decorator_attr_def_in_write = 3
        assert 3 == proxy.decorator_attr_def_in_write

        proxy.non_bound_attr = 1
        assert 1 == proxy.non_bound_attr
        proxy.non_bound_attr_in_write = 2
        assert 2 == proxy.non_bound_attr_in_write


def test_read_write_attribute_with_unbound_functions(server_green_mode):
    v = {"attr": None}
    is_allowed = None

    if server_green_mode == GreenMode.Asyncio:

        async def read_attr(device):
            assert isinstance(device, TestDevice)
            return v["attr"]

        async def write_attr(device, val):
            assert isinstance(device, TestDevice)
            v["attr"] = val

        async def is_attr_allowed(device, req_type):
            assert isinstance(device, TestDevice)
            assert req_type in (AttReqType.READ_REQ, AttReqType.WRITE_REQ)
            return is_allowed

    else:

        def read_attr(device):
            assert isinstance(device, TestDevice)
            return v["attr"]

        def write_attr(device, val):
            assert isinstance(device, TestDevice)
            v["attr"] = val

        def is_attr_allowed(device, req_type):
            assert isinstance(device, TestDevice)
            assert req_type in (AttReqType.READ_REQ, AttReqType.WRITE_REQ)
            return is_allowed

    class TestDevice(Device):
        green_mode = server_green_mode

        attr = attribute(
            fget=read_attr,
            fset=write_attr,
            fisallowed=is_attr_allowed,
            dtype=int,
            access=AttrWriteType.READ_WRITE,
        )

    with DeviceTestContext(TestDevice) as proxy:
        is_allowed = True
        proxy.attr = 123
        assert proxy.attr == 123

        is_allowed = False
        with pytest.raises(DevFailed):
            proxy.attr = 123
        with pytest.raises(DevFailed):
            _ = proxy.attr


def test_read_write_attribute_decorated_methods(server_green_mode):
    class TestDevice(Device):
        green_mode = server_green_mode

        attr_value = None
        is_allowed = None

        attr = attribute(dtype=int, access=AttrWriteType.READ_WRITE)

        sync_code = textwrap.dedent(
            """\
            @general_decorator
            def read_attr(self):
                return self.attr_value

            @general_decorator
            def write_attr(self, value):
                self.attr_value = value

            @general_decorator
            def is_attr_allowed(self, req_type):
                assert req_type in (AttReqType.READ_REQ, AttReqType.WRITE_REQ)
                return self.is_allowed
            """
        )

        if server_green_mode != GreenMode.Asyncio:
            exec(sync_code)
        else:
            exec(sync_code.replace("def ", "async def "))

        @command(dtype_in=bool)
        def make_allowed(self, yesno):
            self.is_allowed = yesno

    with DeviceTestContext(TestDevice) as proxy:
        proxy.make_allowed(True)
        proxy.attr = 123
        assert proxy.attr == 123

        proxy.make_allowed(False)
        with pytest.raises(DevFailed):
            proxy.attr = 123
        with pytest.raises(DevFailed):
            _ = proxy.attr


@pytest.mark.parametrize("auto_size", [True, False])
def test_read_write_wvalue_attribute(
    attribute_typed_values, server_green_mode, auto_size
):
    dtype, values, expected = attribute_typed_values

    class TestDevice(Device):
        green_mode = server_green_mode
        value = None

        @attribute(
            dtype=dtype, max_dim_x=3, max_dim_y=3, access=AttrWriteType.READ_WRITE
        )
        def attr(self):
            return self.value

        @attr.write
        def attr(self, value):
            self.value = value
            w_attr = self.get_device_attr().get_w_attr_by_name("attr")
            if auto_size:
                w_attr.set_write_value(value)
            else:
                fmt = w_attr.get_data_format()
                if fmt == AttrDataFormat.SPECTRUM:
                    w_attr.set_write_value(value, len(value))
                elif fmt == AttrDataFormat.IMAGE:
                    w_attr.set_write_value(value, len(value[0]), len(value))
                else:
                    w_attr.set_write_value(value)

    with DeviceTestContext(TestDevice) as proxy:
        for value in values:
            proxy.attr = value
            assert_close(proxy.attr, expected(proxy.read_attribute("attr").w_value))


def test_write_read_empty_spectrum_attribute(extract_as, base_type):
    requested_type, expected_type = extract_as

    if requested_type == ExtractAs.Numpy and base_type == str:
        expected_type = tuple

    if (
        requested_type in [ExtractAs.ByteArray, ExtractAs.Bytes, ExtractAs.String]
        and base_type == str
    ):
        pytest.xfail(
            "Conversion from (str,) to ByteArray, Bytes and String not supported. May be fixed in future"
        )

    class TestDevice(Device):
        attr_value = []

        @attribute(dtype=(base_type,), max_dim_x=3, access=AttrWriteType.READ_WRITE)
        def attr(self):
            return self.attr_value

        @attr.write
        def attr(self, value):
            self.attr_value = value

        @command(dtype_out=bool)
        def is_attr_empty_list(self):
            if base_type in [int, float, bool]:
                expected_numpy_type = FROM_TANGO_TO_NUMPY_TYPE[TO_TANGO_TYPE[base_type]]
                assert self.attr_value.dtype == np.dtype(expected_numpy_type)
            else:
                assert isinstance(self.attr_value, list)
            assert len(self.attr_value) == 0

    with DeviceTestContext(TestDevice) as proxy:
        # first we read init value
        attr_read = proxy.read_attribute("attr", extract_as=requested_type)
        assert isinstance(attr_read.value, expected_type)
        assert len(attr_read.value) == 0
        # then we write empty list and check if it was really written
        proxy.attr = []
        proxy.is_attr_empty_list()
        # and finally, we read it again and check the value and wvalue
        attr_read = proxy.read_attribute("attr", extract_as=requested_type)
        assert isinstance(attr_read.value, expected_type)
        assert len(attr_read.value) == 0
        assert isinstance(attr_read.w_value, expected_type)
        assert len(attr_read.w_value) == 0


@pytest.mark.parametrize(
    "device_impl_class", [Device_4Impl, Device_5Impl, LatestDeviceImpl]
)
def test_write_read_empty_spectrum_attribute_classic_api(
    device_impl_class, extract_as, base_type
):
    requested_type, expected_type = extract_as

    if requested_type == ExtractAs.Numpy and base_type == str:
        expected_type = tuple

    if (
        requested_type in [ExtractAs.ByteArray, ExtractAs.Bytes, ExtractAs.String]
        and base_type == str
    ):
        pytest.xfail(
            "Conversion from (str,) to ByteArray, Bytes and String not supported. May be fixed in future"
        )

    class ClassicAPIClass(DeviceClass):
        cmd_list = {"is_attr_empty_list": [[DevVoid, "none"], [DevBoolean, "none"]]}
        attr_list = {
            "attr": [[TO_TANGO_TYPE[base_type], SPECTRUM, AttrWriteType.READ_WRITE, 10]]
        }

        def __init__(self, name):
            super().__init__(name)
            self.set_type("TestDevice")

    class ClassicAPIDeviceImpl(device_impl_class):
        attr_value = []

        def read_attr(self, attr):
            attr.set_value(self.attr_value)

        def write_attr(self, attr):
            w_value = attr.get_write_value()
            self.attr_value = w_value

        def is_attr_empty_list(self):
            if base_type in [int, float, bool]:
                expected_numpy_type = FROM_TANGO_TO_NUMPY_TYPE[TO_TANGO_TYPE[base_type]]
                assert self.attr_value.dtype == np.dtype(expected_numpy_type)
            else:
                assert isinstance(self.attr_value, list)
            assert len(self.attr_value) == 0

    with DeviceTestContext(ClassicAPIDeviceImpl, ClassicAPIClass) as proxy:
        # first we read init value
        attr_read = proxy.read_attribute("attr", extract_as=requested_type)
        assert isinstance(attr_read.value, expected_type)
        assert len(attr_read.value) == 0
        # then we write empty list and check if it was really written
        proxy.attr = []
        proxy.is_attr_empty_list()
        # and finally, we read it again and check the value and wvalue
        attr_read = proxy.read_attribute("attr", extract_as=requested_type)
        assert isinstance(attr_read.value, expected_type)
        assert len(attr_read.value) == 0
        assert isinstance(attr_read.w_value, expected_type)
        assert len(attr_read.w_value) == 0


@pytest.mark.parametrize("dtype", ["state", DevState, CmdArgType.DevState])
def test_ensure_devstate_is_pytango_enum(attr_data_format, dtype):
    if attr_data_format == AttrDataFormat.SCALAR:
        value = DevState.ON
    elif attr_data_format == AttrDataFormat.SPECTRUM:
        dtype = (dtype,)
        value = (DevState.ON, DevState.RUNNING)
    else:
        dtype = ((dtype,),)
        value = ((DevState.ON, DevState.RUNNING), (DevState.UNKNOWN, DevState.MOVING))

    class TestDevice(Device):
        @attribute(dtype=dtype, access=AttrWriteType.READ, max_dim_x=3, max_dim_y=3)
        def any_name_for_state_attribute(self):
            return value

    with DeviceTestContext(TestDevice) as proxy:
        states = proxy.any_name_for_state_attribute
        assert states == value
        check_attr_type(states, attr_data_format, DevState)


def test_read_write_attribute_enum(server_green_mode, attr_data_format):
    values = (member.value for member in GoodEnum)
    enum_labels = get_enum_labels(GoodEnum)

    if attr_data_format == AttrDataFormat.SCALAR:
        good_type = GoodEnum
        good_type_str = "DevEnum"
    elif attr_data_format == AttrDataFormat.SPECTRUM:
        good_type = (GoodEnum,)
        good_type_str = ("DevEnum",)
    else:
        good_type = ((GoodEnum,),)
        good_type_str = (("DevEnum",),)

    class TestDevice(Device):
        green_mode = server_green_mode

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if attr_data_format == AttrDataFormat.SCALAR:
                self.attr_from_enum_value = 0
                self.attr_from_labels_value = 0
            elif attr_data_format == AttrDataFormat.SPECTRUM:
                self.attr_from_enum_value = (0,)
                self.attr_from_labels_value = (0,)
            else:
                self.attr_from_enum_value = ((0,),)
                self.attr_from_labels_value = ((0,),)

        @attribute(
            dtype=good_type, max_dim_x=3, max_dim_y=3, access=AttrWriteType.READ_WRITE
        )
        def attr_from_enum(self):
            return self.attr_from_enum_value

        @attr_from_enum.write
        def attr_from_enum(self, value):
            self.attr_from_enum_value = value

        @attribute(
            dtype=good_type_str,
            max_dim_x=3,
            max_dim_y=3,
            enum_labels=enum_labels,
            access=AttrWriteType.READ_WRITE,
        )
        def attr_from_labels(self):
            return self.attr_from_labels_value

        @attr_from_labels.write
        def attr_from_labels(self, value):
            self.attr_from_labels_value = value

    with DeviceTestContext(TestDevice) as proxy:
        for value, label in zip(values, enum_labels):
            nd_value = make_nd_value(value, attr_data_format)
            proxy.attr_from_enum = nd_value
            read_attr = proxy.attr_from_enum
            assert read_attr == nd_value
            check_attr_type(read_attr, attr_data_format, enum.IntEnum)
            check_read_attr(read_attr, attr_data_format, value, label)

            proxy.attr_from_labels = nd_value
            read_attr = proxy.attr_from_labels
            assert read_attr == nd_value
            check_attr_type(read_attr, attr_data_format, enum.IntEnum)
            check_read_attr(read_attr, attr_data_format, value, label)

        for value, label in zip(values, enum_labels):
            nd_label = make_nd_value(label, attr_data_format)
            proxy.attr_from_enum = nd_label
            read_attr = proxy.attr_from_enum
            assert read_attr == nd_label
            check_attr_type(read_attr, attr_data_format, enum.IntEnum)
            check_read_attr(read_attr, attr_data_format, value, label)

            proxy.attr_from_labels = nd_label
            read_attr = proxy.attr_from_labels
            assert read_attr == nd_label
            check_attr_type(read_attr, attr_data_format, enum.IntEnum)
            check_read_attr(read_attr, attr_data_format, value, label)

    with pytest.raises(TypeError) as context:

        class BadTestDevice(Device):
            green_mode = server_green_mode

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                if attr_data_format == AttrDataFormat.SCALAR:
                    self.attr_value = 0
                elif attr_data_format == AttrDataFormat.SPECTRUM:
                    self.attr_value = (0,)
                else:
                    self.attr_value = ((0,),)

            # enum_labels may not be specified if dtype is an enum.Enum
            @attribute(
                dtype=good_type, max_dim_x=3, max_dim_y=3, enum_labels=enum_labels
            )
            def bad_attr(self):
                return self.attr_value

        BadTestDevice()  # dummy instance for Codacy
    assert "enum_labels" in str(context.value)


@pytest.mark.parametrize("enum_type", [DevState, GoodEnum])
def test_enum_devstate_attribute_declared_with_typing(attr_data_format, enum_type):
    value = DevState.MOVING if enum_type is DevState else GoodEnum.MIDDLE
    expected_type = DevState if enum_type is DevState else enum.IntEnum
    nd_value = make_nd_value(value, attr_data_format)

    if attr_data_format == AttrDataFormat.SCALAR:
        EnumType = enum_type
    elif attr_data_format == AttrDataFormat.SPECTRUM:
        EnumType = tuple[enum_type, enum_type, enum_type]
    else:
        EnumType = tuple[
            tuple[enum_type, enum_type, enum_type],
            tuple[enum_type, enum_type, enum_type],
            tuple[enum_type, enum_type, enum_type],
        ]

    class TestDevice(Device):
        attr: EnumType = attribute(access=AttrWriteType.READ)

        def read_attr(self):
            return nd_value

    with DeviceTestContext(TestDevice) as proxy:
        read_value = proxy.attr
        assert read_value == nd_value
        check_attr_type(read_value, attr_data_format, expected_type)
        if enum_type is GoodEnum:
            check_read_attr(read_value, attr_data_format, value, "MIDDLE")


def test_read_attribute_with_invalid_quality_is_none(attribute_typed_values):
    dtype, values, expected = attribute_typed_values

    class TestDevice(Device):
        @attribute(dtype=dtype, max_dim_x=3, max_dim_y=3)
        def attr(self):
            dummy_time = 123.4
            return values[0], dummy_time, AttrQuality.ATTR_INVALID

    with DeviceTestContext(TestDevice) as proxy:
        reading = proxy.read_attribute("attr")
        assert reading.value is None
        assert reading.quality is AttrQuality.ATTR_INVALID
        high_level_value = proxy.attr
        assert high_level_value is None


def test_read_enum_attribute_with_invalid_quality_is_none():
    class TestDevice(Device):
        @attribute(dtype=GoodEnum)
        def attr(self):
            dummy_time = 123.4
            return GoodEnum.START, dummy_time, AttrQuality.ATTR_INVALID

    with DeviceTestContext(TestDevice) as proxy:
        reading = proxy.read_attribute("attr")
        assert reading.value is None
        assert reading.quality is AttrQuality.ATTR_INVALID
        high_level_value = proxy.attr
        assert high_level_value is None


def test_wrong_attribute_read(server_green_mode):
    class TestDevice(Device):
        green_mode = server_green_mode

        @attribute(dtype=str)
        def attr_str_err(self):
            return 1.2345

        @attribute(dtype=int)
        def attr_int_err(self):
            return "bla"

        @attribute(dtype=[str])
        def attr_str_list_err(self):
            return ["hello", 55]

    with DeviceTestContext(TestDevice) as proxy:
        with pytest.raises(DevFailed):
            proxy.attr_str_err
        with pytest.raises(DevFailed):
            proxy.attr_int_err
        with pytest.raises(DevFailed):
            proxy.attr_str_list_err


def test_attribute_access_with_default_method_names(server_green_mode):
    class TestDevice(Device):
        green_mode = server_green_mode
        _read_write_value = ""
        _is_allowed = True

        attr_r = attribute(dtype=str)
        attr_rw = attribute(dtype=str, access=AttrWriteType.READ_WRITE)

        # the following methods are written in plain text which looks
        # weird. This is done so that it is easy to change for async
        # tests without duplicating all the code.
        synchronous_code = textwrap.dedent(
            """\
            def read_attr_r(self):
                return "readable"

            def read_attr_rw(self):
                print(f'Return value {self._read_write_value}')
                return self._read_write_value
    
            def write_attr_rw(self, value):
                print(f'Get value {value}')
                self._read_write_value = value
    
            def is_attr_r_allowed(self, req_type):
                assert req_type in (AttReqType.READ_REQ, AttReqType.WRITE_REQ)
                return self._is_allowed
    
            def is_attr_rw_allowed(self, req_type):
                assert req_type in (AttReqType.READ_REQ, AttReqType.WRITE_REQ)
                return self._is_allowed
    
            """
        )

        @command(dtype_in=bool)
        def make_allowed(self, yesno):
            self._is_allowed = yesno

        asynchronous_code = synchronous_code.replace("def ", "async def ")

        if server_green_mode != GreenMode.Asyncio:
            exec(synchronous_code)
        else:
            exec(asynchronous_code)

    with DeviceTestContext(TestDevice) as proxy:
        proxy.make_allowed(True)
        with pytest.raises(DevFailed):
            proxy.attr_r = "writable"
        assert proxy.attr_r == "readable"
        proxy.attr_rw = "writable"
        assert proxy.attr_rw == "writable"

        proxy.make_allowed(False)
        with pytest.raises(DevFailed):
            _ = proxy.attr_r
        with pytest.raises(DevFailed):
            proxy.attr_rw = "writing_not_allowed"
        with pytest.raises(DevFailed):
            _ = proxy.attr_rw


@pytest.fixture(
    ids=["low_level_read", "high_level_read"],
    params=[
        textwrap.dedent(
            """\
                        def read_dyn_attr(self, attr):
                            attr.set_value(self.attr_value)
                            """
        ),
        textwrap.dedent(
            """\
                        def read_dyn_attr(self, attr):
                            return self.attr_value
                            """
        ),
    ],
)
def dynamic_attribute_read_function(request):
    return request.param


def test_read_write_dynamic_attribute(
    dynamic_attribute_read_function, server_green_mode
):
    class TestDevice(Device):
        green_mode = server_green_mode

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.attr_value = None

        @command
        def add_dyn_attr(self):
            attr = attribute(
                name="dyn_attr",
                dtype=int,
                access=AttrWriteType.READ_WRITE,
                fget=self.read_dyn_attr,
                fset=self.write_dyn_attr,
            )
            self.add_attribute(attr)

        @command
        def delete_dyn_attr(self):
            self.remove_attribute("dyn_attr")

        sync_write = textwrap.dedent(
            """\
            def write_dyn_attr(self, attr):
                self.attr_value = attr.get_write_value()
        """
        )

        if server_green_mode != GreenMode.Asyncio:
            exec(dynamic_attribute_read_function)
            exec(sync_write)
        else:
            exec(dynamic_attribute_read_function.replace("def ", "async def "))
            exec(sync_write.replace("def ", "async def "))

    with DeviceTestContext(TestDevice) as proxy:
        proxy.add_dyn_attr()
        proxy.dyn_attr = 123
        assert proxy.dyn_attr == 123
        proxy.delete_dyn_attr()
        assert "dyn_attr" not in proxy.get_attribute_list()


def test_dynamic_attribute_declared_with_typing(attribute_typed_values):
    dtype, values, expected = attribute_typed_values
    tuple_hint, list_hint, check_x_dim, check_y_dim = convert_dtype_to_typing_hint(
        dtype
    )

    class TestDevice(Device):
        attr_value = None

        def initialize_dynamic_attributes(self):
            attr = attribute(
                name="read_function_tuple_hint",
                access=AttrWriteType.READ_WRITE,
                fget=self.read_attr_with_tuple_hints,
                fset=self.write_attr_no_hints,
            )
            self.add_attribute(attr)

            attr = attribute(
                name="user_size_priority_over_hint",
                max_dim_x=5,
                max_dim_y=5,
                access=AttrWriteType.READ_WRITE,
                fget=self.read_attr_with_tuple_hints,
                fset=self.write_attr_no_hints,
            )
            self.add_attribute(attr)

            attr = attribute(
                name="read_function_list_hint",
                access=AttrWriteType.READ_WRITE,
                max_dim_x=5,
                max_dim_y=5,
                fget=self.read_attr_with_list_hints,
                fset=self.write_attr_no_hints,
            )
            self.add_attribute(attr)

            attr = attribute(
                name="write_function_tuple_hint",
                access=AttrWriteType.READ_WRITE,
                fget=self.read_attr_no_hints,
                fset=self.write_attr_with_tuple_hints,
            )
            self.add_attribute(attr)

            attr = attribute(
                name="write_function_list_hint",
                access=AttrWriteType.READ_WRITE,
                max_dim_x=5,
                max_dim_y=5,
                fget=self.read_attr_no_hints,
                fset=self.write_attr_with_list_hints,
            )
            self.add_attribute(attr)

        def read_attr_no_hints(self, attr):
            return self.attr_value

        def write_attr_no_hints(self, attr):
            self.attr_value = attr.get_write_value()

        def read_attr_with_tuple_hints(self, attr) -> tuple_hint:
            return self.attr_value

        def read_attr_with_list_hints(self, attr) -> list_hint:
            return self.attr_value

        def write_attr_with_tuple_hints(self, attr: tuple_hint):
            self.attr_value = attr.get_write_value()

        def write_attr_with_list_hints(self, attr: list_hint):
            self.attr_value = attr.get_write_value()

        @command()
        def reset(self):
            self.attr_value = None

    def check_attribute_with_size(proxy, attr, value, size_x, size_y):
        setattr(proxy, attr, value)
        assert_close(getattr(proxy, attr), expected(value))
        conf = proxy.get_attribute_config(attr)
        if check_x_dim:
            assert conf.max_dim_x == size_x
        if check_y_dim:
            assert conf.max_dim_y == size_y
        proxy.reset()

    with DeviceTestContext(TestDevice) as proxy:
        for value in values:
            check_attribute_with_size(proxy, "read_function_tuple_hint", value, 3, 2)
            check_attribute_with_size(proxy, "read_function_list_hint", value, 5, 5)
            check_attribute_with_size(
                proxy, "user_size_priority_over_hint", value, 5, 5
            )
            check_attribute_with_size(proxy, "write_function_tuple_hint", value, 3, 2)
            check_attribute_with_size(proxy, "write_function_list_hint", value, 5, 5)


def test_dynamic_attribute_self_typed_with_not_defined_name():
    _value = [None]

    def non_bound_read(device: "TestDevice", attr) -> int:
        return _value[0]

    def non_bound_read_no_return_hint(device: "TestDevice", attr):
        return _value[0]

    def non_bound_write(device: "TestDevice", attr: int):
        _value[0] = attr.get_write_value()

    class TestDevice(Device):
        _value = None

        def initialize_dynamic_attributes(self):
            attr = attribute(
                name="read_with_hint",
                access=AttrWriteType.READ_WRITE,
                fget=self.read_attr,
                fset=self.write_attr,
            )
            self.add_attribute(attr)

            attr = attribute(
                name="read_no_hint",
                access=AttrWriteType.READ_WRITE,
                fget=self.read_attr_no_hint,
                fset=self.write_attr,
            )
            self.add_attribute(attr)

            attr = attribute(
                name="non_bound_read_with_hint",
                access=AttrWriteType.READ_WRITE,
                fget=non_bound_read,
                fset=non_bound_write,
            )
            self.add_attribute(attr)

            attr = attribute(
                name="non_bound_read_no_hint",
                access=AttrWriteType.READ_WRITE,
                fget=non_bound_read_no_return_hint,
                fset=non_bound_write,
            )
            self.add_attribute(attr)

        def read_attr(self: "TestDevice", attr) -> int:
            return self._value

        def read_attr_no_hint(self: "TestDevice", attr):
            return self._value

        def write_attr(self: "TestDevice", attr: int):
            self._value = attr.get_write_value()

    with DeviceTestContext(TestDevice) as proxy:
        proxy.read_with_hint = 1
        assert 1 == proxy.read_with_hint
        proxy.read_no_hint = 2
        assert 2 == proxy.read_no_hint

        proxy.non_bound_read_with_hint = 1
        assert 1 == proxy.non_bound_read_with_hint
        proxy.non_bound_read_no_hint = 2
        assert 2 == proxy.non_bound_read_no_hint


if npt:

    def test_attribute_declared_with_numpy_typing(attribute_numpy_typed_values):
        type_hint, dformat, value, expected = attribute_numpy_typed_values

        class TestDevice(Device):
            attr_value = None

            statement_declaration: type_hint = attribute(
                access=AttrWriteType.READ_WRITE,
                fget="read_attr",
                fset="write_attr",
                dformat=dformat,
                max_dim_x=2,
                max_dim_y=2,
            )

            def read_attr(self):
                return self.attr_value

            def write_attr(self, value):
                self.attr_value = value

            def initialize_dynamic_attributes(self):
                attr = attribute(
                    name="dynamic_declaration",
                    access=AttrWriteType.READ_WRITE,
                    fget=self.read_dynamic_attr,
                    fset=self.write_dynamic_attr,
                    dformat=dformat,
                    max_dim_x=2,
                    max_dim_y=2,
                )
                self.add_attribute(attr)

            def read_dynamic_attr(self, attr):
                return self.attr_value

            def write_dynamic_attr(self, attr):
                self.attr_value = attr.get_write_value()

            @attribute(
                access=AttrWriteType.READ_WRITE,
                dformat=dformat,
                max_dim_x=2,
                max_dim_y=2,
            )
            def decorator_declaration(self) -> type_hint:
                return self.attr_value

            @decorator_declaration.write
            def decorator_declaration_write(self, value: type_hint):
                self.attr_value = value

            @command()
            def reset(self):
                self.attr_value = None

        def check_attribute(proxy, attr, value):
            setattr(proxy, attr, value)
            assert_close(getattr(proxy, attr), expected(value))
            proxy.reset()

        with DeviceTestContext(TestDevice) as proxy:
            check_attribute(proxy, "statement_declaration", value)
            check_attribute(proxy, "decorator_declaration", value)
            check_attribute(proxy, "dynamic_declaration", value)

    def test_attribute_wrong_declared_with_numpy_typing(attribute_wrong_numpy_typed):
        dformat, max_x, max_y, value, error, match = attribute_wrong_numpy_typed

        with pytest.raises(error, match=match):

            class TestDevice(Device):
                attr_value = None

                attr: npt.NDArray[np.int_] = attribute(
                    access=AttrWriteType.READ_WRITE,
                    dformat=dformat,
                    max_dim_x=max_x,
                    max_dim_y=max_y,
                )

                def read_attr(self):
                    return self.attr_value

                def write_attr(self, value):
                    self.attr_value = value

            with DeviceTestContext(TestDevice) as proxy:
                proxy.attr = value
                _ = proxy.attr


def test_read_write_dynamic_attribute_decorated_methods_default_names(
    server_green_mode,
):
    class TestDevice(Device):
        green_mode = server_green_mode

        attr_value = None
        is_allowed = None

        def initialize_dynamic_attributes(self):
            attr = attribute(name="attr", dtype=int, access=AttrWriteType.READ_WRITE)
            self.add_attribute(attr)

        sync_code = textwrap.dedent(
            """\
        @general_decorator
        def read_attr(self, attr):
            return self.attr_value

        @general_decorator
        def write_attr(self, attr):
            self.attr_value = attr.get_write_value()

        @general_decorator
        def is_attr_allowed(self, req_type):
            assert req_type in (AttReqType.READ_REQ, AttReqType.WRITE_REQ)
            return self.is_allowed
        """
        )

        if server_green_mode != GreenMode.Asyncio:
            exec(sync_code)
        else:
            exec(sync_code.replace("def ", "async def "))

        @command(dtype_in=bool)
        def make_allowed(self, yesno):
            self.is_allowed = yesno

    with DeviceTestContext(TestDevice) as proxy:
        proxy.make_allowed(True)
        proxy.attr = 123
        assert proxy.attr == 123

        proxy.make_allowed(False)
        with pytest.raises(DevFailed):
            proxy.attr = 123
        with pytest.raises(DevFailed):
            _ = proxy.attr


def test_read_write_dynamic_attribute_decorated_methods_user_names(server_green_mode):
    class TestDevice(Device):
        green_mode = server_green_mode

        attr_value = None
        is_allowed = None

        def initialize_dynamic_attributes(self):
            attr = attribute(
                name="attr",
                dtype=int,
                access=AttrWriteType.READ_WRITE,
                fget=self.user_read,
                fset=self.user_write,
                fisallowed=self.user_is_allowed,
            )
            self.add_attribute(attr)

        sync_code = textwrap.dedent(
            """\
        @general_decorator
        def user_read(self, attr):
            return self.attr_value

        @general_decorator
        def user_write(self, attr):
            self.attr_value = attr.get_write_value()

        @general_decorator
        def user_is_allowed(self, req_type):
            assert req_type in (AttReqType.READ_REQ, AttReqType.WRITE_REQ)
            return self.is_allowed
        """
        )

        if server_green_mode != GreenMode.Asyncio:
            exec(sync_code)
        else:
            exec(sync_code.replace("def ", "async def "))

        @command(dtype_in=bool)
        def make_allowed(self, yesno):
            self.is_allowed = yesno

    with DeviceTestContext(TestDevice) as proxy:
        proxy.make_allowed(True)
        proxy.attr = 123
        assert proxy.attr == 123

        proxy.make_allowed(False)
        with pytest.raises(DevFailed):
            proxy.attr = 123
        with pytest.raises(DevFailed):
            _ = proxy.attr


def test_read_write_dynamic_attribute_decorated_shared_user_functions(
    server_green_mode,
):
    class TestDevice(Device):
        green_mode = server_green_mode

        attr_values = {"attr1": None, "attr2": None}
        is_allowed = None

        def initialize_dynamic_attributes(self):
            attr = attribute(
                name="attr1",
                dtype=int,
                access=AttrWriteType.READ_WRITE,
                fget=self.user_read,
                fset=self.user_write,
                fisallowed=self.user_is_allowed,
            )
            self.add_attribute(attr)
            attr = attribute(
                name="attr2",
                dtype=int,
                access=AttrWriteType.READ_WRITE,
                fget=self.user_read,
                fset=self.user_write,
                fisallowed=self.user_is_allowed,
            )
            self.add_attribute(attr)

        sync_code = textwrap.dedent(
            """\
        @general_decorator
        def user_read(self, attr):
            return self.attr_values[attr.get_name()]

        @general_decorator
        def user_write(self, attr):
            self.attr_values[attr.get_name()] = attr.get_write_value()

        @general_decorator
        def user_is_allowed(self, req_type):
            assert req_type in (AttReqType.READ_REQ, AttReqType.WRITE_REQ)
            return self.is_allowed
        """
        )

        if server_green_mode != GreenMode.Asyncio:
            exec(sync_code)
        else:
            exec(sync_code.replace("def ", "async def "))

        @command(dtype_in=bool)
        def make_allowed(self, yesno):
            self.is_allowed = yesno

    with DeviceTestContext(TestDevice) as proxy:
        proxy.make_allowed(True)
        proxy.attr1 = 123
        assert proxy.attr1 == 123
        proxy.attr2 = 456
        assert proxy.attr1 == 123
        assert proxy.attr2 == 456

        proxy.make_allowed(False)
        with pytest.raises(DevFailed):
            proxy.attr1 = 123
        with pytest.raises(DevFailed):
            _ = proxy.attr1
        with pytest.raises(DevFailed):
            proxy.attr2 = 123
        with pytest.raises(DevFailed):
            _ = proxy.attr2


def test_read_write_dynamic_attribute_enum(server_green_mode, attr_data_format):
    values = (member.value for member in GoodEnum)
    enum_labels = get_enum_labels(GoodEnum)

    if attr_data_format == AttrDataFormat.SCALAR:
        attr_type = DevEnum
        attr_info = (DevEnum, attr_data_format, READ_WRITE)
    elif attr_data_format == AttrDataFormat.SPECTRUM:
        attr_type = (DevEnum,)
        attr_info = (DevEnum, attr_data_format, READ_WRITE, 10)
    else:
        attr_type = ((DevEnum,),)
        attr_info = (DevEnum, attr_data_format, READ_WRITE, 10, 10)

    class TestDevice(Device):
        green_mode = server_green_mode

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if attr_data_format == AttrDataFormat.SCALAR:
                self.attr_value = 0
            elif attr_data_format == AttrDataFormat.SPECTRUM:
                self.attr_value = (0,)
            else:
                self.attr_value = ((0,),)

        @command
        def add_dyn_attr_old(self):
            attr = AttrData(
                "dyn_attr",
                None,
                attr_info=[
                    attr_info,
                    {"enum_labels": enum_labels},
                ],
            )
            self.add_attribute(
                attr, r_meth=self.read_dyn_attr, w_meth=self.write_dyn_attr
            )

        @command
        def add_dyn_attr_new(self):
            attr = attribute(
                name="dyn_attr",
                dtype=attr_type,
                max_dim_x=3,
                max_dim_y=3,
                access=AttrWriteType.READ_WRITE,
                fget=self.read_dyn_attr,
                fset=self.write_dyn_attr,
            )
            self.add_attribute(attr)

        @command
        def delete_dyn_attr(self):
            self.remove_attribute("dyn_attr")

        sync_code = textwrap.dedent(
            """\
            def read_dyn_attr(self, attr):
                return self.attr_value

            def write_dyn_attr(self, attr):
                self.attr_value = attr.get_write_value()
                """
        )

        if server_green_mode != GreenMode.Asyncio:
            exec(sync_code)
        else:
            exec(sync_code.replace("def ", "async def "))

    with DeviceTestContext(TestDevice) as proxy:
        for add_attr_cmd in [proxy.add_dyn_attr_old, proxy.add_dyn_attr_new]:
            add_attr_cmd()
            for value, label in zip(values, enum_labels):
                nd_value = make_nd_value(value, attr_data_format)
                proxy.dyn_attr = nd_value
                read_attr = proxy.dyn_attr
                assert read_attr == nd_value
                check_attr_type(read_attr, attr_data_format, enum.IntEnum)
                check_read_attr(read_attr, attr_data_format, value, label)
            proxy.delete_dyn_attr()
            assert "dyn_attr" not in proxy.get_attribute_list()


@pytest.mark.parametrize("enum_type", [DevState, GoodEnum])
def test_enum_devstate_dynamic_attribute_declared_with_typing(
    attr_data_format, enum_type
):
    value = DevState.MOVING if enum_type is DevState else GoodEnum.MIDDLE
    expected_type = DevState if enum_type is DevState else enum.IntEnum
    nd_value = make_nd_value(value, attr_data_format)

    if attr_data_format == AttrDataFormat.SCALAR:
        EnumType = enum_type
    elif attr_data_format == AttrDataFormat.SPECTRUM:
        EnumType = tuple[enum_type, enum_type, enum_type]
    else:
        EnumType = tuple[
            tuple[enum_type, enum_type, enum_type],
            tuple[enum_type, enum_type, enum_type],
        ]

    class TestDevice(Device):
        def initialize_dynamic_attributes(self):
            self.add_attribute(attribute(name="attr", access=AttrWriteType.READ))

        def read_attr(self, attr) -> EnumType:
            return nd_value

    with DeviceTestContext(TestDevice) as proxy:
        read_value = proxy.attr
        assert read_value == nd_value
        check_attr_type(read_value, attr_data_format, expected_type)
        if enum_type is GoodEnum:
            check_read_attr(read_value, attr_data_format, value, "MIDDLE")


def test_read_write_dynamic_attribute_is_allowed_with_async(server_green_mode):
    class TestDevice(Device):
        green_mode = server_green_mode

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for att_num in range(1, 7):
                setattr(self, f"attr{att_num}_allowed", True)
            for att_num in range(1, 7):
                setattr(self, f"attr{att_num}_value", None)

        def initialize_dynamic_attributes(self):
            # recommended approach: using attribute() and bound methods:
            attr = attribute(
                name="dyn_attr1",
                dtype=int,
                access=AttrWriteType.READ_WRITE,
                fget=self.read_dyn_attr1,
                fset=self.write_dyn_attr1,
                fisallowed=self.is_attr1_allowed,
            )
            self.add_attribute(attr)

            # not recommended: using attribute() with unbound methods:
            attr = attribute(
                name="dyn_attr2",
                dtype=int,
                access=AttrWriteType.READ_WRITE,
                fget=TestDevice.read_dyn_attr2,
                fset=TestDevice.write_dyn_attr2,
                fisallowed=TestDevice.is_attr2_allowed,
            )
            self.add_attribute(attr)

            # possible approach: using attribute() with method name strings:
            attr = attribute(
                name="dyn_attr3",
                dtype=int,
                access=AttrWriteType.READ_WRITE,
                fget="read_dyn_attr3",
                fset="write_dyn_attr3",
                fisallowed="is_attr3_allowed",
            )
            self.add_attribute(attr)

            # old approach: using tango.AttrData with bound methods:
            attr_name = "dyn_attr4"
            data_info = self._get_attr_data_info()
            dev_class = self.get_device_class()
            attr_data = AttrData(attr_name, dev_class.get_name(), data_info)
            self.add_attribute(
                attr_data,
                self.read_dyn_attr4,
                self.write_dyn_attr4,
                self.is_attr4_allowed,
            )

            # old approach: using tango.AttrData with unbound methods:
            attr_name = "dyn_attr5"
            attr_data = AttrData(attr_name, dev_class.get_name(), data_info)
            self.add_attribute(
                attr_data,
                TestDevice.read_dyn_attr5,
                TestDevice.write_dyn_attr5,
                TestDevice.is_attr5_allowed,
            )

            # old approach: using tango.AttrData with default method names
            attr_name = "dyn_attr6"
            attr_data = AttrData(attr_name, dev_class.get_name(), data_info)
            self.add_attribute(attr_data)

        def _get_attr_data_info(self):
            simple_type, fmt = get_tango_type_format(int)
            data_info = [[simple_type, fmt, READ_WRITE]]
            return data_info

        @command(dtype_in=bool)
        def make_allowed(self, yesno):
            for att_num in range(1, 7):
                setattr(self, f"attr{att_num}_allowed", yesno)

        # the following methods are written in plain text which looks
        # weird. This is done so that it is easy to change for async
        # tests without duplicating all the code.
        read_code = textwrap.dedent(
            """\
            def read_dyn_attr(self, attr):
                return self.attr_value
                """
        )

        write_code = textwrap.dedent(
            """\
            def write_dyn_attr(self, attr):
                self.attr_value = attr.get_write_value()
                """
        )

        is_allowed_code = textwrap.dedent(
            """\
            def is_attr_allowed(self, req_type):
                assert req_type in (AttReqType.READ_REQ, AttReqType.WRITE_REQ)
                return self.attr_allowed
            """
        )

        for attr_num in range(1, 7):
            read_method = read_code.replace("read_dyn_attr", f"read_dyn_attr{attr_num}")
            read_method = read_method.replace("attr_value", f"attr{attr_num}_value")
            write_method = write_code.replace(
                "write_dyn_attr", f"write_dyn_attr{attr_num}"
            )
            write_method = write_method.replace("attr_value", f"attr{attr_num}_value")
            if attr_num < 6:
                is_allowed_method = is_allowed_code.replace(
                    "is_attr_allowed", f"is_attr{attr_num}_allowed"
                )
            else:
                # default name differs
                is_allowed_method = is_allowed_code.replace(
                    "is_attr_allowed", f"is_dyn_attr{attr_num}_allowed"
                )
            is_allowed_method = is_allowed_method.replace(
                "self.attr_allowed", f"self.attr{attr_num}_allowed"
            )

            if server_green_mode != GreenMode.Asyncio:
                exec(read_method)
                exec(write_method)
                exec(is_allowed_method)
            else:
                exec(read_method.replace("def ", "async def "))
                exec(write_method.replace("def ", "async def "))
                exec(is_allowed_method.replace("def ", "async def "))

    with DeviceTestContext(TestDevice) as proxy:
        proxy.make_allowed(True)
        proxy.dyn_attr1 = 1
        assert proxy.dyn_attr1 == 1

        proxy.dyn_attr2 = 2
        assert proxy.dyn_attr2 == 2

        proxy.dyn_attr3 = 3
        assert proxy.dyn_attr3 == 3

        proxy.dyn_attr4 = 4
        assert proxy.dyn_attr4 == 4

        proxy.dyn_attr5 = 5
        assert proxy.dyn_attr5 == 5

        proxy.dyn_attr6 = 6
        assert proxy.dyn_attr6 == 6

        proxy.make_allowed(False)
        with pytest.raises(DevFailed):
            proxy.dyn_attr1 = 1
        with pytest.raises(DevFailed):
            _ = proxy.dyn_attr1
        with pytest.raises(DevFailed):
            proxy.dyn_attr2 = 2
        with pytest.raises(DevFailed):
            _ = proxy.dyn_attr2
        with pytest.raises(DevFailed):
            proxy.dyn_attr3 = 3
        with pytest.raises(DevFailed):
            _ = proxy.dyn_attr3
        with pytest.raises(DevFailed):
            proxy.dyn_attr4 = 4
        with pytest.raises(DevFailed):
            _ = proxy.dyn_attr4
        with pytest.raises(DevFailed):
            proxy.dyn_attr5 = 5
        with pytest.raises(DevFailed):
            _ = proxy.dyn_attr5
        with pytest.raises(DevFailed):
            proxy.dyn_attr6 = 6
        with pytest.raises(DevFailed):
            _ = proxy.dyn_attr6


@pytest.mark.parametrize("use_green_mode", [True, False])
def test_dynamic_attribute_with_green_mode(use_green_mode, server_green_mode):
    class TestDevice(Device):
        green_mode = server_green_mode
        attr_value = 123

        def initialize_dynamic_attributes(self):
            global executor
            executor = get_executor(server_green_mode)
            attr = attribute(
                name="attr_r",
                dtype=int,
                access=AttrWriteType.READ,
                fget=self.user_read,
                read_green_mode=use_green_mode,
            )
            self.add_attribute(attr)
            attr = attribute(
                name="attr_rw",
                dtype=int,
                access=AttrWriteType.READ_WRITE,
                fget=self.user_read,
                fset=self.user_write,
                read_green_mode=use_green_mode,
                write_green_mode=use_green_mode,
            )
            self.add_attribute(attr)
            attr = attribute(
                name="attr_ia",
                dtype=int,
                access=AttrWriteType.READ,
                fget=self.user_read,
                fisallowed=self.user_is_allowed,
                read_green_mode=use_green_mode,
                isallowed_green_mode=use_green_mode,
            )
            self.add_attribute(attr)
            attr = attribute(
                name="attr_rw_always_ok",
                dtype=int,
                access=AttrWriteType.READ_WRITE,
                fget=self.user_read,
                fset=self.user_write,
                green_mode=True,
            )
            self.add_attribute(attr)

        def user_read(self, attr):
            self.assert_executor_context_correct(attr.get_name())
            return self.attr_value

        def user_write(self, attr):
            self.assert_executor_context_correct(attr.get_name())
            self.attr_value = attr.get_write_value()

        def user_is_allowed(self, req_type):
            self.assert_executor_context_correct()
            assert req_type in (AttReqType.READ_REQ, AttReqType.WRITE_REQ)
            return True

        def assert_executor_context_correct(self, attr_name=""):
            check_required = attr_name != "attr_rw_always_ok"
            if check_required and executor.asynchronous:
                assert executor.in_executor_context() == use_green_mode

    with DeviceTestContext(TestDevice) as proxy:
        assert proxy.attr_r == 123
        proxy.attr_rw = 456
        assert proxy.attr_rw == 456
        assert proxy.attr_ia == 456


@pytest.mark.parametrize(
    "device_impl_class", [Device_4Impl, Device_5Impl, LatestDeviceImpl]
)
def test_dynamic_attribute_using_classic_api_like_sardana(device_impl_class):
    class ClassicAPIClass(DeviceClass):
        cmd_list = {
            "make_allowed": [[DevBoolean, "allow access"], [DevVoid, "none"]],
        }

        def __init__(self, name):
            super().__init__(name)
            self.set_type("TestDevice")

    class ClassicAPIDeviceImpl(device_impl_class):
        def __init__(self, cl, name):
            super().__init__(cl, name)
            ClassicAPIDeviceImpl.init_device(self)

        def init_device(self):
            self._attr1 = 3.14
            self._is_test_attr_allowed = True
            read = self.__class__._read_attr
            write = self.__class__._write_attr
            is_allowed = self.__class__._is_attr_allowed
            attr_name = "attr1"
            data_info = [[DevDouble, SCALAR, READ_WRITE]]
            dev_class = self.get_device_class()
            attr_data = AttrData(attr_name, dev_class.get_name(), data_info)
            self.add_attribute(attr_data, read, write, is_allowed)

        def _is_attr_allowed(self, req_type):
            assert req_type in (AttReqType.READ_REQ, AttReqType.WRITE_REQ)
            return self._is_test_attr_allowed

        def _read_attr(self, attr):
            attr.set_value(self._attr1)

        def _write_attr(self, attr):
            w_value = attr.get_write_value()
            self._attr1 = w_value

        def make_allowed(self, yesno):
            self._is_test_attr_allowed = yesno

    with DeviceTestContext(ClassicAPIDeviceImpl, ClassicAPIClass) as proxy:
        proxy.make_allowed(True)
        assert proxy.attr1 == 3.14
        proxy.attr1 = 42.0
        assert proxy.attr1 == 42.0

        proxy.make_allowed(False)
        with pytest.raises(DevFailed):
            _ = proxy.attr1
        with pytest.raises(DevFailed):
            proxy.attr1 = 12.0


@pytest.mark.parametrize("read_function_signature", ["low_level", "high_level"])
@pytest.mark.parametrize("patched", [True, False])
def test_dynamic_attribute_with_unbound_functions(
    read_function_signature, patched, server_green_mode
):
    value = {"attr": None}
    is_allowed = None

    if server_green_mode == GreenMode.Asyncio:

        async def low_level_read_function(device, attr):
            assert isinstance(device, TestDevice)
            attr.set_value(value["attr"])

        async def high_level_read_function(device, attr):
            assert isinstance(device, TestDevice)
            return value["attr"]

        async def write_function(device, attr):
            assert isinstance(device, TestDevice)
            value["attr"] = attr.get_write_value()

        async def is_allowed_function(device, req_type):
            assert isinstance(device, TestDevice)
            assert req_type in (AttReqType.READ_REQ, AttReqType.WRITE_REQ)
            return is_allowed

    else:

        def low_level_read_function(device, attr):
            assert isinstance(device, TestDevice)
            attr.set_value(value["attr"])

        def high_level_read_function(device, attr):
            assert isinstance(device, TestDevice)
            return value["attr"]

        def write_function(device, attr):
            assert isinstance(device, TestDevice)
            value["attr"] = attr.get_write_value()

        def is_allowed_function(device, req_type):
            assert isinstance(device, TestDevice)
            assert req_type in (AttReqType.READ_REQ, AttReqType.WRITE_REQ)
            return is_allowed

    class TestDevice(Device):
        green_mode = server_green_mode

        def initialize_dynamic_attributes(self):
            if read_function_signature == "low_level":
                read_function = low_level_read_function
            elif read_function_signature == "high_level":
                read_function = high_level_read_function

            # trick to run server with non device method: patch __dict__
            if patched:
                self.__dict__["read_dyn_attr1"] = read_function
                self.__dict__["write_dyn_attr1"] = write_function
                self.__dict__["is_dyn_attr1_allowed"] = is_allowed_function
                attr = attribute(
                    name="dyn_attr1", dtype=int, access=AttrWriteType.READ_WRITE
                )
                self.add_attribute(attr)

                setattr(self, "read_dyn_attr2", read_function)
                setattr(self, "write_dyn_attr2", write_function)
                setattr(self, "is_dyn_attr2_allowed", is_allowed_function)
                attr = attribute(
                    name="dyn_attr2", dtype=int, access=AttrWriteType.READ_WRITE
                )
                self.add_attribute(attr)

            else:
                attr = attribute(
                    name="dyn_attr",
                    fget=read_function,
                    fset=write_function,
                    fisallowed=is_allowed_function,
                    dtype=int,
                    access=AttrWriteType.READ_WRITE,
                )
                self.add_attribute(attr)

    with DeviceTestContext(TestDevice) as proxy:
        is_allowed = True
        if patched:
            proxy.dyn_attr1 = 123
            assert proxy.dyn_attr1 == 123

            proxy.dyn_attr2 = 456
            assert proxy.dyn_attr2 == 456
        else:
            proxy.dyn_attr = 789
            assert proxy.dyn_attr == 789

        is_allowed = False
        if patched:
            with pytest.raises(DevFailed):
                proxy.dyn_attr1 = 123

            with pytest.raises(DevFailed):
                _ = proxy.dyn_attr1

            with pytest.raises(DevFailed):
                proxy.dyn_attr2 = 456

            with pytest.raises(DevFailed):
                _ = proxy.dyn_attr2
        else:
            with pytest.raises(DevFailed):
                proxy.dyn_attr = 123

            with pytest.raises(DevFailed):
                _ = proxy.dyn_attr


def test_attribute_decorators(server_green_mode):
    class TestDevice(Device):
        green_mode = server_green_mode
        current_value = None
        voltage_value = None
        is_allowed = None

        current = attribute(label="Current", unit="mA", dtype=float)
        voltage = attribute(label="Voltage", unit="V", dtype=float)

        sync_code = textwrap.dedent(
            """
        @current.getter
        def cur_read(self):
            return self.current_value

        @current.setter
        def cur_write(self, current):
            self.current_value = current

        @current.is_allowed
        def cur_allo(self, req_type):
            return self.is_allowed

        @voltage.read
        def vol_read(self):
            return self.voltage_value

        @voltage.write
        def vol_write(self, voltage):
            self.voltage_value = voltage

        @voltage.is_allowed
        def vol_allo(self, req_type):
            return self.is_allowed
        """
        )

        @command(dtype_in=bool)
        def make_allowed(self, yesno):
            self.is_allowed = yesno

        if server_green_mode == GreenMode.Asyncio:
            exec(sync_code.replace("def ", "async def "))
        else:
            exec(sync_code)

    with DeviceTestContext(TestDevice) as proxy:
        proxy.make_allowed(True)
        proxy.current = 2.0
        assert_close(proxy.current, 2.0)
        proxy.voltage = 3.0
        assert_close(proxy.voltage, 3.0)

        proxy.make_allowed(False)
        with pytest.raises(DevFailed):
            proxy.current = 4.0
        with pytest.raises(DevFailed):
            _ = proxy.current
        with pytest.raises(DevFailed):
            proxy.voltage = 4.0
        with pytest.raises(DevFailed):
            _ = proxy.voltage


def test_read_only_dynamic_attribute_with_dummy_write_method(
    dynamic_attribute_read_function, server_green_mode
):
    def dummy_write_method():
        return None

    class TestDevice(Device):
        green_mode = server_green_mode

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.attr_value = 123

        def initialize_dynamic_attributes(self):
            self.add_attribute(
                Attr("dyn_attr", DevLong, AttrWriteType.READ),
                r_meth=self.read_dyn_attr,
                w_meth=dummy_write_method,
            )

        sync_code = textwrap.dedent(
            """\
            def read_dyn_attr(self, attr):
                return self.attr_value
                """
        )

        if server_green_mode != GreenMode.Asyncio:
            exec(sync_code)
        else:
            exec(sync_code.replace("def ", "async def "))

    with DeviceTestContext(TestDevice) as proxy:
        assert proxy.dyn_attr == 123


def test_dynamic_attribute_with_method_in_other_class(server_green_mode):
    class Helper:
        value = 0
        is_allowed = True

        def read_method(self, device, attr):
            assert isinstance(self, Helper)
            assert isinstance(device, TestDevice)
            assert attr.get_name() == "dyn_attr"
            return self.value

        def write_method(self, device, attr):
            assert isinstance(self, Helper)
            assert isinstance(device, TestDevice)
            assert attr.get_name() == "dyn_attr"
            self.value = attr.get_write_value()

        def is_allowed_method(self, device, req_type):
            assert isinstance(self, Helper)
            assert isinstance(device, TestDevice)
            assert req_type in (AttReqType.READ_REQ, AttReqType.WRITE_REQ)
            return Helper.is_allowed

    class TestDevice(Device):
        green_mode = server_green_mode

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = Helper()

        def initialize_dynamic_attributes(self):
            self.add_attribute(
                Attr("dyn_attr", DevLong, AttrWriteType.READ_WRITE),
                r_meth=self.helper.read_method,
                w_meth=self.helper.write_method,
                is_allo_meth=self.helper.is_allowed_method,
            )

    with DeviceTestContext(TestDevice) as proxy:
        Helper.is_allowed = True
        proxy.dyn_attr = 123
        assert proxy.dyn_attr == 123

        Helper.is_allowed = False
        with pytest.raises(DevFailed):
            proxy.dyn_attr = 456
        with pytest.raises(DevFailed):
            _ = proxy.dyn_attr


# Test properties


def test_device_property_no_default(command_typed_values, server_green_mode):
    dtype, values, expected = command_typed_values
    patched_dtype = dtype if dtype != (bool,) else (int,)
    value = values[1]

    class TestDevice(Device):
        green_mode = server_green_mode

        prop_without_db_value = device_property(dtype=dtype)
        prop_with_db_value = device_property(dtype=dtype)

        @command(dtype_out=bool)
        def is_prop_without_db_value_set_to_none(self):
            return self.prop_without_db_value is None

        @command(dtype_out=patched_dtype)
        def get_prop_with_db_value(self):
            return self.prop_with_db_value

    with DeviceTestContext(
        TestDevice, properties={"prop_with_db_value": value}
    ) as proxy:
        assert proxy.is_prop_without_db_value_set_to_none()
        assert_close(proxy.get_prop_with_db_value(), expected(value))


def test_device_property_with_typing(command_typed_values):
    dtype, values, expected = command_typed_values
    patched_dtype = dtype if dtype != (bool,) else (int,)
    value = values[1]

    tuple_hint, list_hint, _, _ = convert_dtype_to_typing_hint(dtype)

    class TestDevice(Device):
        prop_tuple_hint: tuple_hint = device_property()

        prop_list_hint: list_hint = device_property()

        prop_user_type_has_priority: dict = device_property(dtype=dtype)

        @command(dtype_out=patched_dtype)
        def get_prop_tuple_hint(self):
            return self.prop_tuple_hint

        @command(dtype_out=patched_dtype)
        def get_prop_list_hint(self):
            return self.prop_list_hint

        @command(dtype_out=patched_dtype)
        def get_prop_user_type_has_priority(self):
            return self.prop_user_type_has_priority

    with DeviceTestContext(
        TestDevice,
        properties={
            "prop_tuple_hint": value,
            "prop_list_hint": value,
            "prop_user_type_has_priority": value,
        },
    ) as proxy:
        assert_close(proxy.get_prop_tuple_hint(), expected(value))
        assert_close(proxy.get_prop_list_hint(), expected(value))
        assert_close(proxy.get_prop_user_type_has_priority(), expected(value))


if npt:

    def test_device_property_with_numpy_typing(command_numpy_typed_values):
        type_hint, dformat, value, expected = command_numpy_typed_values
        if type_hint in [np.uint8, npt.NDArray[np.uint8]]:
            pytest.xfail("Does not work for some reason")

        class TestDevice(Device):
            prop: type_hint = device_property()

            @command(dformat_out=dformat)
            def get_prop(self) -> type_hint:
                return self.prop

        with DeviceTestContext(TestDevice, properties={"prop": value}) as proxy:
            assert_close(proxy.get_prop(), expected(value))


def test_device_property_with_default_value(command_typed_values):
    dtype, values, expected = command_typed_values
    patched_dtype = dtype if dtype != (bool,) else (int,)

    default = values[0]
    value = values[1]

    class TestDevice(Device):
        prop_without_db_value = device_property(dtype=dtype, default_value=default)
        prop_with_db_value = device_property(dtype=dtype, default_value=default)

        @command(dtype_out=patched_dtype)
        def get_prop_without_db_value(self):
            return self.prop_without_db_value

        @command(dtype_out=patched_dtype)
        def get_prop_with_db_value(self):
            return self.prop_with_db_value

    with DeviceTestContext(
        TestDevice, properties={"prop_with_db_value": value}
    ) as proxy:
        assert_close(proxy.get_prop_without_db_value(), expected(default))
        assert_close(proxy.get_prop_with_db_value(), expected(value))


def test_device_get_device_properties_when_init_device(server_green_mode):
    class TestDevice(Device):
        green_mode = server_green_mode
        _got_properties = False

        def get_device_properties(self, *args, **kwargs):
            super().get_device_properties(*args, **kwargs)
            self._got_properties = True

        @attribute(dtype=bool)
        def got_properties(self):
            return self._got_properties

    with DeviceTestContext(TestDevice) as proxy:
        assert proxy.got_properties


def test_device_get_attr_config(server_green_mode):
    class TestDevice(Device):
        green_mode = server_green_mode

        @attribute(dtype=bool)
        def attr_config_ok(self):
            # testing that call to get_attribute_config for all types of
            # input arguments gives same result and doesn't raise an exception
            ac1 = self.get_attribute_config(b"attr_config_ok")
            ac2 = self.get_attribute_config("attr_config_ok")
            ac3 = self.get_attribute_config(["attr_config_ok"])
            return repr(ac1) == repr(ac2) == repr(ac3)

    with DeviceTestContext(TestDevice) as proxy:
        assert proxy.attr_config_ok


def test_get_attr_config_ex(server_green_mode):
    class TestDevice(Device):
        green_mode = server_green_mode

        @attribute(dtype=int, unit="mA")
        def attr_config_int(self):
            return 1

        @attribute(dtype=bool)
        def attr_config_bool(self):
            return True

    def assert_attr_config_ok(dev_proxy):
        # testing that call to get_attribute_config_ex for all types of
        # input arguments gives same result and doesn't raise an exception
        ac1 = dev_proxy.get_attribute_config_ex("attr_config_int")
        ac2 = dev_proxy.get_attribute_config_ex(["attr_config_int"])
        assert repr(ac1) == repr(ac2)

    def assert_multiple_attrs_config_ok(dev_proxy):
        # testing that querying multiple attributes gives same result and
        # doesn't raise an exception
        ac1 = dev_proxy.get_attribute_config_ex("attr_config_int")
        ac2 = dev_proxy.get_attribute_config_ex("attr_config_bool")
        acs = dev_proxy.get_attribute_config_ex(("attr_config_int", "attr_config_bool"))
        acs_2 = dev_proxy.get_attribute_config_ex(
            ["attr_config_int", "attr_config_bool"]
        )

        acs_all = dev_proxy.get_attribute_config_ex(tango.constants.AllAttr)

        assert repr(ac1[0]) == repr(acs[0]) == repr(acs_2[0]) == repr(
            acs_all[0]
        ) and repr(ac2[0]) == repr(acs[1]) == repr(acs_2[1]) == repr(acs_all[1])

    with DeviceTestContext(TestDevice) as proxy:
        assert_attr_config_ok(proxy)
        assert_multiple_attrs_config_ok(proxy)


def test_default_units(server_green_mode):
    # testing that, by default tango.constants.UnitNotSpec is set
    # when no unit is specified. For bool, int, float and str dtypes
    class TestDevice(Device):
        green_mode = server_green_mode

        @attribute(dtype=bool)
        def attr_bool_ok(self):
            return True

        @attribute(dtype=int)
        def attr_int_ok(self):
            return 1

        @attribute(dtype=float)
        def attr_float_ok(self):
            return 1.0

        @attribute(dtype=str)
        def attr_str_ok(self):
            return "True"

    def assert_attr_bool_ok(dev_proxy):
        config = dev_proxy.get_attribute_config("attr_bool_ok")
        assert config.unit == tango.constants.UnitNotSpec

    def assert_attr_int_ok(dev_proxy):
        config = dev_proxy.get_attribute_config("attr_int_ok")
        assert config.unit == tango.constants.UnitNotSpec

    def assert_attr_float_ok(dev_proxy):
        config = dev_proxy.get_attribute_config("attr_float_ok")
        assert config.unit == tango.constants.UnitNotSpec

    def assert_attr_str_ok(dev_proxy):
        config = dev_proxy.get_attribute_config("attr_str_ok")
        assert config.unit == tango.constants.UnitNotSpec

    with DeviceTestContext(TestDevice) as proxy:
        assert_attr_bool_ok(proxy)
        assert_attr_int_ok(proxy)
        assert_attr_float_ok(proxy)
        assert_attr_str_ok(proxy)


def test_custom_units(server_green_mode):
    class TestDevice(Device):
        green_mode = server_green_mode

        @attribute(dtype=bool, unit="mA")
        def custom_unit_ok(self):
            return True

    def assert_custom_unit_ok(dev_proxy):
        config = dev_proxy.get_attribute_config("custom_unit_ok")
        assert config.unit == "mA"

    with DeviceTestContext(TestDevice) as proxy:
        assert_custom_unit_ok(proxy)


# Test inheritance


def test_inheritance_override_a_property(server_green_mode):
    class A(Device):
        green_mode = server_green_mode

        prop1 = device_property(dtype=str, default_value="hello1")
        prop2 = device_property(dtype=str, default_value="hello2")

        @command(dtype_out=str)
        def get_prop1(self):
            return self.prop1

        @command(dtype_out=str)
        def get_prop2(self):
            return self.prop2

    class B(A):
        prop2 = device_property(dtype=str, default_value="goodbye2")

    with DeviceTestContext(B) as proxy:
        assert proxy.get_prop1() == "hello1"
        assert proxy.get_prop2() == "goodbye2"


def test_inheritance_override_dev_status(server_green_mode):
    class A(Device):
        green_mode = server_green_mode

        def dev_status(self):
            return ")`'-.,_"

    class B(A):
        if server_green_mode == GreenMode.Asyncio:

            async def dev_status(self):
                coro = super(type(self), self).dev_status()
                result = await coro
                return 3 * result

        else:

            def dev_status(self):
                return 3 * A.dev_status(self)

    with DeviceTestContext(B) as proxy:
        assert proxy.status() == ")`'-.,_)`'-.,_)`'-.,_"


def test_inheritance_init_device(server_green_mode):
    class A(Device):
        green_mode = server_green_mode
        initialised_count_a = 0

        if server_green_mode == GreenMode.Asyncio:

            async def init_device(self):
                await super().init_device()
                self.initialised_count_a += 1

        else:

            def init_device(self):
                super().init_device()
                self.initialised_count_a += 1

        @command(dtype_out=int)
        def get_is_initialised_a(self):
            return self.initialised_count_a

    class B(A):
        initialised_count_b = 0

        if server_green_mode == GreenMode.Asyncio:

            async def init_device(self):
                await super().init_device()
                self.initialised_count_b += 1

        else:

            def init_device(self):
                super().init_device()
                self.initialised_count_b += 1

        @command(dtype_out=int)
        def get_is_initialised_b(self):
            return self.initialised_count_b

    with DeviceTestContext(B) as proxy:
        assert proxy.get_is_initialised_a() == 1
        assert proxy.get_is_initialised_b() == 1


def test_inheritance_with_decorated_attributes(server_green_mode):
    is_allowed = True

    class A(Device):
        green_mode = server_green_mode

        @attribute(access=AttrWriteType.READ_WRITE)
        def decorated_a(self):
            return self.decorated_a_value

        @decorated_a.setter
        def decorated_a(self, value):
            self.decorated_a_value = value

        @decorated_a.is_allowed
        def decorated_a(self, req_type):
            assert req_type in (AttReqType.READ_REQ, AttReqType.WRITE_REQ)
            return is_allowed

    class B(A):
        @attribute(access=AttrWriteType.READ_WRITE)
        def decorated_b(self):
            return self.decorated_b_value

        @decorated_b.setter
        def decorated_b(self, value):
            self.decorated_b_value = value

        @decorated_b.is_allowed
        def decorated_b(self, req_type):
            assert req_type in (AttReqType.READ_REQ, AttReqType.WRITE_REQ)
            return is_allowed

    with DeviceTestContext(B) as proxy:
        is_allowed = True

        proxy.decorated_a = 1.23
        assert proxy.decorated_a == 1.23
        proxy.decorated_b = 4.5
        assert proxy.decorated_b == 4.5

        is_allowed = False
        with pytest.raises(DevFailed):
            proxy.decorated_a = 1.0
        with pytest.raises(DevFailed):
            _ = proxy.decorated_a
        with pytest.raises(DevFailed):
            proxy.decorated_b = 1.0
        with pytest.raises(DevFailed):
            _ = proxy.decorated_b


def test_inheritance_with_undecorated_attributes(server_green_mode):
    is_allowed = True

    class A(Device):
        green_mode = server_green_mode

        attr_a = attribute(access=AttrWriteType.READ_WRITE)

        def read_attr_a(self):
            return self.attr_a_value

        def write_attr_a(self, value):
            self.attr_a_value = value

        def is_attr_a_allowed(self, req_type):
            assert req_type in (AttReqType.READ_REQ, AttReqType.WRITE_REQ)
            return is_allowed

    class B(A):
        attr_b = attribute(access=AttrWriteType.READ_WRITE)

        def read_attr_b(self):
            return self.attr_b_value

        def write_attr_b(self, value):
            self.attr_b_value = value

        def is_attr_b_allowed(self, req_type):
            assert req_type in (AttReqType.READ_REQ, AttReqType.WRITE_REQ)
            return is_allowed

    with DeviceTestContext(B) as proxy:
        is_allowed = True

        proxy.attr_a = 2.5
        assert proxy.attr_a == 2.5
        proxy.attr_b = 5.75
        assert proxy.attr_b == 5.75

        is_allowed = False
        with pytest.raises(DevFailed):
            proxy.attr_a = 1.0
        with pytest.raises(DevFailed):
            _ = proxy.attr_a
        with pytest.raises(DevFailed):
            proxy.attr_b = 1.0
        with pytest.raises(DevFailed):
            _ = proxy.attr_b


def test_inheritance_with_undecorated_attribute_and_bound_methods(server_green_mode):
    is_allowed = True

    class A(Device):
        attr_a = attribute(
            access=AttrWriteType.READ_WRITE,
            fget="get_attr_a",
            fset="set_attr_a",
            fisallowed="isallowed_attr_a",
        )

        def get_attr_a(self):
            return self.attr_value

        def set_attr_a(self, value):
            self.attr_value = value

        def isallowed_attr_a(self, req_type):
            assert req_type in (AttReqType.READ_REQ, AttReqType.WRITE_REQ)
            return is_allowed

    class B(A):
        attr_b = attribute(
            access=AttrWriteType.READ_WRITE,
            fget="get_attr_b",
            fset="set_attr_b",
            fisallowed="isallowed_attr_b",
        )

        def get_attr_b(self):
            return self.attr_value

        def set_attr_b(self, value):
            self.attr_value = value

        def isallowed_attr_b(self, req_type):
            assert req_type in (AttReqType.READ_REQ, AttReqType.WRITE_REQ)
            return is_allowed

    with DeviceTestContext(B) as proxy:
        is_allowed = True
        proxy.attr_a = 3.75
        assert proxy.attr_a == 3.75
        proxy.attr_b = 6.0
        assert proxy.attr_b == 6.0

        is_allowed = False
        with pytest.raises(DevFailed):
            proxy.attr_a = 1.0
        with pytest.raises(DevFailed):
            _ = proxy.attr_a
        with pytest.raises(DevFailed):
            proxy.attr_b = 1.0
        with pytest.raises(DevFailed):
            _ = proxy.attr_b


def test_inheritance_with_undecorated_attributes_and_unbound_functions(
    server_green_mode,
):
    is_allowed = True
    values = {"a": 0.0, "b": 0.0}

    def read_attr_a(device):
        assert isinstance(device, B)
        return values["a"]

    def write_attr_a(device, value):
        assert isinstance(device, B)
        values["a"] = value

    def is_attr_a_allowed(device, req_type):
        assert isinstance(device, B)
        assert req_type in (AttReqType.READ_REQ, AttReqType.WRITE_REQ)
        return is_allowed

    class A(Device):
        green_mode = server_green_mode

        attr_a = attribute(
            access=AttrWriteType.READ_WRITE,
            fget=read_attr_a,
            fset=write_attr_a,
            fisallowed=is_attr_a_allowed,
        )

    def read_attr_b(device):
        assert isinstance(device, B)
        return values["b"]

    def write_attr_b(device, value):
        assert isinstance(device, B)
        values["b"] = value

    def is_attr_b_allowed(device, req_type):
        assert isinstance(device, B)
        assert req_type in (AttReqType.READ_REQ, AttReqType.WRITE_REQ)
        return is_allowed

    class B(A):
        attr_b = attribute(
            access=AttrWriteType.READ_WRITE,
            fget=read_attr_b,
            fset=write_attr_b,
            fisallowed=is_attr_b_allowed,
        )

    with DeviceTestContext(B) as proxy:
        is_allowed = True

        proxy.attr_a = 2.5
        assert proxy.attr_a == 2.5
        proxy.attr_b = 5.75
        assert proxy.attr_b == 5.75

        is_allowed = False
        with pytest.raises(DevFailed):
            proxy.attr_a = 1.0
        with pytest.raises(DevFailed):
            _ = proxy.attr_a
        with pytest.raises(DevFailed):
            proxy.attr_b = 1.0
        with pytest.raises(DevFailed):
            _ = proxy.attr_b


def test_inheritance_command_is_allowed_by_naming_convention(server_green_mode):
    is_allowed = True

    class A(Device):
        green_mode = server_green_mode

        @command(dtype_out=str)
        def cmd(self):
            return "ok"

        def is_cmd_allowed(self):
            return is_allowed

    class B(A):
        pass

    with DeviceTestContext(B) as proxy:
        is_allowed = True
        assert proxy.cmd() == "ok"
        is_allowed = False
        with pytest.raises(DevFailed):
            proxy.cmd()


def test_inheritance_command_is_allowed_by_kwarg_method(server_green_mode):
    is_allowed = True

    class A(Device):
        green_mode = server_green_mode

        @command(dtype_out=str, fisallowed="fisallowed_kwarg_method")
        def cmd(self):
            return "ok 1"

        def fisallowed_kwarg_method(self):
            return is_allowed

    class B(A):
        pass

    with DeviceTestContext(B) as proxy:
        is_allowed = True
        assert proxy.cmd() == "ok 1"
        is_allowed = False
        with pytest.raises(DevFailed):
            proxy.cmd()


def test_inheritance_command_is_allowed_by_kwarg_unbound_function(server_green_mode):
    is_allowed = True

    def fisallowed_function(self):
        return is_allowed

    class A(Device):
        green_mode = server_green_mode

        @command(dtype_out=str, fisallowed=fisallowed_function)
        def cmd(self):
            return "ok"

    class B(A):
        pass

    with DeviceTestContext(B) as proxy:
        is_allowed = True
        assert proxy.cmd() == "ok"
        is_allowed = False
        with pytest.raises(DevFailed):
            proxy.cmd()


def test_polled_attribute(server_green_mode):
    dct = {"PolledAttribute1": 100, "PolledAttribute2": 100000, "PolledAttribute3": 500}

    class TestDevice(Device):
        green_mode = server_green_mode

        @attribute(polling_period=dct["PolledAttribute1"])
        def PolledAttribute1(self):
            return 42.0

        @attribute(polling_period=dct["PolledAttribute2"])
        def PolledAttribute2(self):
            return 43.0

        @attribute(polling_period=dct["PolledAttribute3"])
        def PolledAttribute3(self):
            return 44.0

    with DeviceTestContext(TestDevice) as proxy:
        ans = proxy.polling_status()
        for x in ans:
            lines = x.split("\n")
            attr = lines[0].split("= ")[1]
            poll_period = int(lines[1].split("= ")[1])
            assert dct[attr] == poll_period


def test_mandatory_device_property_with_db_value_succeeds(
    command_typed_values, server_green_mode
):
    dtype, values, expected = command_typed_values
    patched_dtype = dtype if dtype != (bool,) else (int,)
    default, value = values[:2]

    class TestDevice(Device):
        green_mode = server_green_mode

        prop = device_property(dtype=dtype, mandatory=True)

        @command(dtype_out=patched_dtype)
        def get_prop(self):
            return self.prop

    with DeviceTestContext(TestDevice, properties={"prop": value}) as proxy:
        assert_close(proxy.get_prop(), expected(value))


def test_mandatory_device_property_without_db_value_fails(
    command_typed_values, server_green_mode
):
    dtype, _, _ = command_typed_values

    class TestDevice(Device):
        green_mode = server_green_mode
        prop = device_property(dtype=dtype, mandatory=True)

    with pytest.raises(DevFailed) as context:
        with DeviceTestContext(TestDevice):
            pass
    assert "Device property prop is mandatory" in str(context.value)


def test_logging(server_green_mode):
    log_received = threading.Event()

    class LogSourceDevice(Device):
        green_mode = server_green_mode
        _last_log_time = 0.0

        @command(dtype_in=("str",))
        def log_fatal_message(self, msg):
            self._last_log_time = time.time()
            if len(msg) > 1:
                self.fatal_stream(msg[0], msg[1])
            else:
                self.fatal_stream(msg[0])

        @command(dtype_in=("str",))
        def log_error_message(self, msg):
            self._last_log_time = time.time()
            if len(msg) > 1:
                self.error_stream(msg[0], msg[1])
            else:
                self.error_stream(msg[0])

        @command(dtype_in=("str",))
        def log_warn_message(self, msg):
            self._last_log_time = time.time()
            if len(msg) > 1:
                self.warn_stream(msg[0], msg[1])
            else:
                self.warn_stream(msg[0])

        @command(dtype_in=("str",))
        def log_info_message(self, msg):
            self._last_log_time = time.time()
            if len(msg) > 1:
                self.info_stream(msg[0], msg[1])
            else:
                self.info_stream(msg[0])

        @command(dtype_in=("str",))
        def log_debug_message(self, msg):
            self._last_log_time = time.time()
            if len(msg) > 1:
                self.debug_stream(msg[0], msg[1])
            else:
                self.debug_stream(msg[0])

        @attribute(dtype=float)
        def last_log_time(self):
            return self._last_log_time

    class LogConsumerDevice(Device):
        green_mode = server_green_mode
        _last_log_data = []

        @command(dtype_in=("str",))
        def Log(self, argin):
            self._last_log_data = argin
            log_received.set()

        @attribute(dtype=int)
        def last_log_timestamp_ms(self):
            return int(self._last_log_data[0])

        @attribute(dtype=str)
        def last_log_level(self):
            return self._last_log_data[1]

        @attribute(dtype=str)
        def last_log_source(self):
            return self._last_log_data[2]

        @attribute(dtype=str)
        def last_log_message(self):
            return self._last_log_data[3]

        @attribute(dtype=str)
        def last_log_context_unused(self):
            return self._last_log_data[4]

        @attribute(dtype=str)
        def last_log_thread_id(self):
            return self._last_log_data[5]

    def assert_log_details_correct(level, msg):
        assert log_received.wait(0.5)
        _assert_log_time_close_enough()
        _assert_log_fields_correct_for_level(level, msg)
        log_received.clear()

    def _assert_log_time_close_enough():
        log_emit_time = proxy_source.last_log_time
        log_receive_time = proxy_consumer.last_log_timestamp_ms / 1000.0
        now = time.time()
        # cppTango logger time function may use a different
        # implementation to CPython's time.time().  This is
        # especially noticeable on Windows platforms.
        timer_implementation_tolerance = 0.020 if WINDOWS else 0.001
        min_time = log_emit_time - timer_implementation_tolerance
        max_time = now + timer_implementation_tolerance
        assert min_time <= log_receive_time <= max_time

    def _assert_log_fields_correct_for_level(level, msg):
        assert proxy_consumer.last_log_level == level.upper()
        assert proxy_consumer.last_log_source == "test/log/source"
        assert proxy_consumer.last_log_message == msg
        assert proxy_consumer.last_log_context_unused == ""
        assert len(proxy_consumer.last_log_thread_id) > 0

    devices_info = (
        {"class": LogSourceDevice, "devices": [{"name": "test/log/source"}]},
        {"class": LogConsumerDevice, "devices": [{"name": "test/log/consumer"}]},
    )

    with MultiDeviceTestContext(devices_info) as context:
        proxy_source = context.get_device("test/log/source")
        proxy_consumer = context.get_device("test/log/consumer")
        consumer_access = context.get_device_access("test/log/consumer")
        proxy_source.add_logging_target(f"device::{consumer_access}")

        for msg in ([""], [" with literal %s"], [" with string %s as arg", "foo"]):
            level = "fatal"
            log_msg = msg[:]
            log_msg[0] = "test " + level + msg[0]
            proxy_source.log_fatal_message(log_msg)
            if len(msg) > 1:
                check_log_msg = log_msg[0] % log_msg[1]
            else:
                check_log_msg = log_msg[0]
            assert_log_details_correct(level, check_log_msg)

            level = "error"
            log_msg = msg[:]
            log_msg[0] = "test " + level + msg[0]
            proxy_source.log_error_message(log_msg)
            if len(msg) > 1:
                check_log_msg = log_msg[0] % log_msg[1]
            else:
                check_log_msg = log_msg[0]
            assert_log_details_correct(level, check_log_msg)

            level = "warn"
            log_msg = msg[:]
            log_msg[0] = "test " + level + msg[0]
            proxy_source.log_warn_message(log_msg)
            if len(msg) > 1:
                check_log_msg = log_msg[0] % log_msg[1]
            else:
                check_log_msg = log_msg[0]
            assert_log_details_correct(level, check_log_msg)

            level = "info"
            log_msg = msg[:]
            log_msg[0] = "test " + level + msg[0]
            proxy_source.log_info_message(log_msg)
            if len(msg) > 1:
                check_log_msg = log_msg[0] % log_msg[1]
            else:
                check_log_msg = log_msg[0]
            assert_log_details_correct(level, check_log_msg)

            level = "debug"
            log_msg = msg[:]
            log_msg[0] = "test " + level + msg[0]
            proxy_source.log_debug_message(log_msg)
            if len(msg) > 1:
                check_log_msg = log_msg[0] % log_msg[1]
            else:
                check_log_msg = log_msg[0]
            assert_log_details_correct(level, check_log_msg)


@pytest.mark.skipif(
    not os.environ.get("PYTHONUNBUFFERED"),
    reason="This test requires PYTHONUNBUFFERED=1 to capture the outputs.",
)
def test_decorator_logging_source_location(server_green_mode, capfd):
    """Run decorated commands and attributes and verify that @InfoIt decorator
    always logs the correct location."""

    class InfoItDevice(Device):
        green_mode = server_green_mode

        @InfoIt()
        @command(dtype_out=int)
        def decorated_command(self):
            return inspect.currentframe().f_lineno

        @command(dtype_out=int)
        def run_decorated_method(self):
            return self.decorated_method()

        @InfoIt()
        @general_decorator
        def decorated_method(self):
            return inspect.currentframe().f_lineno

        @attribute(dtype=int)
        @InfoIt()
        def decorated_attribute(self):
            return inspect.currentframe().f_lineno

    with DeviceTestContext(InfoItDevice, debug=3) as device:
        filename = os.path.basename(__file__)
        for cmd, method in [
            ("decorated_command", "decorated_command"),
            ("run_decorated_method", "decorated_method"),
        ]:
            lineno = device.command_inout(cmd) - 3
            out, err = capfd.readouterr()  # calling this function clears the buffer
            assert (
                f"({filename}:{lineno}) test/nodb/infoitdevice -> InfoItDevice.{method}()"
                in out
            )

        lineno = device.decorated_attribute - 3
        out, err = capfd.readouterr()
        assert (
            f"({filename}:{lineno}) test/nodb/infoitdevice -> InfoItDevice.decorated_attribute()"
            in out
        )


@pytest.mark.skipif(
    not os.environ.get("PYTHONUNBUFFERED"),
    reason="This test requires PYTHONUNBUFFERED=1 to capture the outputs.",
)
def test_stream_logging_source_location(server_green_mode, capfd):
    class StreamLogsDevice(Device):
        green_mode = server_green_mode

        @command(dtype_out=int)
        def log_streams(self):
            self.info_stream("info")
            self.debug_stream("debug")
            self.warn_stream("warn")
            self.error_stream("error")
            self.fatal_stream("fatal")
            return inspect.currentframe().f_lineno

    with DeviceTestContext(StreamLogsDevice, debug=3) as device:
        lineno = device.command_inout("log_streams") - 5
        filename = os.path.basename(__file__)
        out, err = capfd.readouterr()
        for i, level in [
            (0, "INFO"),
            (1, "DEBUG"),
            (2, "WARN"),
            (3, "ERROR"),
            (4, "FATAL"),
        ]:
            assert (
                f"{level} ({filename}:{lineno + i}) test/nodb/streamlogsdevice" in out
            )


# fixtures


@pytest.fixture(params=[GoodEnum])
def good_enum(request):
    return request.param


@pytest.fixture(params=[BadEnumNonZero, BadEnumSkipValues, BadEnumDuplicates])
def bad_enum(request):
    return request.param


# test utilities for servers


def test_get_enum_labels_success(good_enum):
    expected_labels = ["START", "MIDDLE", "END"]
    assert get_enum_labels(good_enum) == expected_labels


def test_get_enum_labels_fail(bad_enum):
    with pytest.raises(EnumTypeError):
        get_enum_labels(bad_enum)


# DevEncoded


def test_read_write_dev_encoded(dev_encoded_values, server_green_mode):
    def check_ans(raw_ans, expected_type):
        assert len(raw_ans) == 2
        assert is_pure_str(raw_ans[0])
        if expected_type == bytes:
            assert isinstance(raw_ans[1], bytes)
            assert raw_ans[1] == UTF8_STRING.encode()
        elif expected_type == str:
            assert is_pure_str(raw_ans[1])
            assert raw_ans[1] == UTF8_STRING
        else:
            assert isinstance(raw_ans[1], bytearray)
            assert raw_ans[1] == bytearray(UTF8_STRING.encode())

    class TestDevice(Device):
        green_mode = server_green_mode
        attr_value = None
        command_value = None

        @attribute(dtype=DevEncoded, access=AttrWriteType.READ_WRITE)
        def attr(self):
            return self.attr_value

        @attr.write
        def attr(self, value):
            check_ans(value, bytes)
            self.attr_value = value

        @command(dtype_in=DevEncoded)
        def cmd_in(self, value):
            check_ans(value, bytes)
            self.command_value = value

        @command(dtype_out=DevEncoded)
        def cmd_out(self):
            return self.command_value

        @command(dtype_in=DevEncoded, dtype_out=DevEncoded)
        def cmd_in_out(self, value):
            check_ans(value, bytes)
            return value

    with DeviceTestContext(TestDevice) as proxy:
        proxy.attr = dev_encoded_values
        raw_ans = proxy.read_attribute("attr", extract_as=ExtractAs.Bytes)
        check_ans(raw_ans.value, bytes)
        check_ans(raw_ans.w_value, bytes)

        raw_ans = proxy.read_attribute("attr", extract_as=ExtractAs.String)
        check_ans(raw_ans.value, str)
        check_ans(raw_ans.w_value, str)

        raw_ans = proxy.read_attribute("attr", extract_as=ExtractAs.ByteArray)
        check_ans(raw_ans.value, bytearray)
        check_ans(raw_ans.w_value, bytearray)

        proxy.cmd_in(dev_encoded_values)
        raw_ans = proxy.cmd_out()
        check_ans(raw_ans, bytes)

        raw_ans = proxy.cmd_in_out(dev_encoded_values)
        check_ans(raw_ans, bytes)


def test_dev_encoded_wrong_encoding():
    class TestDevice(Device):
        @attribute(dtype=DevEncoded, access=AttrWriteType.READ)
        def attr_bad_encoding(self):
            return "utf-16", UTF8_STRING.encode("utf-16")

        @attribute(dtype=DevEncoded, access=AttrWriteType.READ)
        def attr_bad_string(self):
            return "bad_one", b"\xff"

    with DeviceTestContext(TestDevice) as proxy:
        with pytest.raises(UnicodeDecodeError):
            _ = proxy.read_attribute("attr_bad_encoding", extract_as=ExtractAs.String)

        with pytest.raises(UnicodeDecodeError):
            _ = proxy.read_attribute("attr_bad_string", extract_as=ExtractAs.String)


ENCODED_ATTRIBUTES = (  # encode function, decode function, data
    ("gray8", "gray8", np.array([np.arange(100, dtype=np.byte) for _ in range(5)])),
    ("gray16", "gray16", np.array([np.arange(100, dtype=np.int16) for _ in range(5)])),
    ("rgb24", "decode_24", np.ones((20, 10, 3), dtype=np.uint8)),
    (
        "jpeg_gray8",
        "gray8",
        np.array([np.arange(100, dtype=np.byte) for _ in range(5)]),
    ),
    ("jpeg_rgb24", None, np.ones((10, 10, 3), dtype=np.uint8)),
    ("jpeg_rgb32", "rgb32", np.zeros((10, 10, 3), dtype=np.uint8)),
)


def test_set_value_None():
    none_position = 0

    class TestDevice(Device):
        def init_device(self):
            super().init_device()
            attr = attribute(name="attr")
            self.add_attribute(attr, self._read_attr_that_raises)

            attr = attribute(name="attr_with_data_quality")
            self.add_attribute(attr, self._read_attr_with_date_quality_that_raises)

        def _read_attr_that_raises(self, attr):
            invalid_value = None
            attr.set_value(invalid_value)

        def _read_attr_with_date_quality_that_raises(self, attr):
            invalid_value = [1, 1, AttrQuality.ATTR_VALID]
            invalid_value[none_position] = None
            attr.set_value_date_quality(*invalid_value)

    with DeviceTestContext(TestDevice) as proxy:
        with pytest.raises(DevFailed, match="method cannot be called with None"):
            _ = proxy.attr

        for _ in range(3):
            with pytest.raises(DevFailed, match="method cannot be called with None"):
                _ = proxy.attr_with_data_quality
            none_position += 1


@pytest.mark.parametrize(
    "f_encode, f_decode, data",
    ENCODED_ATTRIBUTES,
    ids=[f_name for f_name, _, _ in ENCODED_ATTRIBUTES],
)
def test_encoded_attribute(f_encode, f_decode, data):
    if f_encode == "jpeg_rgb32":
        pytest.xfail(
            "jpeg_rgb32 needs cppTango built with TANGO_USE_JPEG option, so we skip this test"
        )

    class TestDevice(Device):
        @attribute(dtype=DevEncoded, access=AttrWriteType.READ)
        def attr(self):
            enc = EncodedAttribute()
            getattr(enc, f"encode_{f_encode}")(data)
            return enc

    def decode_24(data_to_decode):
        # first two bytes are width, then two bytes are height and then goes encoded image
        # see implementation of other decode methods, e.g.
        # https://gitlab.com/tango-controls/cppTango/-/blob/main/cppapi/server/encoded_attribute.cpp#L229
        width = int.from_bytes(data_to_decode[:2], byteorder="big")
        height = int.from_bytes(data_to_decode[2:4], byteorder="big")
        decoded_data = np.frombuffer(data_to_decode[4:], dtype=np.uint8)
        return decoded_data.reshape((height, width, 3))

    with DeviceTestContext(TestDevice) as proxy:
        if f_decode == "decode_24":
            ret = proxy.read_attribute("attr", extract_as=ExtractAs.Bytes)
            codec, ret_data = ret.value
            assert_close(decode_24(ret_data), data)
        elif f_decode is not None:
            ret = proxy.read_attribute("attr", extract_as=ExtractAs.Nothing)
            enc = EncodedAttribute()
            assert_close(getattr(enc, f"decode_{f_decode}")(ret), data)
        else:
            # for jpeg24 we test only encode
            pass


def test_dev_encoded_memory_usage():
    LARGE_DATA_SIZE = 10 * 1024 * 1024  # 1 Mb should be enough, but 10 more reliable
    NUM_CYCLES = 5

    def check_ans(raw_ans):
        assert len(raw_ans) == 2
        assert is_pure_str(raw_ans[0])
        assert isinstance(raw_ans[1], bytes)
        assert len(raw_ans[1]) == LARGE_DATA_SIZE
        if raw_ans[0] == "str":
            assert raw_ans[1] == b"a" * LARGE_DATA_SIZE
        elif raw_ans[0] == "bytes":
            assert raw_ans[1] == b"b" * LARGE_DATA_SIZE
        else:
            assert raw_ans[1] == b"c" * LARGE_DATA_SIZE

    class TestDevice(Device):
        attr_str_read = attribute(
            dtype=DevEncoded, access=AttrWriteType.READ, fget="read_str"
        )
        attr_str_write = attribute(
            dtype=DevEncoded, access=AttrWriteType.WRITE, fset="write_str"
        )
        attr_str_read_write = attribute(
            dtype=DevEncoded,
            access=AttrWriteType.READ_WRITE,
            fget="read_str",
            fset="write_str",
        )

        attr_bytes_read = attribute(
            dtype=DevEncoded, access=AttrWriteType.READ, fget="read_bytes"
        )
        attr_bytes_write = attribute(
            dtype=DevEncoded, access=AttrWriteType.WRITE, fset="write_bytes"
        )
        attr_bytes_read_write = attribute(
            dtype=DevEncoded,
            access=AttrWriteType.READ_WRITE,
            fget="read_bytes",
            fset="write_bytes",
        )

        attr_bytearray_read = attribute(
            dtype=DevEncoded, access=AttrWriteType.READ, fget="read_bytearray"
        )
        attr_bytearray_write = attribute(
            dtype=DevEncoded, access=AttrWriteType.WRITE, fset="write_bytearray"
        )
        attr_bytearray_read_write = attribute(
            dtype=DevEncoded,
            access=AttrWriteType.READ_WRITE,
            fget="read_bytearray",
            fset="write_bytearray",
        )

        def read_str(self):
            return "str", "a" * LARGE_DATA_SIZE

        def write_str(self, value):
            check_ans(value)

        def read_bytes(self):
            return "bytes", b"b" * LARGE_DATA_SIZE

        def write_bytes(self, value):
            check_ans(value)

        def read_bytearray(self):
            return "bytearray", bytearray(b"c" * LARGE_DATA_SIZE)

        def write_bytearray(self, value):
            check_ans(value)

        @command(dtype_in=DevEncoded, dtype_out=DevEncoded)
        def cmd_in_out(self, value):
            check_ans(value)
            if value[0] == "str":
                return "str", "a" * LARGE_DATA_SIZE
            elif value[0] == "bytes":
                return "bytes", b"b" * LARGE_DATA_SIZE
            else:
                return "bytearray", bytearray(b"c" * LARGE_DATA_SIZE)

    with DeviceTestContext(TestDevice) as proxy:
        last_memory_usage = None
        for cycle in range(NUM_CYCLES):
            proxy.attr_str_write = "str", "a" * LARGE_DATA_SIZE
            proxy.attr_bytes_write = "bytes", b"b" * LARGE_DATA_SIZE
            proxy.attr_bytearray_write = "bytearray", bytearray(b"c" * LARGE_DATA_SIZE)

            proxy.attr_str_read_write = "str", "a" * LARGE_DATA_SIZE
            proxy.attr_bytes_read_write = "bytes", b"b" * LARGE_DATA_SIZE
            proxy.attr_bytearray_read_write = "bytearray", bytearray(
                b"c" * LARGE_DATA_SIZE
            )

            check_ans(proxy.attr_str_read)
            check_ans(proxy.attr_bytes_read)
            check_ans(proxy.attr_bytearray_read)

            check_ans(proxy.attr_str_read_write)
            check_ans(proxy.attr_bytes_read_write)
            check_ans(proxy.attr_bytearray_read_write)

            check_ans(proxy.cmd_in_out(("str", "a" * LARGE_DATA_SIZE)))
            check_ans(proxy.cmd_in_out(("bytes", b"b" * LARGE_DATA_SIZE)))
            check_ans(
                proxy.cmd_in_out(("bytearray", bytearray(b"c" * LARGE_DATA_SIZE)))
            )

            current_memory_usage = int(psutil.Process(os.getpid()).memory_info().rss)
            if cycle > 2:  # first two cycles we memory usage grows....
                assert np.isclose(
                    last_memory_usage, current_memory_usage, atol=LARGE_DATA_SIZE / 2
                )
            last_memory_usage = current_memory_usage


# Test Exception propagation


def test_exception_propagation(server_green_mode):
    class TestDevice(Device):
        green_mode = server_green_mode

        @attribute
        def attr(self):
            1 / 0  # pylint: disable=pointless-statement

        @command
        def cmd(self):
            1 / 0  # pylint: disable=pointless-statement

    with DeviceTestContext(TestDevice) as proxy:
        with pytest.raises(DevFailed) as record:
            proxy.attr  # pylint: disable=pointless-statement
        assert "ZeroDivisionError" in record.value.args[0].desc

        with pytest.raises(DevFailed) as record:
            proxy.cmd()
        assert "ZeroDivisionError" in record.value.args[0].desc


def _avoid_double_colon_node_ids(val):
    """Return node IDs without a double colon.

    IDs with "::" can't be used to launch a test from the command line, as pytest
    considers this sequence as a module/test name separator.  Add something extra
    to keep them usable for single test command line execution (e.g., under Windows CI).
    """
    if is_pure_str(val) and "::" in val:
        return str(val).replace("::", ":_:")


@pytest.fixture(params=["linux", "win"])
def os_system(request):
    original_platform = sys.platform
    sys.platform = request.param
    yield
    sys.platform = original_platform


@pytest.mark.parametrize(
    "applicable_os, test_input, expected_output",
    DEVICE_SERVER_ARGUMENTS,
    ids=_avoid_double_colon_node_ids,
)
def test_arguments(applicable_os, test_input, expected_output, os_system):
    try:
        assert set(parse_args(test_input.split())) == set(expected_output)
    except SystemExit:
        assert sys.platform not in applicable_os


# Test Server init hook


def test_server_init_hook_called(server_green_mode):
    class TestDevice(Device):
        green_mode = server_green_mode
        server_init_hook_called = False

        def server_init_hook(self):
            TestDevice.server_init_hook_called = True

    with DeviceTestContext(TestDevice):
        assert TestDevice.server_init_hook_called


def test_asyncio_server_init_hook_called():
    class TestDevice(Device):
        green_mode = GreenMode.Asyncio
        has_been_called = False

        async def server_init_hook(self):
            await asyncio.sleep(0.01)
            TestDevice.has_been_called = True

    with DeviceTestContext(TestDevice):
        assert TestDevice.has_been_called


def test_server_init_hook_change_state(server_green_mode):
    class TestDevice(Device):
        green_mode = server_green_mode

        def server_init_hook(self):
            self.set_state(DevState.ON)

    with DeviceTestContext(TestDevice) as proxy:
        assert proxy.state() == DevState.ON


def test_asyncio_server_init_hook_change_state():
    class TestDevice(Device):
        green_mode = GreenMode.Asyncio

        async def server_init_hook(self):
            await asyncio.sleep(0.01)
            self.set_state(DevState.ON)

    with DeviceTestContext(TestDevice) as proxy:
        assert proxy.state() == DevState.ON


def test_server_init_hook_called_after_init():
    class TestDevice(Device):
        def init_device(self):
            self.set_state(DevState.INIT)

        def server_init_hook(self):
            self.set_state(DevState.ON)

    with DeviceTestContext(TestDevice) as proxy:
        assert proxy.state() == DevState.ON


def test_async_server_init_hook_called_after_init():
    class TestDevice(Device):
        green_mode = GreenMode.Asyncio

        async def init_device(self):
            await asyncio.sleep(0.01)
            self.set_state(DevState.INIT)

        async def server_init_hook(self):
            await asyncio.sleep(0.01)
            self.set_state(DevState.ON)

    with DeviceTestContext(TestDevice) as proxy:
        assert proxy.state() == DevState.ON


def test_server_init_hook_exception(server_green_mode):
    class TestDevice(Device):
        green_mode = server_green_mode

        def server_init_hook(self):
            self.set_state(DevState.ON)
            raise RuntimeError("Force exception for test")

    with DeviceTestContext(TestDevice) as proxy:
        assert proxy.state() == DevState.FAULT


def test_asyncio_server_init_hook_exception():
    class TestDevice(Device):
        green_mode = GreenMode.Asyncio

        async def server_init_hook(self):
            await asyncio.sleep(0.01)
            raise RuntimeError("Force exception for test")

    with DeviceTestContext(TestDevice) as proxy:
        assert proxy.state() == DevState.FAULT


def test_server_init_hook_with_low_level_api_called(server_green_mode):
    class ClassicAPISimpleDeviceImpl(LatestDeviceImpl):
        green_mode = server_green_mode
        has_been_called = False

        def server_init_hook(self):
            self.set_state(DevState.ON)
            ClassicAPISimpleDeviceImpl.has_been_called = True

    class ClassicAPISimpleDeviceClass(DeviceClass):
        pass

    with DeviceTestContext(ClassicAPISimpleDeviceImpl, ClassicAPISimpleDeviceClass):
        assert ClassicAPISimpleDeviceImpl.has_been_called


def test_server_init_hook_with_low_level_api_change_state(server_green_mode):
    class ClassicAPISimpleDeviceImpl(LatestDeviceImpl):
        green_mode = server_green_mode

        def server_init_hook(self):
            self.set_state(DevState.ON)

    class ClassicAPISimpleDeviceClass(DeviceClass):
        pass

    with DeviceTestContext(
        ClassicAPISimpleDeviceImpl, ClassicAPISimpleDeviceClass
    ) as proxy:
        assert proxy.state() == DevState.ON


def test_server_init_hook_with_low_level_api_called_after_init():
    class ClassicAPISimpleDeviceImpl(LatestDeviceImpl):
        def init_device(self):
            self.set_state(DevState.INIT)

        def server_init_hook(self):
            self.set_state(DevState.ON)

    class ClassicAPISimpleDeviceClass(DeviceClass):
        pass

    with DeviceTestContext(
        ClassicAPISimpleDeviceImpl, ClassicAPISimpleDeviceClass
    ) as proxy:
        assert proxy.state() == DevState.ON


def test_server_init_hook_with_low_level_api_exception(server_green_mode):
    class ClassicAPISimpleDeviceImpl(LatestDeviceImpl):
        green_mode = server_green_mode

        def server_init_hook(self):
            self.set_state(DevState.ON)
            raise RuntimeError("Force exception for test")

    class ClassicAPISimpleDeviceClass(DeviceClass):
        pass

    with DeviceTestContext(
        ClassicAPISimpleDeviceImpl, ClassicAPISimpleDeviceClass
    ) as proxy:
        assert proxy.state() == DevState.FAULT


def test_server_init_multiple_devices():
    event_list = []

    class DeviceOne(Device):
        def server_init_hook(self):
            event_list.append("DeviceOne")

    class DeviceTwo(Device):
        def server_init_hook(self):
            event_list.append("DeviceTwo")

    devices_info = (
        {"class": DeviceOne, "devices": [{"name": "test/device1/1"}]},
        {
            "class": DeviceTwo,
            "devices": [{"name": "test/device2/1"}, {"name": "test/device3/1"}],
        },
    )

    with MultiDeviceTestContext(devices_info):
        assert len(event_list) == 3
        assert "DeviceOne" in event_list
        assert "DeviceTwo" in event_list


def test_server_init_hook_subscribe_event_multiple_devices():
    pytest.xfail("This test is unreliable - to be fixed soon")

    event_queue = multiprocessing.Queue()

    class DeviceOne(Device):
        @attribute(dtype=int)
        def some_attribute(self):
            return 42

        def init_device(self):
            super().init_device()
            self.set_change_event("some_attribute", True, False)

        @command
        def push_event_cmd(self):
            self.push_change_event("some_attribute", 43)

    class DeviceTwo(Device):
        def event_handler(self, data):
            event_queue.put(data.attr_value.value)

        def server_init_hook(self):
            self.dev1_proxy = DeviceProxy("test/device1/1")
            self.dev1_proxy.subscribe_event(
                "some_attribute", EventType.CHANGE_EVENT, self.event_handler
            )

    devices_info = (
        {"class": DeviceOne, "devices": [{"name": "test/device1/1"}]},
        {
            "class": DeviceTwo,
            "devices": [{"name": "test/device2/1"}, {"name": "test/device3/1"}],
        },
    )

    with MultiDeviceTestContext(devices_info) as context:
        proxy = context.get_device("test/device1/1")

        # synchronous event
        assert 42 == event_queue.get(timeout=TIMEOUT)
        assert 42 == event_queue.get(timeout=TIMEOUT)
        assert event_queue.empty()

        # asynchronous event pushed from user code
        proxy.push_event_cmd()
        assert 43 == event_queue.get(timeout=TIMEOUT)
        assert 43 == event_queue.get(timeout=TIMEOUT)
        assert event_queue.empty()


def test_warning_not_coroutine_asyncio(server_green_mode):
    class TestDevice(Device):
        green_mode = server_green_mode

        def init_device(self):
            pass

    if server_green_mode == GreenMode.Asyncio:
        with pytest.warns(PyTangoUserWarning):
            with DeviceTestContext(TestDevice):
                pass
    else:
        # check no warnings
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            with DeviceTestContext(TestDevice):
                pass


def test_no_warning_coroutine_asyncio():
    class TestDevice(Device):
        green_mode = GreenMode.Asyncio

        async def init_device(self):
            pass

    # check no warnings
    with warnings.catch_warnings():
        warnings.simplefilter("error")
        with DeviceTestContext(TestDevice):
            pass
