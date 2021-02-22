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

phoneBook = set()
diffNums = 0

for call in calls :
    inBoundNumber = call[0]
    outBandNumber = call[1]

    if inBoundNumber not in phoneBook :
        phoneBook.add(inBoundNumber)
    if outBandNumber not in phoneBook :
        phoneBook.add(outBandNumber)

for text in texts :
    inBoundNumber = text[0]
    outBandNumber = text[1]

    if inBoundNumber not in phoneBook :
        phoneBook.add(inBoundNumber)
    if outBandNumber not in phoneBook :
        phoneBook.add(outBandNumber)

print("There are {} different telephone numbers in the records".format(len(phoneBook)))