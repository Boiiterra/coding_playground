#!/bin/bash

if [ ! -d "./pascal/out/" ]; then
    echo "./pascal/out/ is created for storing output files.\n"
    mkdir ./pascal/out
fi

file=$1
output=${file%.pas*}

if [ -f ./pascal/$file ]; then
    # echo "File $file exists and will be converted to $output.jar and executed"
    fpc ./pascal/$file
    mv ./pascal/$output ./pascal/out/
    mv ./pascal/$output.o ./pascal/out/
    ./pascal/out/$output
else
    echo "File \"$file\" does not exist"
    echo "Or try to run this file in the scope of coding_playground directory"
fi
