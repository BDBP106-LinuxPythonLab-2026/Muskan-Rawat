#!/bin/bash
awk '{printf $0=$0 ",\n", $1=$1 ",", $2=$2 ",", $3=$3 ","}' stud.txt
echo stud.txt > data2.csv
