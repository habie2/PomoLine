import datetime
class Pomo():
    def __init__(self, mins: int):
        self.star_time = datetime.datetime.now()
        self.mins = mins
        self.status = 'running'
    def update(self):
        print(self.star_time)

pomo = Pomo(25)
pomo.update()