#!/bin/bash

awk ' $3=="Physics" {print $1}' stud.txt

