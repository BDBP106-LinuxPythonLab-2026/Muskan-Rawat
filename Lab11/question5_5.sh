#!/bin/bash

var1="Testing"
var2="testing"
if [ $var1 \> $var2 ]; then
	echo "$var1 is greater than $var2"
else
	echo "$var2 is greater than $var1"
fi


echo "$var1;$var2" >> teststringfile
sort teststringfile
