# This program will read a file and look for integers using re.findall(),
# then convert extracted strings to integers and find sum

import re
fn = input('Enter a filename: ')
# open file in read mode
fhand = open(fn, 'r')
# instantiate list for numbers
numlist = list()
# if a line contains a number, append that number to list
for lin in fhand:
    num = re.findall('[0-9]+', lin)
    numlist = num + numlist
# convert each number from string to int
numbers = [int(i) for i in numlist]
# calculate total
total = sum(numbers)
print(total)
