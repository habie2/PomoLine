from PyInquirer import prompt
from pomodoro import Pomodoro

class Menu():
    def __init__(self) -> None:
        self.menu_name = 'Main Menu'

    def start_program(self):
        self.initial_prompt()
     
    def initial_prompt(self):
        menu_prompt = [{   
            'type': 'list', 
            'name': 'Initial prompt',
            'message': 'What do you want to do?',
            'choices': ['Start a pomodoro' ,'quit']
    }]
        answer = prompt(menu_prompt)
        if answer['Initial prompt'] == 'Start a pomodoro':
            self.start_pomodoro()
        elif answer['Initial prompt'] == 'quit':
            quit()
    
    def start_pomodoro(self):
        
        menu_prompt = [{   
            'type': 'list', 
            'name': 'pomodoro_time prompt',
            'message': 'Time?',
            'choices': ['50' ,'25']
    }]
        answer = prompt(menu_prompt)
        pomo = Pomodoro(int(answer['pomodoro_time prompt']))
        
    