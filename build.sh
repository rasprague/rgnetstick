#!/bin/sh

# build netstick
# hard-coded for arm64 build
cd netstick
dockcross-linux-armm64 make clean
dockcross-linux-armm64 rm CMakeCahce.txt
cmake CMakeLists.txt
make
cd ..

# build rgnetstick
rm rgnetstick.pyxapp
pyxel package . rgnetstick.py
