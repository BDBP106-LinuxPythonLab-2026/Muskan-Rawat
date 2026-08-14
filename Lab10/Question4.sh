#!/bin/bash

echo "Enter a number: "
read number
if [ "$number" -gt 0 ]; then
	echo "posiitve"
elif [ "$number" -lt 0 ]; then
	echo "negative"
else 
	echo "zero"
fi
