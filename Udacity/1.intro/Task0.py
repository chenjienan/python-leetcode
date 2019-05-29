"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    first_text = texts[0]  

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    last_call = calls[-1]  


txt_in_num, txt_ans_num, txt_time = first_text[0], first_text[1], first_text[2]
call_in_num, call_ans_num, call_time, duration = last_call[0], last_call[1], last_call[2], last_call[3]

print('First record of texts, {} texts {} at time {}'
        .format(
            txt_in_num,
            txt_ans_num,
            txt_time
            )
        )

print('Last record of calls, {} calls {} at time {}, lasting {} seconds'
        .format(
            call_in_num,
            call_ans_num,
            call_time,
            duration
            )
        )


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

