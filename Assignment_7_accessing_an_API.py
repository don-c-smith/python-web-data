# Let's use JSON to make a request of the course's 'snapshot' mapping API
# We will have to conform to their API's 'rules' about how to make requests of their service

# We start by importing the libraries/tools we'll need
import urllib.request  # To read the web data
import urllib.parse  # To translate normal, 'written out' text into URL format
import urllib.error  # Honestly I'm not sure what this one is for
import json  # To work with JSON

service_url = 'http://py4e-data.dr-chuck.net/json?'  # This is where we can access the data
user_location = input('Enter location: ')  # Ask the user to enter their location of interest
api_url = service_url + urllib.parse.urlencode({'address': user_location, 'key': 42})  # The key is '42'
# Now we begin the send-and-receive process
print('Retrieving', api_url)  # Show the user which page is being accessed
url_handle = urllib.request.urlopen(api_url)  # Create a correctly-formatted URL that can be passed to the API
data = url_handle.read().decode()  # Read and decode the returned JSON and store it in data
# If all is well, at this point we should have the long JSON string which we can load into an object in Python
# Now we need to use a try/except to check if the JSON has been fetched correctly
try:
    json = json.loads(data)  # Try to load the retrieved JSON string into a Python JSON object
except:  # If that doesn't work
    json = None  # Set the value to None-type
if not json or 'status' not in json or json['status'] != 'OK':  # Various checks for successful load status
    print('*** RETRIEVAL FAILURE, RETRY ***')  # Error message if line 23 spots a problem
    quit()  # Stop the program
print('JSON stored as:')  # If the process worked
print(json)  # Print out the dictionary
print('Place ID:', json['results'][0]['place_id'])  # Print out the place ID
# Index 0 is because there's only once place being referenced
