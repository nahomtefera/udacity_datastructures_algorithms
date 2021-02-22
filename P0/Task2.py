from datetime import datetime

"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

# Approach
    # We want to get the customer that spend the most amount on a call cumulatively
    # We need to add each call to dictionary
        # For everytime that the phone number shows as outbandd or inbound
    # Create a longestCall variable
    # Loop through our dictionary of numbers and time spent on calls, 
        # get the highest one

timeSpentByNumber = {}

for call in calls :
    # Format time
    date = datetime.strptime(call[2], "%d-%m-%Y %H:%M:%S")
    month = date.month
    year = date.year
    hour = date.hour
    # Initialize call variables
    outbandNumber = call[0]
    inBoundNumber = call[1]
    timeOnCall = int(call[3])

    if year == 2016 and month == 9 :
        # Outband calls
        if outbandNumber in timeSpentByNumber :
            timeSpentByNumber[outbandNumber] += int(timeOnCall)
        elif outbandNumber not in timeSpentByNumber :
            timeSpentByNumber[outbandNumber] = int(timeOnCall)

        # Inboundd calls
        if inBoundNumber in timeSpentByNumber :
            timeSpentByNumber[inBoundNumber] += int(timeOnCall)
        elif inBoundNumber not in timeSpentByNumber :
            timeSpentByNumber[inBoundNumber] = int(timeOnCall)

longestCallTime = 0
number = None

for phoneNumber in timeSpentByNumber :
    time = timeSpentByNumber[phoneNumber]
    if time > longestCallTime :
        longestCallTime = time
        number = phoneNumber

print("{} spent the longest time, {} seconds, on the phone during September 2016".format(number, longestCallTime))