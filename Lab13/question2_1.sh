#!/bin/bash

awk '$2<=25 {print $1}' stud.txt
