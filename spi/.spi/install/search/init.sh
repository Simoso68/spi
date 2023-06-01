#!/bin/bash

if ($1 == "download") then
    bash /usr/bin/.spi/install/download/get.sh $2 $3
elif ($1 == "search")
    python3 /usr/bin/.spi/install/search/search.py $2 $3
fi