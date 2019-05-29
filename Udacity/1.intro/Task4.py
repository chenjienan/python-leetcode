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

out_calls = set()
in_calls = set()
for record in calls:
    out_calls.add(record[0])
    in_calls.add(record[1])

out_texts = set()
in_texts = set()
for record in texts:
    out_texts.add(record[0])
    in_texts.add(record[1])

tel_market_calls = []
for num in out_calls:
    if num not in in_calls and \
       num not in out_texts and \
       num not in in_texts:

       tel_market_calls.append(num)

tel_market_calls.sort()
print('These numbers could be telemarketers: ')
for num in tel_market_calls:
    print(num)
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but 
1.never send texts,
2.never receive texts,
3.never receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

