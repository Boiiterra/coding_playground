#!/bin/bash

file=$1
output=${file%.kt*}

if [ -f ./kotlin/$file ]; then
    # echo "File $file exists and will be converted to $output.jar and executed"
    kotlinc ./kotlin/$file -include-runtime -d ./kotlin/out/$output.jar
    java -jar ./kotlin/out/$output.jar
else
    echo "File \"$file\" does not exist"
    echo "Or try to run this file in the scope of coding_playground directory"
fi