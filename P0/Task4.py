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