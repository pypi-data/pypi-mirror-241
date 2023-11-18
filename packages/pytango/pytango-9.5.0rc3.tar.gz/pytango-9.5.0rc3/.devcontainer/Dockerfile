# Lets name this image: ubuntu2204-pytango-dev
FROM ubuntu:22.04

ARG OMNIORB_VERSION=4.3.0
ARG CPP_TANGO_VERSION=9.5.0
ARG TANGO_TEST_VERSION=3.8
ARG TANGO_IDL=5.1.2

RUN apt-get update -q \
    && apt-get install -y -q sudo \
       build-essential git pkg-config gdb libtool autoconf automake \
       ca-certificates curl vim \
       python3 python3-pip python3-venv \
       lcov doxygen clang-tidy-12 cppcheck \
       libboost-python-dev libzmq3-dev libcos4-dev libjpeg-turbo8-dev \
       unattended-upgrades
RUN unattended-upgrade \
    && apt-get purge unattended-upgrades -y \
    && update-alternatives --install /usr/bin/clang-tidy clang-tidy /usr/bin/clang-tidy-12 120
RUN pip3 install cmake

# Create a non-root account 'developer' without a password
# and give this account sudo access.
RUN useradd --create-home --shell /bin/bash developer \
    && adduser developer sudo \
    # Ensure sudo group users are not asked for a password when using 
    # sudo command (ammending sudoers file)
    && echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers \
    # Create a /src/ dir and hand it over to 'developer'
    && mkdir /src && chown -R developer:developer /src

USER developer
WORKDIR /src

# build and install omniorb
RUN curl -L -o omniORB.tar.bz2 https://sourceforge.net/projects/omniorb/files/omniORB/omniORB-${OMNIORB_VERSION}/omniORB-${OMNIORB_VERSION}.tar.bz2/download \
    && mkdir omniorb  \
    && tar xjf omniORB.tar.bz2 --directory=omniorb --strip-components=1 \
    && mkdir -p omniorb/build \
    && cd omniorb/build \
    && ../configure --prefix=/usr/local/ --with-openssl \
    && make -j$(nproc) all \
    && sudo make install

# build and install tangoidl
RUN git clone --depth 1 -b "$TANGO_IDL" https://gitlab.com/tango-controls/tango-idl.git \
    && mkdir -p tango-idl/build && cd tango-idl \
    && cmake -S . -B build -DCMAKE_INSTALL_PREFIX=/usr/local/ \
    && cmake --build build \
    && sudo cmake --install build

# build and install cppTango
WORKDIR /src
RUN git clone --depth 1 -b "$CPP_TANGO_VERSION" https://gitlab.com/tango-controls/cppTango.git \
    && cd cppTango \
    && mkdir -p build \
    && cmake -S . -B build -DBUILD_TESTING=OFF -DIDL_BASE=/usr/local \
    && cmake --build build \
    && sudo cmake --install build \
    && sudo ldconfig

# Build and install TangoTest
# This is required for running the pytest unittest suite
WORKDIR /src
RUN git clone --depth 1 -b "$TANGO_TEST_VERSION" https://gitlab.com/tango-controls/TangoTest.git  \
    && cd TangoTest \
    && mkdir -p build \
    && cmake -S . -B build \
    && cmake --build build \
    && sudo cmake --install build

WORKDIR /src
RUN python3 -m venv py3venv \
    && . py3venv/bin/activate \
    && pip install -U pip \
    # Build dependencies:
    && pip install scikit-build-core wheel build cmake numpy ninja \
    # Install dependencies is just numpy...
    # Test dependencies
    && pip install pytest pytest-forked gevent psutil

WORKDIR /src
ENV VIRTUAL_ENV=/src/py3venv
ENV PATH=${VIRTUAL_ENV}/bin:${PATH}
ENV CMAKE_GENERATOR="Ninja"
CMD exec /bin/bash

# To build:
# docker build . -t ubuntu2204-pytango-dev
# To run interactively:
# docker run -it --rm -v $(pwd):/src/pytango --name u22-pytango-dev ubuntu2204-pytango-dev
# To run a configure/build/other command...
# 
