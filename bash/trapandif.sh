#!/bin/bash

trap checkfunction INT

checkfunction() {
echo "Are you sure to cancel [yes/no]:"
read input

if [[ $input == 'yes' ]]; then
	echo "Exiting..."
	sleep 1
	echo "Program closed!!!"
	exit
else 
	echo "process will continue"
fi
}


for a in `seq 1 10`; do
echo "$a position in loop"
sleep 1
done
