#!/bin/bash

string1=""
string2="hello my name is muskan"
if [ -n "$string1" ]; then # -n checks if the string is not empty (length is non-zero).
       echo "string is not empty"
else
	echo "string is empty"
fi
if [ -z "$string2" ]; then # -z chekcs if the string is empty (length is zero).
	echo "string is empty"
else
	echo "string is not empty"
fi
