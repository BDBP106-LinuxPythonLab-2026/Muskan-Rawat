#!/bin/bash
filename='Que1.png'

echo 'File_name: '
read filename

if [ -f "$filename" ]; then
if [ -x "$filename" ]; then
	echo "file exists and is executable"
else 
	echo "file exists but is not executable"

	fi
else
	echo " file does not exist"
fi

