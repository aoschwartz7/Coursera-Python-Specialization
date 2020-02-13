# Write a program to read through mbox.txt and figure out who has sent
# the greatest number of mail messages.
# Look for 'From ' lines and take the second word of those
# lines as the person who sent the mail.
# Create a Python dictionary that maps the sender's mail address
# to a count of the number of times they appear in the file.
# After the dictionary is produced, the read through the
# dictionary using a maximum loop to find the most prolific committer.

# enter name of txt file (mbox.txt) and open in read mode
filename = input('Enter a file name: ')
fhand = open(filename, 'r')
# instantiate empty dictionary and list
di = dict()
lst = list()

# break each txt file line into words
for lin in fhand:
    lin = lin.split()
    # nest for loop to search for 'From' in line
    for word in lin:
        if not word.startswith('From'):
            continue
        # if contains 'From', append the word (sender) directly adjacent to it
        # to list (lst)
        if len(lin) > 4:
            lst.append(lin[1])
# for each sender entry in list, tally up the sum and add to dictionary
for email in lst:
    di[email] = di.get(email, 0) + 1

largest = -1
sender = None
# loop through dictionary items and keep track of sender with greatest tally
for k,v in di.items():
    if v > largest:
        largest = v
        sender = k
print(sender, largest)
