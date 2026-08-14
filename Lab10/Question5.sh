#!/bin/bash
echo "Enter score: "
read score

if [ "$score" -ge 90 ]; then
	echo "A"
elif [ "$score" -ge 80 ]; then
	echo "B"
elif [ "$score" -ge 70 ]; then
	echo "C"
else 
	echo "FAIL"
fi
