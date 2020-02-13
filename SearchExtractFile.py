# Write a program that prompts for a file name (mbox.txt),
# then opens that file and reads through the file looking for lines
# containing "X-DSPAM-Confidence:0.8475".
# Count these lines, extract the floating point values from each of the lines,
# compute the average of those values, and produce an output.

# use mbox.txt and open in read mode
filename = input('Enter a file name: ')
fhand = open(filename, 'r')
# instantiate variables
linecount = 0
total = 0
# loop through lines in file stripping white-space and locate 'X-DSPAM...'
for line in fhand:
    line = line.rstrip()
    pos = line.find('X-DSPAM-Confidence:')
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    # index into 'X-DSPAM' to extract number and convert to float then add to
    # total.
    total = total + float(line[pos + len('X-DSPAM-Confidence:'):])
    # keep count for calculating average
    linecount = linecount + 1
# calculate average and print it
print("Average spam confidence:", total/linecount)
