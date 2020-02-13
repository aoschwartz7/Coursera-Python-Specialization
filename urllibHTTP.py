# This program is essentially the same as socketHTTP.py, only it uses urllib
# library to retrieve content from a web page, treating it much like a file.

import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        # add word to counts{} and increment
        counts[word] = counts.get(word, 0) + 1
print(counts)
