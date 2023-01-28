import time
class Pomodoro():
    '''Pomodoro class'''
    def __init__(self, duration: int):
        self.__duration = duration
        self.status = 'paused'
    
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, status):
        if status not in ['running', 'paused', 'stopped']:
            raise ValueError('Status must be running, paused, or stopped.')
        self._status = status
    
    def countdown(self) -> None:
        
        num_of_secs = self.__duration * 60
        while num_of_secs and self.status == 'running':
            m, s = divmod(num_of_secs, 60)
            min_sec_format = f'🍅🍅 {int(m)}:{int(s)}'
            print(min_sec_format, end='\r')
            time.sleep(1)
            num_of_secs -= 1

        print('Pomodoro finished.')

    def start(self):
        '''Change status to running'''
        self.status = 'running'
    
    def pause(self):
        self.status = 'paused'
    
    def stop(self):
        self.status = 'stopped'

