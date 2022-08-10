# This file contains code notes and examples of the Python concepts taught in level 3 of 'Python for Everybody'
# Level 3, 'Accessing Web Data with Python,' is about how to access and use network-based data with Python
# These code examples show how to work with and execute the class' core concepts


# REGULAR EXPRESSIONS

# Regular expressions ('regex') are a bit of CompSci arcana that allow you to do sophisticated text searches
# Using them isn't an essential skill, but they can be very helpful and powerful
# They have their own set of characters because they're essentially a 'mini language' of their own
# They're not built into Python natively - you need to import the capability with the command 'import re'

# The re.search() function will return True or False based on whether the thing you searched for is present
# The re.findall() function will actually *extract* the matching strings

import re  # This imports the regular expressions library
line = 'My name is Don, I like woodworking, I am 35, was born on 1/6, and my favorite color is green.'
# Let's use re.search() to tell us if the characters 'wood' are present in that string
if re.search('wood', line):  # If 'wood' is present in the text
    print('True')  # Returns 'True'

# You can also use the special characters particular to regular expressions to do more advanced searches
# Let's say I wanted to know if the string had a birthdate in it expressed as #/#
if re.search('[0-9]/[0-9]', line):  # If the line contains a number from 0-9, followed by a slash, followed immediately by another number
    print('True')  # Returns True
if re.search('^[0-9]/[0-9]', line):  # If the line STARTS WITH a number from 0-9, followed by a slash, followed immediately by another number
    print('True')  # Does not print 'True' because the searched-for string is not at the start of the line

# Now let's try extracting text with re.findall()
# Let's extract all the numbers in the line, regardless of context
search = re.findall('[0-9]+', line)  # Extract all numbers - the '+' means 'find one or more of these'
print(search)  # Returns a LIST containing STRING copies of the numbers in the text
search2 = re.findall('[AEIOU]+', line)  # Search for any uppercase vowels in the line
print(search2)  # Returns a list containing the single 'I' of 'I am 35'

# Something to be aware of is that when using the * or + characters to search for multiple characters, the search is 'greedy' by default
# That means that it will return the longest possible string, searching BOTH directions, that satisfies your parameters
# So, if we were searching for strings with a colon, and had this text:
line2 = 'From: Don Smith - re: Setting a meeting'
# But we just wanted to return the part that started in F and ended in a colon - if we typed:
search3 = re.findall('F.+:', line2)  # Find a capital F, then any number of any characters, then a colon
print(search3)  # The 'greedy' setting meant we didn't get what we wanted, which was 'From:'
# Instead, we get ['From: Don Smith - re:']
# You can 'turn off' greedy mode by using a '?' character BEFORE the character of interest
# This tells the function to stop looking/expanding when it hits the FIRST instance of the character of interest
search4 = re.findall('F.+?:', line2)
print(search4)  # And NOW we just get 'From:', as desired
# Both of these modes are useful

# By fine-tuning your parameters, you can do very useful things efficiently
# Consider the task of extracting ONLY a usable email address from a long, nasty email text dump
text = 'From: don.cs.smith@gmail.com Sat July 2 2022 5:23:47 PM'
# If we ONLY wanted a usable email address from that line of text, we can say:
email = re.findall('\S+@\S+', text)  # See the breakdown below.
# Find a non-whitespace character \S
# Followed by any number of other characters +
# Followed by an '@' sign @
# Followed by another non-whitespace character \S
# Followed by any number of characters
print(email)  # Returns a list containing the string 'don.cs.smith@gmail.com'
# Only the email address prints because no other substrings have an '@ sign and none of them match the search parameters

# You can use parentheses to further specify what you want extracted. For example:
# Let's say we wanted to search only within lines that STARTED with 'From:' but we still only wanted to EXTRACT the email address
email2 = re.findall('^From: (\S+@\S+)', text)  # Search for text that starts with From-colon-space
# But the parentheses mean 'but only extract the text that starts here and ends here, as defined in my expression
print(email2)  # This returns a list containing the string 'don.cs.smith@gmail.com'
# Regex are one of those things that you don't use often, but they are *awfully* handy at times


# SOCKETS AND 'SEND REQUESTS'

# Let's try a very simple 'send request' via http for some data on the course website
# We're going to try to retrieve that bit of Romeo and Juliet along with its markup information
# At this stage, many of these things won't make sense - we have to start by taking things 'on faith'

import socket  # Import the socket library

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Define our socket (Address family, socket type)
mysock.connect(('data.pr4e.org', 80))  # Connect with our socket to a specified (domain, port number)
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()  # Here's the exact GET command we're sending
# I know the command in line 81 doesn't make total sense - hang in there
# The 'encode' command converts the Python command to a series of UTF-8 bytes that the transfer protocol can use
mysock.send(cmd)  # This tells Python to send the command

while True:  # This indefinite loop allows us to retrieve data as long as there's data to retrieve from the site
    data = mysock.recv(512)  # Pulls the data from the socket, stores in a new variable called data
    # The 512 number limits the length of the data received to 512 characters at a time - a "buffer"
    if len(data) < 1:  # If we stop receiving data (there's no more content in the web document/page)
        break  # Stop attempting to retrieve data
    print(data.decode())  # Decode and print each line of web data
mysock.close()  # Close the socket, as we have finished retrieving data. "End of transmission."
# Now you see the webpage and markup info and the actual page content
# This is basically how a request-response cycle of code in Python works
# MUCH more efficient in Python than in nearly all other languages

# Using urllib
# Because http requests are so common, there's a package designed to simplify the necessary coding processes
# The package is called urllib, and it saves a lot of time and is more comprehensible
# In many ways, it kind of mimics the open() function structure we're used to
# We're essentially "opening" a file from a remote location rather than our disk drive
# urllib also makes web pages 'look like' files, which is helpful
# Let's use urllib to open that same passage of Shakespeare from the course site
import urllib.request  # Import urllib functions
import urllib.parse  # Import urllib functions
import urllib.error  # Import urllib functions

file = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')  # Set the file 'handle' equal to the data at this URL
for line in file:  # For each line in the data
    print(line.decode().strip())  # Decode the data, strip the whitespace, and print each line
# The output has the Shakespeare text but NO HEADERS
# The urllib functions store and "remember" the headers - you can ask for them if you want
# However, we usually don't want/don't care about the headers
# You can also pull HTML from webpages, not just static text


# PARSING HTML WITH THE 'BEAUTIFULSOUP' LIBRARY

# The beautiful soup library makes it easier to parse HTML data when scraping websites
# This makes it more likely that you'll get usable data from websites
# Let's give it a try
import urllib.request  # Import urllib functionalities
import urllib.parse
import urllib.error
import ssl  # Import tools to work with website security - mostly to avoid errors
from bs4 import BeautifulSoup  # Import BeautifulSoup library

# First, use the ssl library to ignore any SSL certificate errors triggered by websites
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Now we start the work
URL = input('Enter URL:')
html = urllib.request.urlopen(URL, context=ctx).read()  # The read() function returns all the page content at once
soup = BeautifulSoup(html, 'html.parser')  # The 'cleaned' HTML is now stored in soup
# Fetching just the 'anchor tags'
tags = soup('a')  # Fetch just the anchor tags ('a') from the cleaned HTML (soup) and store them in tags
for tag in tags:  # For each individual anchor tag in the list of tags
    print(tag.get('href', None))  # Print the links as defined by their being paired with HTML 'href' tags


# PARSING XML WITH THE 'ELEMENTTREE' LIBRARY

# We need to be able to convert XML into an object-based format we can 'work on' with Python
# There's a helpful library called ElementTree (usually imported as ET) that we like to use
# ElementTree puts the XML data into a tree structure that we can access using Python
# Let's start by importing ElementTree
import xml.etree.ElementTree as ET

# Now let's provide some very basic XML. Note the triple-quote string which allows us to use multiple lines
# This is relevant because in XML, line breaks are a meaningful part of the information
# We'll store the XML text in a variable called data
data = '''<person>
    <name>Don</name>
    <phone type="intl">
        +1 267 664 4368
    </phone>
    <email hide="yes"/>
</person>'''
# Remember the whitespace doesn't matter to the computer, it just makes the XML more readable for us humans
# The overarching node is 'person'
# There's a child node called 'name' which contains the text value 'Don'
# There's another child node called 'phone' with datatype 'intl' and a value of +1 267 664 4368
# There's another child node with an ATTRIBUTE, which is the email hiding status, which is set to 'yes'
# Those data are stored within 'person'

# Now we'll convert that XML into a Python-usable tree using ElementTree
tree = ET.fromstring(data)  # Create a tree called 'tree' from the string variable 'data', using ElementTree
print(tree.find('name').text)  # Print the text contained in the child node called 'name' in the tree called 'tree'
# Returns 'Don'
print(tree.find('phone').attrib)  # Print the type header and the type value of the child node 'phone'
# Returns {'type' : 'intl'} - Note that it's stored as a key-value pair
print(tree.find('email').get('hide'))  # Get the 'status' of the 'hide' setting on the child node 'email'
# Returns 'yes'

# However, XML is very rarely that simple. Usually you'll have multiple sub-trees under child nodes
# For example, under the child node 'users,' you could have multiple data fields for each user
# To work with those tree structures, you need to iterate on them, which means using lists and 'for'
# Let's create some more realistic XML
new_data = '''<info>
    <users>
        <user x="1">
            <id>484997</id>
            <name>Don</name>
        </user>
        <user x="2">
            <id>196329</id>
            <name>Sherry</name>
        </user>
    </users>
</info>'''
# This XML has a child node called users which contains two separate sub-trees - one for each user.
# As such, you can't just call 'user' because that's not sufficiently iterative or specific
# So, you still you use ET, but now you use a for loop to get data for each user separately
info = ET.fromstring(new_data)  # Parse the XML and create the tree
user_list = info.findall('users/user')  # Find the values for each node within the users->user path (there are 2 users)
# Now we have a list with the user data:
print(len(user_list))  # Printing the length of this list gives us the user count, which is 2
# Now we iterate on the list to extract the data
for user in user_list:  # For each user in the user list
    print('Name:', user.find('name').text)  # Return the text value stored under 'name'
    print('ID number:', user.find('id').text)  # Return the text value stored under 'id'
    print('Data attribute:', user.get("x"))  # Return the value associated with the data attribute 'x'
# Returns name, ID number, attribute for each user, one user at a time
# This is a common sort of task when working with XML in Python
# Obviously, this can get much, much more complicated


# JSON FUNDAMENTALS

# JSON is a simpler, less rigorous serialization language that is becoming increasingly common
# Despite its simplicity and lack of explicative "power," it maps very well onto Python and is easy to work with
# Lots of people like JSON because it's easier to comprehend, particularly as a Python programmer
# Python 'reads in' JSON as nested lists and dictionaries, which are familiar and easy to work with
# Let's work with a couple of simple examples of JSON

# First we need to import the JSON library into Python
import json

# Now, let's create some simple JSON data
JSON_data = '''{
    "name" : "Don",
    "phone" : {
        "type" : "US",
        "number" : "267 664 4368"
    },
    "email" : {
        "hide" : "yes"
    }
}'''
# Lots of things to note here. ^^^
# First, note the creation of nested dictionaries with what are functionally key-value pairs
# Note also the 'stacking' or curly brackets to create nested sub-dictionaries
# As with XML, the whitespace is just so we understand the nesting more readily

# Now, let's work with these JSON data a bit
data = json.loads(JSON_data)  # The loads.variable function is 'load string'
print(data['name'])  # Note that we can interact with the JSON data now just as we would with a normal dictionary
print(data['phone']['number'])  # Asking for the 'number' value of the 'phone' sub-dictionary - returns 267 664 4368
print(data)  # Print the whole thing and you see a normal-looking dictionary
# This familiarity and ease-of-use is one of the main reasons Python people like JSON so much

# Commonly, you'll have a JSON structure with multiple 'members' with common fields
# AS in previous examples, we'll build some JSON with common fields for two users
# In cases like this, JSON is basically a LIST of DICTIONARIES
new_JSON = '''[
    { "id" : "001",
        "birthdate" : "01/06/1987",
        "name" : "Don"
    } ,
    {"id" : "002",
        "birthdate" : "09/25/1986",
        "name" : "Sherry"
    }
]'''
# Now we have a list of dictionaries. Two users with common data fields.
# As before, we can work with it like we'd work with a list or a dictionary
data2 = json.loads(new_JSON)
print(len(data2))  # Printing the length of the list gives you the user count: 2
print(data2[0])  # This prints all the data for the first user in the list (index is the first list element)
print(data2[0]['name'])  # This prints the value for name for the first user (element) in the list
# You can also use a for loop to iterate through the users
for person in data2:  # For each person in the list
    print('Name:', person['name'])  # Print their name
    print('Birthdate:', person['birthdate'])  # And their birthdate

# Writing a JSON API Request
# Let's use JSON to make a request of Google's locational mapping API
# We will have to conform to the Google Maps API's 'rules' about how to make requests of their service

# We start by importing the libraries/tools we'll need
import urllib.request  # To read the web data
import urllib.parse  # To translate normal, 'written out' text into URL format
import urllib.error  # Honestly I'm not sure what this one is for
import json  # To work with JSON

service_url = 'http://maps.googleapis/com/maps/api/geocode/json?'  # This is the main 'access' URL for the service
# Whatever we want to look for will be appended to that URL after the question mark

# Now we start the send-and-retrieve process, which will live within an indefinite 'while' loop
while True:
    user_location = input('Enter location: ')  # Ask the user to enter their location of interest
    if len(user_location) < 1:  # If they don't input anything and just hit 'enter'
        break  # Stop the loop and abandon the process

    api_url = service_url + urllib.parse.urlencode(
        {'location': user_location})  # This concatenates the service URL with the URL-encoded text the user entered

    # Now we begin the send-and-receive process
    print('Retrieving', api_url)
    url_handle = urllib.request.urlopen(api_url)
    data = url_handle.read().decode()
    # If all is well, at this point we should have the long JSON string which we can load into an object in Python

    # Now we need to use a try/except to check if the JSON has been fetched correctly
    try:
        json = json.loads(data)  # Try to load the retrieved JSON string into a Python JSON object
    except:  # If that doesn't work
        json = None  # Set the value to None-type

    if not json or 'status' not in json or json['status'] != 'OK':  # Various checks for successful load status
        print('*** RETRIEVAL FAILURE, RETRY ***')  # Error message if line 34 spots a problem
        continue  # If error occurs, return to the start of the loop

    print('JSON stored as:')  # If the process worked
    print(json.dumps(json, indent=4))  # Print the entire JSON object ('dumps' = dump string) in 'Python pretty' style

    latitude = json['results'][0]['geometry']['location']['lat']  # Access the latitude value in the JSON object
    longitude = json['results'][0]['geometry']['location']['lng']  # Access the longitude value
    print('Latitude:', latitude, 'Longitude:', longitude)  # Print those two values for the user's input
    clean_location = json['results'][0]['formatted address']  # Fetch the formatted full name of the user's input
    print(clean_location)  # Print the formatted full name of the user's input
