# from PyInquirer import prompt, print_json
# import json
# questions = [
#     {
#         'type': 'input',
#         'name': 'first_name',
#         'message': 'What\'s your first name',
#     }
# ]

# answers = prompt(questions)

# print_json(answers)  # use the answers as input for your app

# with open('data.json', 'w') as outfile:
#     json.dump(answers, outfile)
#------------------------------------------------
# countdown.py
# import time

# def countdown(num_mins):
#     num_of_secs = num_mins * 60
#     while num_of_secs:
#         m, s = divmod(num_of_secs, 60)
#         min_sec_format = f'{int(m)}:{int(s)}'
#         print(min_sec_format, end='\r')
#         time.sleep(1)
#         num_of_secs -= 1
        
#     print('Countdown finished.')

# countdown(0.1)
#------------------------------------------------
import time

while True:
    time.sleep(1)
    print('hello', end='\r')
    time.sleep(1)
    print('alo', end='\r')