from textual.widgets import Static
from pomodoro import Pomodoro

class TimerWidget(Static):
    '''A container for the PomoApp.'''
    def __init__(self, pomodoro: Pomodoro):
        super().__init__()
        self.pomo = pomodoro
    def render(self):
        return self.pomo.output_formatter()
    def update(self):
        return self.pomo.output_formatter()

ex = TimerWidget(Pomodoro(50))
while True:
    print(ex.render())
