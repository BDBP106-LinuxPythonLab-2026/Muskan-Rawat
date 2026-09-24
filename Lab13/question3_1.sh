#!/bin/bash

awk  '{print $1==">",d}' stud.txt
