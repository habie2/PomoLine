import time
from PyInquirer import prompt

class Pomodoro():
    '''Pomodoro class'''
    def __init__(self, duration: int):
        self.duration = duration
        self.status = 'running'
    
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, status):
        if status not in ['running', 'paused', 'stopped']:
            raise ValueError('Status must be running, paused, or stopped.')
        self._status = status
    
    def countdown(self) -> None:
        
        num_of_secs = self.duration * 60
        while num_of_secs:
            if self.status == 'running':
                m, s = divmod(num_of_secs, 60)
                min_sec_format = f'🍅🍅 {int(m)}:{int(s)}'
                print(min_sec_format, end='\r')

                time.sleep(1)
                num_of_secs -= 1

            elif self.status == 'paused':
                pass
            elif self.status == 'stopped':
                num_of_secs = 0 
            else:
                raise ValueError('Status must be running, paused, or stopped.')

    def start(self):
        '''Change status to running'''
        self.status = 'running'
    
    def pause(self):
        '''Change status to paused'''
        self.status = 'paused'
    
    def stop(self):
        '''Change status to stopped'''
        self.status = 'stopped'
    
    def actions_menu(self):
        '''Actions menu for pomodoro, it includes:
        start, pause, and stop on a prompt menu.'''
        print('Actions:')
        actions_prompt = [{   
            'type': 'list', 
            'name': 'actions prompt',
            'message': 'Actions:',
            'choices': ['start' ,'pause', 'stop']
    }]  
        answer = prompt(actions_prompt)
        if answer['actions prompt'] == 'start':
            self.start()
        elif answer['actions prompt'] == 'pause':
            self.pause()
        elif answer['actions prompt'] == 'stop':
            self.stop()
        else:
            raise ValueError('Invalid action.')
