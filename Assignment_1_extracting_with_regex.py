# In this assignment, we are given a block of text from which we are to extract and then sum all numbers present
# We are to read in the text file, and use iteration and regex to extract the numbers
# Then, we convert the numbers from strings to integers, store them in a list, and sum them up
# The sample file should return 90 numbers with a sum of 445833
# The exercise file should return 65 values with a sum that ends in 828
import re  # Import the regular expressions library
file = open('C:/Users/doncs/Documents/exercise_text.txt')  # Remember to flip the slashes
numlist = list()  # Create an empty list
for line in file:  # For each line of text in the file
    if not re.search('[0-9]', line):  # If the line does not contain at least one number
        continue  # Skip that line
    else:  # Otherwise
        number_str = re.findall('[0-9]+', line)  # Extract all numbers and add to a list called number_str
    for number in number_str:  # For each number in that list of strings
        numlist.append(int(number))  # Append the integer of that number to the empty list numlist
print(sum(numlist))  # Print the sum of those numbers, 300828
# The sum matches exercise parameters - ends in ...828
