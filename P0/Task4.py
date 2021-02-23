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
    # Create empty set of possible telemarketers
    # Loop through all calls
        # Add call[0] to list
    # Loop through calls again 
        # Discard call[1] if it's in the list (teles don receive calls)
    # Loop throug texts
        # remove text[0] and text[1] (teles don't do texts)


# CODE

possibleTeles = set()

for call in calls :
    possibleTeles.add(call[0])
for call in calls :
    possibleTeles.discard(call[1])
for text in texts :
    possibleTeles.discard(text[0])
    possibleTeles.discard(text[1])

# Sort result
sortedTeles = sorted(possibleTeles)

print("These numbers could be telemarketers: ")

for phoneNumber in sortedTeles :
    print(phoneNumber)