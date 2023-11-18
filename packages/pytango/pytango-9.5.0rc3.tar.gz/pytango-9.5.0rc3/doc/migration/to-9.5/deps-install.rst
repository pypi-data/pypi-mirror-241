.. _to9.5_deps_install:

=============================
Dependencies and installation
=============================

Dependencies
============

PyTango v9.5.0 requires Python 3.9 or higher.

PyTango v9.5.0 moved from `cppTango`_ 9.4.x to at least 9.5.0.  It
will not run with earlier versions.  cppTango's dependencies have also changed,
most notably, omniORB 4.3.x is required, instead of 4.2.x.

In most cases, your existing PyTango devices and clients will continue to
work as before, however there are important changes.  In the other sections of
the migration guide, you can find the incompatibilities and the necessary migration steps.

Installation
============

Similar to the 9.4.x series, the binary wheels on `PyPI`_ and `Conda-forge`_ make installation very simple on many
platforms.  No need for compilation.  See :ref:`Getting started <getting-started>`.

If you are compiling from source, you may notice that the build system has changed completely.
We now use `scikit-build-core <https://scikit-build-core.readthedocs.io/>`_, and use `CMake <https://cmake.org>`_
for the compilation on all platforms.  See :ref:`building from source <build-from-source>`.
