# Author: Sudeep Pillai (Sep 14, 2014)
project (ipmodule)
cmake_minimum_required (VERSION 2.6.0)

# Include package config, boost-python
find_package(PkgConfig REQUIRED)
include(cmake/boost-python.cmake)


# Include python (use -D flags instead)
if (NOT PYTHON_INCLUDE_DIRS OR NOT PYTHON_LIBRARIES)
    SET(PYTHON_INCLUDE_DIRS "/usr/include/python2.7")
    SET(PYTHON_LIBRARIES "/usr/lib/x86_64-linux-gnu/libpython2.7.so")
endif()

file(GLOB SrcCpp ${PROJECT_SOURCE_DIR}/src/*.cpp)

# Build test library
include_directories(${CMAKE_CURRENT_SOURCE_DIR})
boost_python_module(ipmodule ${SrcCpp})
target_link_libraries(ipmodule boost_system boost_python)
