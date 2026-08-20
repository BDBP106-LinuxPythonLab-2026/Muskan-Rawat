#!/bin/bash

mkdir file1
echo "hello my name is muskan, i am 21 years old." > file1.txt
echo "" > file2.txt
if [ -f file2.txt ]; then # -f checks if a file is a regular file.
	echo "a regular file"
else
	echo "not a regular file"
fi
if [ -e file1.txt ]; then # -e checks if a file exist.
	echo "file exists"
else
	echo "file does not exist"
fi
if [ -s file1.txt ]; then # -s checks if a file not empty.
	echo "file is not empty"
else
	echo "file is empty"
fi
