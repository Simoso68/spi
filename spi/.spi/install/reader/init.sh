#!/bin/bash

if ($1 == "instructions") then
    python3 /usr/bin/.spi/install/reader/instructions.py "$2"

elif ($1 == "manifest") then
    python3 /usr/bin/.spi/install/reader/manifest.py "$2"
    
fi