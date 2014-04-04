#!/bin/bash 

set -e

make
make ./ex17_rev2
./ex17_rev2 ex17_rev2.db c 512 100
