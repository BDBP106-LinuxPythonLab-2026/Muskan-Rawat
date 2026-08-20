#!/bin/bash

val1="Jayashree"
val2="Nagesh"
if [ $val1 \> $val2 ]; then
	echo "$val1 is greater than $val2"
else
	echo "$val1 is lesser than $val2" #basically by using \ before > operator which is ususally used to redirect one file to another one due to \> this operator it compared the strings whichis greater.
fi

