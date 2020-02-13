# Write a program to read through the mbox-short.txt and figure out the
# distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then
# splitting the string a second time using a colon.
# Example format: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts
# sorted by hour.

# open file (use mbox.txt)
fn = input('Enter a filename: ')
fhand = open(fn, 'r')
# create dictionary & list
di = dict()
time_stamps = list()
# populate dictionary with tuples (date, frequency)
for lin in fhand :
    # find 'From' keyword in each line in file
    if not lin.startswith('From'):
        continue
    # split the 'From' lines into strings
    lin = lin.split()
    #length of time_stamp is >4 and time is at index 5
    if len(lin) > 4:
        time_stamps.append(lin[5])
# split time_stamps by colon to dissect hours
for stamp in time_stamps:
    stamp = stamp.split(':')
    # populate dict (di) with hour entries and attribute frequency values
    # hour entries are at index 0 in stamp (stamp[0])
    di[stamp[0]] = di.get(stamp[0], 0) + 1

# use sorted() to sort keys in dict numerically by hours
for key in sorted(di.keys()):
    print(key, di[key])
