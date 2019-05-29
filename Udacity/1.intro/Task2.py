"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

phone_pair = {}

for record in calls:
    duration = int(record[-1])
    
    for i in range(2):
        if record[i] not in phone_pair:
            phone_pair[record[i]] = duration
        else:
            phone_pair[record[i]] += duration

max_duration = 0
target_phone = ''
for phone, duration in phone_pair.items():
    if duration > max_duration:
        target_phone, max_duration = phone, duration

print("{} spent the longest time, {} seconds, on the phone during September 2016."
    .format(
    target_phone,
    max_duration
))


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

