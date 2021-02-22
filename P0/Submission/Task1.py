"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

phoneBook = {}
diffNums = 0

for call in calls :
    phoneNumber = call[0]

    if phoneNumber not in phoneBook :
        phoneBook[phoneNumber] = True
        diffNums += 1

print("There are " + str(diffNums) + " different telephone numbers in the records")
    
# COMPLEXY ANALYSIS
    # We are runnin the operations of 
        # assigning 2 variables => 2
        # Looping through a list => n
            # Creating a variable => 1
            # Searching through a dict => 1
                # Comparison => 1
                # Addition => 1
        # Print => 1
    # Complexity is 2 + n(1 + 1(2)) => Big O(n)