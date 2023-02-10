import time
import os
import sys
import asyncio
import keyboard

class Pomodoro():
    '''Pomodoro class'''
    def __init__(self, duration: int):
        '''Initialize the pomodoro timer

        Parameters:
            duration (int): Duration of the pomodoro in minutes
        '''
        self.secs = duration * 60
        self.status = 'running'

    async  def keyboard_space(self):
        for i in range(10000000):
            print(i)
            await asyncio.sleep(0.01)
            if keyboard.is_pressed('space'):
                self.status = 'paused'
                return True
        # asyncio.sleep(10)
        # i = 0
        # while True:
        #     i += 1
        #     if keyboard.is_pressed('space'):
        #         self.status = 'paused'
        #         return True
        #     print(i)

    async def main(self):
        task = asyncio.create_task(self.keyboard_space())
        # task = asyncio.sleep(10)
        try:
            async with asyncio.timeout(5):
                await task
                print('task finished, without timeout')
        except TimeoutError:
            print("The long operation timed out, but we've handled it.")


    

pomo = Pomodoro(50)
asyncio.run(pomo.main())
#       pomo.test_keyboard_input()
# asyncio.run(pomo.test_keyboard_input())
# asyncio.run(pomo.countdown())