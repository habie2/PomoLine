import time
import os
import sys

class Pomodoro():
    '''Pomodoro class'''
    def __init__(self, duration: int):
        self.duration = duration
        self.secs = duration * 60
        self.status = 'running'
        self.__MISS_MINUTES = 1 # Adds a 'hack' in order to make time fly
        # It is actually the time.sleep on the counter

    @property
    def duration(self):
        return self._duration
    @duration.setter
    def duration(self, duration):
        if duration < 0:
            raise ValueError('Duration cannot be negative.')
        if type(duration) != int:
            raise TypeError('Duration must be an integer.')
        self._duration = duration
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
            min_sec_format (str): String in the format of 'mm:ss'
        '''
        
        while self.secs:
            if self.status == 'running':
                time.sleep(self.__MISS_MINUTES)
                self.secs -= 1
            elif self.status == 'paused':
                pass
            elif self.status == 'stopped':
                self.secs = 0 
            else:
                raise ValueError('Status must be running, paused, or stopped.')

            return self.output_formatter()
        self.status = 'stopped'
        return 'Countdown finished.'

    def output_formatter(self) -> str:
        '''Format the output of the countdown method
        Returns a string in the format of 'mm:ss'
        
        Parameters:
            None
        Returns:
            min_sec_format (str): String in the format of 'mm:ss'
        '''
        mm_ss_format = divmod(self.secs, 60)
        output = f'🍅🍅🍅 {int(mm_ss_format[0]):02}:{int(mm_ss_format[1]):02}' 
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
    
    def draw(self) -> None:
        '''Draw the pomodoro timer'''
        while self.status != 'stopped':
            
            print('Actual pomodoro:')
            print(self.countdown())
            

            # print(self.countdown()) # For debbuging purposes only
        
