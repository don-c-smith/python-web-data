# This assignment requires writing a program will use urllib to read the HTML from a data file
# We then have to extract the href= values from the anchor tags
# Then we scan for a tag that is in a particular position relative to the first name in the list
# Then we need to follow that link and repeat the process a number of times and report the last name found
import urllib.request  # Import urllib functionality
import urllib.parse  # Import urllib functionality
import urllib.error  # Import urllib functionality
from bs4 import BeautifulSoup  # Import BeautifulSoup library
import ssl  # Import ssl tools

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

URL = input('Enter URL:')  # Here's the prompt for the URL
count = int(input('Enter loop count:'))  # Prompt for loop count
position = int(input('Enter link position:'))-1  # Prompt for position desired in link list
# The -1 is because the original name is first in the list
link_list = list()  # Create an empty list for the links
for iteration in range(count):  # For each iteration of the loop as defined by the entered value of count
    raw_html = urllib.request.urlopen(URL)  # Open each URL and store the raw HTML data in raw_html
    soup = BeautifulSoup(raw_html, 'html.parser')  # Parse and clean the raw HTML data and store it in soup
    anchor_tags = soup('a')  # Extract the list of anchor tags
    tag_list = list()  # Create an empty list for the tags
    for tag in anchor_tags:  # For each tag in the list of anchor tags
        link = tag.get('href', None)  # Extract the links as identified by the href tags
        tag_list.append(link)  # Append that link to the empty list of tags
    URL = tag_list[position]  # Set the URL of interest equal to the href tag at the position entered at the beginning
    link_list.append(URL)  # Add the URL of interest to the list of links
print(link_list[-1])  # Print the last element in the list of links
# Returns http://py4e-data.dr-chuck.net/known_by_Teejay.html
