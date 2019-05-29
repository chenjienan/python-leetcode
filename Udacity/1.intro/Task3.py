"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# part A
phone_ans = set()

for record in calls:
      if record[0].startswith('(080)'):
            if record[1].startswith('(0'):
                  i_close_bracket = record[1].index(')')
                  phone_ans.add(record[1][:i_close_bracket + 1])
            if record[1][0] in '789':
                  phone_ans.add(record[1][:4])
                  
phone_ans = list(phone_ans)
phone_ans.sort()
print('The numbers called by people in Bangalore have codes:')
for num in phone_ans:
      print(num)


# part B
calls_from_bgl = 0
calls_from_bgl_to_bgl = 0
for record in calls:
      if record[0].startswith('(080)'):
            calls_from_bgl += 1
            if record[1].startswith('(080)'):
                  calls_from_bgl_to_bgl += 1

percentage = round(calls_from_bgl_to_bgl / calls_from_bgl * 100, 2)
print('{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'
        .format(percentage))
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
