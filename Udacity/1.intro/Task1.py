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

phone_ls = set()
for record in texts:
    phone_ls.add(record[0])
    phone_ls.add(record[1])

for record in calls:
    phone_ls.add(record[0])
    phone_ls.add(record[1])

print("There are {} different telephone numbers in the records.".format(len(phone_ls)))

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
