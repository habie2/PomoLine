import time
from PyInquirer import prompt

class Pomodoro():
    '''Pomodoro class'''
    def __init__(self, duration: int):
        self.duration = duration
        self.secs = duration * 60
        self.status = 'running'
    
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, status):
        if status not in ['running', 'paused', 'stopped']:
            raise ValueError('Status must be running, paused, or stopped.')
        self._status = status
    
    def countdown(self) -> any:
        '''Countdown timer for pomodoro
        Returns a string in the format of 'mm:ss'
        
        Parameters:
            None
        Returns:
            min_sec_format (str): String in the format of 'mm:ss
        '''
        
        while self.secs:
            if self.status == 'running':
                time.sleep(1)
                self.secs -= 1
            elif self.status == 'paused':
                pass
            elif self.status == 'stopped':
                self.secs = 0 
            else:
                raise ValueError('Status must be running, paused, or stopped.')

            return self.output_formatter()

    def output_formatter(self) -> str:
        '''Format the output of the countdown method
        Returns a string in the format of 'mm:ss'
        
        Parameters:
            None
        Returns:
            min_sec_format (str): String in the format of 'mm:ss
        '''
        mm_ss_format = divmod(self.secs, 60)
        output = f'🍅🍅 {mm_ss_format[0]}:{mm_ss_format[1]}'
        return output

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
