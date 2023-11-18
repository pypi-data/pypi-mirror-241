"""Provides PyTango as a module for backward compatibility."""


# start delvewheel patch
def _delvewheel_patch_1_5_1():
    import ctypes
    import os
    import platform
    import sys
    libs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'pytango.libs'))
    is_conda_cpython = platform.python_implementation() == 'CPython' and (hasattr(ctypes.pythonapi, 'Anaconda_GetVersion') or 'packaged by conda-forge' in sys.version)
    if sys.version_info[:2] >= (3, 8) and not is_conda_cpython or sys.version_info[:2] >= (3, 10):
        if os.path.isdir(libs_dir):
            os.add_dll_directory(libs_dir)
    else:
        load_order_filepath = os.path.join(libs_dir, '.load-order-pytango-9.5.0rc3')
        if os.path.isfile(load_order_filepath):
            with open(os.path.join(libs_dir, '.load-order-pytango-9.5.0rc3')) as file:
                load_order = file.read().split()
            for lib in load_order:
                lib_path = os.path.join(os.path.join(libs_dir, lib))
                if os.path.isfile(lib_path) and not ctypes.windll.kernel32.LoadLibraryExW(ctypes.c_wchar_p(lib_path), None, 0x00000008):
                    raise OSError('Error loading {}; {}'.format(lib, ctypes.FormatError()))


_delvewheel_patch_1_5_1()
del _delvewheel_patch_1_5_1
# end delvewheel patch

# Imports
import sys
import tango
import pkgutil


def alias_package(package, alias, extra_modules={}):
    """Alias a python package properly.

    It ensures that modules are not duplicated by trying
    to import and alias all the submodules recursively.
    """
    path = package.__path__
    alias_prefix = alias + "."
    prefix = package.__name__ + "."
    # Alias all importable modules recursively
    for _, name, _ in pkgutil.walk_packages(path, prefix):
        # Skip databaseds backends
        if name.startswith("tango.databaseds.db_access."):
            continue
        try:
            if name not in sys.modules:
                __import__(name)
        except ImportError:
            continue
        alias_name = name.replace(prefix, alias_prefix)
        sys.modules[alias_name] = sys.modules[name]
    # Alias extra modules
    for key, value in extra_modules.items():
        name = prefix + value
        if name not in sys.modules:
            __import__(name)
        if not hasattr(package, key):
            setattr(package, key, sys.modules[name])
        sys.modules[alias_prefix + key] = sys.modules[name]
    # Alias root module
    sys.modules[alias] = sys.modules[package.__name__]


# Do not flood pytango users console with warnings yet
# warnings.warn('PyTango module is deprecated, import tango instead.')

# Alias tango package
alias_package(
    package=tango,
    alias=__name__,
    extra_modules={"_PyTango": "_tango", "constants": "constants"},
)