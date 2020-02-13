# this program will take a text file (romeo.txt), create a dictionary of
# each word/string, tally up the count per word,
# and report that tally and the max counted word.

# open romeo.txt
fn = input('Enter a filename: ')
fh = open(fn)
# instantiate empty dictionary
di = dict()

# break each txt file line into words
for lin in fh :
    lin = lin.rstrip()
    wds = lin.split()
    # use nested loop to enter each word into dictionary and add count to it
    for wd in wds :
        di[wd] = di.get(wd, 0) + 1

largest = -1
theword = None
# loop through dictionay items to find largest word count
for k,v in di.items() :
    if v > largest :
        largest = v
        theword = wd
print('Done', theword, v)
print(di)
