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

import time

def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format, end='/r')
        time.sleep(1)
        num_of_secs -= 1
        
    print('Countdown finished.')

inp = int(input('Input number of seconds to countdown: '))
countdown(inp)