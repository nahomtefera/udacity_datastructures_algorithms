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

longestTime = 0
phoneNumber = None

for call in calls :
    if call[3] > longestTime :
        longestTime = int(call[3])
        phoneNumber = call[0]

print(phoneNumber + " spent the longest time, " + str(longestTime) + " seconds, on the phone during September 2016")

# COMPLEXY ANALYSIS
    # We are runnin the operations of 
        # assigning 2 variables => 2
        # Looping through a list => n
            # Comparison => 1
                # Assigning 2 variables
        # Print => 1
    # Complexity is 2 + n(1 + 1(2)) => Big O(n)