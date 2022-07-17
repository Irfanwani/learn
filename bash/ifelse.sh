#!/bin/bash

dir='../../lab'

#check if a directory exists or not
if [ -d $dir ]; then
echo "directory exists"

else 
echo "directory doesnot exist"
fi



#nested if else in bash
number=4

while [ $number -eq 4 ]; do
echo "please enter a number between 1 and 4"
read number
if [ $number == 1 ]; then 
echo "you entered 1. So got first word"
elif [ $number == 2 ]; then
echo "you entered 2 so you got second word"
else 
if [ $number == 3 ]; then
echo "you entered 3 so you got third word"
else
echo "you entered wrong number"
number=4
fi
fi
done


# arithmetic comparisons

# -lt >> less than (<)
# -gt >> greater than (>)
# -le >> less or equal to (<=)
# -ge >> greater or equal to (>=)
# -eq >> equal to (==)
# -ne >> not equal to (!=)

# taking an example where we compare two numbers
echo "please enter first number:"

read number1

echo "please enter second number:"
read number2

if [ $number1 -eq $number2 ]; then
echo "numbers are equal"
else
echo "numbers are different"
fi
