import time
import os
import sys
import keyboard
import asyncio

class Pomodoro():
    '''Pomodoro class'''
    def __init__(self, duration: int):
        '''Initialize the pomodoro timer

        Parameters:
            duration (int): Duration of the pomodoro in minutes
        '''
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
    
    async def countdown(self) -> any:
        '''Countdown timer for pomodoro
        Returns a string in the format of 'mm:ss'
        
        Parameters:
            None
        Returns:
            min_sec_format (str): String in the format of 'mm:ss'
        '''
        while self.secs:
            task = asyncio.create_task(self.keyboard_pause())
            if self.status == 'running':
                asyncio.sleep(1)
                self.secs -= 1
            elif self.status == 'paused':
                pass
            elif self.status == 'stopped':
                self.secs = 0 
            else:
                raise ValueError('Status must be running, paused, or stopped.')
        self.status = 'stopped'

    async def keyboard_pause(self):
        pressed = False
        while True and not pressed:
            if keyboard.key_is_pressed('p'):
                self.pause()
                pressed = True

    def start(self):
        '''Change status to running'''
        self.status = 'running'
    
    def pause(self):
        '''Change status to paused'''
        self.status = 'paused'
    
    def stop(self):
        '''Change status to stopped'''
        self.status = 'stopped'

    def output(self) -> str:
        '''Format the output of the countdown method
        Returns a string in the format of 'mm:ss'
        
        Parameters:
            None
        Returns:
            min_sec_format (str): String in the format of 'mm:ss'
        '''
        mm_ss_format = divmod(self.secs, 60)
        output = f'🍅 {int(mm_ss_format[0]):02}:{int(mm_ss_format[1]):02}' 
        return output, self.status
    

pomo = Pomodoro(50)
asyncio.run(pomo.countdown())
while True:
    print(pomo.output())