#!/bin/bash

filename='Que1.png'
read filename
echo "File_name: "

if [ -f "$filename" ]; then
	echo "file exists"
	exit 200
else
	echo " file does not exists"
	exit 201
fi
	


