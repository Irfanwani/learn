#!/bin/bash

first=$1
second=$2

if [[ $first = $second ]]; then
	echo "they are same"
else 
	echo "they are different"
fi
