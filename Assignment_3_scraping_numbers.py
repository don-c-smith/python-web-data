import urllib.request  # Import urllib functionalities
import urllib.error
import ssl  # Import tools to work with website security - mostly to avoid errors
from bs4 import BeautifulSoup  # Import BeautifulSoup library
import re  # Import regular expression library

# First, use the ssl library to ignore any SSL certificate errors triggered by websites
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Now we start the work.
URL = input('Enter URL:')
raw_html = urllib.request.urlopen(URL, context=ctx).read()  # The read() function returns all the page content at once
soup = BeautifulSoup(raw_html, 'html.parser')  # The 'cleaned' HTML is now stored in soup
final_sum = 0  # Start with a zero sum
span_tags = soup('span')  # Use BeautifulSoup to create a list of just the '<span>' tags
for tag in span_tags:  # For each of those individual tags in the list of '<span>' tags
    str_tag = str(tag)  # Create a 'common' string version of each tag
    num_extract = re.findall('[0-9]+', str_tag)  # Use regex to extract just the numbers from each tag
    for number in num_extract:  # For each number in the list of numbers
        number = int(number)  # Convert the extracted string of the number to an integer
    final_sum = final_sum + number  # Add each integer to the sum value - this is a 'running' sum
print(final_sum)  # Print the final value of the sum
