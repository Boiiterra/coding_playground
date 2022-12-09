# !/bin/bash

if [ -f ./cpp/$1.cpp ]; then
    cd ./cpp 
    echo "Starting $1.cpp script"
    echo
    g++ -o $1 $1.cpp
    ./$1
    rm ./$1
    echo
    echo "$1.cpp script stopped"
else
    echo "$1.cpp is not here"
fi