# Write a program that prompts for a file name (ie words.txt),
# then opens that file and reads through the file,
# and print the contents of the file in upper case.

file = input("Enter file name to open:")
try:
    fhand = open(file,'r')
except:
    print("Please enter correct file name")
    quit()
for line in fhand:
    print(line.upper().rstrip())
