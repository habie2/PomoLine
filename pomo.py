from datetime import datetime
import keyboard

class Pomo():
    def __init__(self, mins: int):
        self.star_time = datetime.now()
        self.mins = mins

    def run(self):
        intro = 'Welcome to pomo.\n[r] refresh'
        print(intro)
        while True:
            self.check_refresh()
            
    def check_refresh(self):
        if keyboard.is_pressed('r'):
            self.refresh()
    
    def refresh(self):
        '''Print time.now() - self.start_time'''
        time_left = 1
        print(datetime.now() - self.star_time)

pomo = Pomo(25)
pomo.run()