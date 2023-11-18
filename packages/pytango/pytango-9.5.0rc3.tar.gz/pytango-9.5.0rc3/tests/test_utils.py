# -*- coding: utf-8 -*-

import pytest

from tango.utils import (
    _clear_test_context_tango_host_fqtrl,
    _get_device_fqtrl_if_necessary,
    _get_test_context_tango_host_fqtrl,
    _set_test_context_tango_host_fqtrl,
    InvalidTangoHostTrlError,
)


@pytest.fixture()
def restore_global():
    yield
    _clear_test_context_tango_host_fqtrl()


@pytest.mark.parametrize(
    "override_trl, input_trl, expected_trl",
    [
        (None, "a/b/c", "a/b/c"),
        (None, "a/b/c/d", "a/b/c/d"),
        (None, "tango://host:12/a/b/c", "tango://host:12/a/b/c"),
        (None, "tango://host:12/a/b/c#dbase=no", "tango://host:12/a/b/c#dbase=no"),
        (None, "no://trl/validation", "no://trl/validation"),
        ("tango://host:12", "a/b/c", "tango://host:12/a/b/c"),
        ("tango://host:12", "a/b/c/d", "tango://host:12/a/b/c/d"),
        ("tango://host:12", "tango://host:12/a/b/c", "tango://host:12/a/b/c"),
        ("tango://host:12#dbase=no", "a/b/c", "tango://host:12/a/b/c#dbase=no"),
        ("tango://host:12#dbase=yes", "a/b/c", "tango://host:12/a/b/c#dbase=yes"),
        ("tango://127.0.0.1:12", "a/b/c", "tango://127.0.0.1:12/a/b/c"),
    ],
)
def test_get_trl_with_test_fqtrl_success(
    override_trl, input_trl, expected_trl, restore_global
):
    _set_test_context_tango_host_fqtrl(override_trl)
    actual_trl = _get_device_fqtrl_if_necessary(input_trl)
    assert actual_trl == expected_trl


@pytest.mark.parametrize(
    "override_trl, input_trl",
    [
        ("host:123", "a/b/c"),  # missing scheme
        ("tango://", "a/b/c"),  # missing hostname and port
        ("tango://:123", "a/b/c"),  # missing hostname
        ("tango://host", "a/b/c"),  # missing port
        ("tango://host:0", "a/b/c"),  # zero-value port
        ("tango://host:12/path", "a/b/c"),  # non-empty path
        ("tango://host:123?query=1", "a/b/c"),  # non-empty query
        ("tango://host:123#dbase=invalid", "a/b/c"),  # invalid fragment
    ],
)
def test_get_trl_with_test_fdqn_failure(override_trl, input_trl, restore_global):
    _set_test_context_tango_host_fqtrl(override_trl)
    with pytest.raises(InvalidTangoHostTrlError):
        _ = _get_device_fqtrl_if_necessary(input_trl)


def test_global_state_default_set_and_clear(restore_global):
    default = _get_test_context_tango_host_fqtrl()
    _set_test_context_tango_host_fqtrl("tango://localhost:1234")
    after_set = _get_test_context_tango_host_fqtrl()
    _clear_test_context_tango_host_fqtrl()
    after_clear = _get_test_context_tango_host_fqtrl()

    assert default is None
    assert after_set == "tango://localhost:1234"
    assert after_clear is None


def test_clear_global_var_without_set_does_not_raise():
    _clear_test_context_tango_host_fqtrl()
