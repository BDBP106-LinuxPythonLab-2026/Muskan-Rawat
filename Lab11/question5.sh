#!/bin/bash

var1="Testing"
var2="testing"
if [ $var2 \> $var1 ]; then
	echo "$var1 is greater than $var2"
else
	echo "$var2 is greater than $var1" #basically by used \> together it compared both the strings whereas when we only used the > operator it used to redirect one file to another.
fi
