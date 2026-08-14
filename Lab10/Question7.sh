#!/bin/bash
#Getting the username of the logged-in user
Logged_in_user="whoami" #no need of dollar sign and "whoami" does not need to be into brackets but in double inverted commas.
#Cheching if the user is logged in
if [ -n "$Logged_in_user" ];	#syntax error and brackets in both sides.
then
	echo "The logged-in user is: Logged_in_user" #syntax error
else
	echo "user is not logged in"
fi
