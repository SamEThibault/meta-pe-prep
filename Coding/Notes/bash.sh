#!/bin/bash

# Bash Review

# Variables (space-sensitive)
name="Sam"
echo "Hello there ${name}" # brackets good practice

# Grab invoke parameters this way:
param1=$1
echo "Parameter: ${param1}"

# $@ reads all inputs
# Ask for user input:
read -p "Enter whatever you want to print: " var
echo ${var}

# Arrays
array=("1" "2" "3" "4")
echo "First element of the array: ${array[0]}"

# can do last element like python: array[-1]
# return all elements in array: array[@]
# output array length: #array[@]

# print range of elements
echo ${array[@]:1:3} # prints 2 3 4

# You can do string slicing: ${string:start:length} (length is max number of chars to extract)
string="ABCDE"
echo ${string:0:2} # outputs AB

# True if file exists:
[[ -a ${file} ]]

# True if length of string is non-zero
[[ -n ${string} ]]

# Check if strings are equal
[[ ${string1} == ${string2} ]]

# Check if numbers are equal
[[ ${arg1} -eq ${arg2} ]]

# AND: &&, OR: ||

# Check if previous command was successful:
[[ $? -eq 0 ]]

# If statements:
if [[ some_test ]]
then
    #<commands>
    echo hello
else
    #<commands>
    echo hello
fi

# For loops:
for num in {1..10}
do
    echo ${num}
done

# or iterate through string
users="User1 User2 User3"

for user in ${users}
do
    echo ${user}
done

# or iterate through array
for element in ${array[@]}
do
    echo $element
done

# while loop:
counter=1
while [[ $counter -le 10 ]]
do
    echo $counter
    ((counter++))
done

# functions
function hello() {
    echo "Hello $1"
}

