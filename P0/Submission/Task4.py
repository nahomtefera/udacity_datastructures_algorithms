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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# APRROACH
    # Create dict of outbound calls and a list of possible telemarketers
    # Loop through all calls
        # Add outband call to list
    # Loop through calls again 
        # check if current caller is in the outband calls list
            # if it's not in the outbound list, add it to possible telemarketers list
    # Loop throug texts
        # check if current sender, and sendee are in the possible telemarketers list
            # if they are, remove them 


# CODE

outbandCalls = {}
possibleTeles = []

for call in calls :
    if call[1] not in outbandCalls :
        outbandCalls[call[1]] = True

for call in calls :
    if call[0] not in outbandCalls :
        possibleTeles.append(call[0])

for text in texts :
    if text[0] in possibleTeles :
        possibleTeles.remove(text[0])
    if text[1] in possibleTeles :
        possibleTeles.remove(text[1])

possibleTeles.sort() 

print("These numbers could be telemarketers: ")

for phoneNumber in possibleTeles :
    print(phoneNumber)

# COMPLEXY ANALYSIS
    # We are runnin the operations of 
        # assigning 2 variables => 2
        # Looping through a list => n
            # Searching on dict => 1
                # Assigning a value to a key => 1
        # Looping through a list => n
            # Searching on dict => 1
                # Assigning a value to a key => 1
        # Looping through a list => n
            # Searching on list => n
                # removing item from list => 1     
            # Searching on list => n
                # removing item from list => n
        # sort list => n log n
        # Print => 1
        # Looping through a list => n
            # Print => 1
    # Complexity is 2 + n + n + n(n + n(n)) + n log n + n => Big 0(n^3)