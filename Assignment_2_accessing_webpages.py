# For this assignment, we have to retrieve data from a specified webpage and supply some of the data we get back
# We need to access http://data.pr4e.org/intro-short.txt
# We will need to supply the header field values for:
# Last-modified, ETag, Content-Length, Cache-Control, Content-Type

import socket  # Import the socket library

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Define our socket (Address family, socket type)
mysock.connect(('data.pr4e.org', 80))  # Connect with our socket to a specified (domain, port number)
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()  # Here's the exact GET command we're sending
# I know the command in line 8 doesn't make total sense. Hang in there.
# The 'encode' command converts the Python command to a series of UTF-8 bytes that the transfer protocol can use
mysock.send(cmd)  # This tells Python to send the command

while True:  # This indefinite loop allows us to retrieve data as long as there's data to retrieve from the site
    data = mysock.recv(512)  # Pulls the data from the socket, stores in a new variable called data
    # The 512 number limits the length of the data received to 512 characters at a time - a "buffer"
    if len(data) < 1:  # If we stop receiving data (there's no more content in the web document/page)
        break  # Stop attempting to retrieve data
    print(data.decode())  # Decode and print each line of web data
mysock.close()  # Close the socket, as we have finished retrieving data. "End of transmission."
