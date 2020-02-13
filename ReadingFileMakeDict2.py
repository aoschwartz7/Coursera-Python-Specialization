# Open the a file (romeo.txt) and read it line by line.
# For each line, split the line into a list of words using the split() method.
# Build a list of words. For each word on each line check to see if the word
# is already in the list and if not append it to the list.
# Sort and print the resulting words in alphabetical order.

# open txt file (romeo.txt) in read mode
filename = input('Enter the file name:')
fhand = open(filename, 'r')
# instantiate list
full_list = list()
# loop through file lines and split string into words
for line in fhand:
    line = line.split()
    # use nested loop to append words to list
    for item in line:
        if item not in full_list:
            full_list.append(item)
print(sorted(full_list))
