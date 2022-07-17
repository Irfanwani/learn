#!/bin/bash


VAR="global variable"

function func {
local VAR="local variable"
echo $VAR
}

echo $VAR
func
echo $VAR


echo $1 $2 $3
args=("$@")

echo ${args[0]} ${args[1]} ${args[2]}
echo "number of args passed: $#"

#executing a shell command seperately
echo $(uname -o)


#this will print the command as it is without running it
echo uname -o

echo "Your name please: "
read name

echo "Hello $name"

# arrays
declare -a array

#Link file descriptor 10 with stdin
exec 10<&0

# stdin replaced with the file supplied as a first argument
exec < $1

echo $length

for ((i=0;i<3;i++)); do
read line
array[${i}]=$line

done

echo length: ${#array[@]}

echo ${array[@]}



#restore stdin from filedescriptor 10 and close filedescriptor 10
exec 0<&10<&-
