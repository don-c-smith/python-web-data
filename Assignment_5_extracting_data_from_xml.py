# For this assignment, we need to write an XML-parsing script that uses a live URL
# The program has to prompt for a URL, then read the XML data from that URL using urllib
# Then we need to parse and extract the comment counts from the XML data
# Finally, we need to compute the sum of the numbers in the file and provide the final sum
import urllib.request
import urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

URL = input('Enter URL:')  # First, prompt for the URL
XML = urllib.request.urlopen(URL, context=ctx).read()  # Read the contents of the page, which are XML
print('Fetched ' + str(len(XML)) + ' characters.')  # Print number of characters in the full XML
tree = ET.fromstring(XML)  # Convert the XML into a tree using ET
# Note that you CAN use fromstring() even though the datatype of XML is 'bytes'. This was not explained to us.
count_list = tree.findall('.//count')  # Pull all the values occurring after the text 'count' and put them in a list
print('Total values: ' + str(len(count_list)))  # Print the total number of values to sum
total = 0  # Create a total, starting at zero
for count in count_list:  # For each count in the list of counts
    total = total + int(count.text)  # Add the integer of each text value of each count to the running sum
print('Final sum is ' + str(total))  # Print the final sum
