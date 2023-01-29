from pomodoro import Pomodoro
from menu import Menu
import time

# main_menu = Menu()
# main_menu.start_program()

testing_pomo = Pomodoro(1) # testing pomodoro

while True:
    print(testing_pomo.countdown(), end='\r')

