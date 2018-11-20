#! /bin/bash
mkdir build
cd build
cmake ..
make
cd ..
cp build/ipmodule.so ./ 
sudo python test.py
