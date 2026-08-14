#!/bin/bash

echo "Input a number: "
read n

if [ "$n" -gt 100 ]; then # ["$n" -gt 100] should be in sqaure brackets only.
	echo "The number is greater than 100."
else
echo "The number is not greater than 100." 

fi
if [ "$n" -gt 100 ]; then # only sqaure brackets should be used and semi-colon after the sqaure brackets are closed and before then.
	echo "The number is greater than 100."
fi
