#! /bin/bash
mkdir build
cd build
cmake ..
make

sudo ./exe/test
