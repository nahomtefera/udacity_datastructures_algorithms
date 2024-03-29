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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# PART A
  # Loop through the phone numbers and get all the outbound calls from phones that start with (080)
  # Separate outbound calls by fixed lines, mobile numbers and telemarketers

# PART B
  # Count number of outbound calls that start with (080)

# PART 1 CODE
outBoundFixedLines = []
outBoundMobiles = []
outBoundTeles = []

for call in calls :
  if call[0][0:5] == '(080)' :
    if call[1][0:2] == "(0" :
      indexEndPrefix = call[1].find(")")
      outBoundFixedLines.append(call[1][1:indexEndPrefix])
    elif " " in call[1] and (call[1][0] == 7 or 8 or 9):
      outBoundMobiles.append(call[1][0:4])
    elif call[1][0:3] == "140" :
      outBoundTeles.append(call[1])  

# SORT ALL OUTBOUND CALLS
outBandCalls = outBoundFixedLines + outBoundMobiles + outBoundTeles
numOfCalls = len(outBandCalls)
sortedCalls = sorted(set(outBandCalls))


# PART B CODE
outbandBnglr = 0

for call in outBandCalls :
  if call[0:3] == '080' :
      outbandBnglr += 1

# PART A PRINT
print("The numbers called by people in Bangalore have codes: ")
for call in sortedCalls :
  print(call)

# PART B PRINT
percCallsBnglr = (100 * outbandBnglr) / float(numOfCalls)
print(str(round(percCallsBnglr, 2)) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")