# This program will play the role of a web browser by
# making a connection to a web server to send a GET request
# to display HTTP Response headers and program content.

# Socket is used for communicating between two web programs
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# make connection to port 80 on server data.py4e.org
mysock.connect(('data.pr4e.org', 80))
# \r\n signifies an EOL (end of line) to separate header info from content
# use encode() to send data as bytes instead of strings
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
# receive data in 512-character chunks from the socket and print it
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    # decode() to convert data from bytes to strings
    print(data.decode())

mysock.close()
