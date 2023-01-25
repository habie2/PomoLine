import time
class Pomodoro():
    '''Pomodoro class'''
    def __init__(self, duration):
        self.duration = duration
        self.start_time = time.time()
        self.end_time = self.start_time + self.duration

    def start(self):
        print('Starting pomodoro')
        self.time.sleep(self.duration)
        print('Pomodoro finished')
        return True
    
    def pause(self):
        pass
    
    def stop(self):
        pass