# For this assignment, we need to write an JSON-parsing script that uses a live URL
# The program has to prompt for a URL, then read the JSON data from that URL using urllib
# Then we need to parse and extract the comment counts from the JSON data
# Finally, we need to compute the sum of the numbers in the file and provide the final sum

# Import necessary packages/libraries first
import urllib.request
import json

count_list = list()  # Create an empty list to append the numbers to
# Connect to the user-supplied URL and extract JSON data
url = input('Enter URL:')
raw_json = urllib.request.urlopen(url).read().decode()  # Multi-step - open URL, read text, decode into Unicode
json = json.loads(raw_json)  # Load the decoded JSON string into a JSON object
comments = json['comments']  # Create a new list of extracted tuples under the 'comments' header
for person in comments:  # For each person in the new list
    count_list.append(person['count'])  # Extract the value associated with the 'count' key and add it to the empty list
print(sum(count_list))  # Print the sum of the new list
