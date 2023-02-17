import curses
import asyncio
from datetime import timedelta, datetime

class PomodoroTUI:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.timer = None
        self.time_left = timedelta(minutes=25)
        self.paused = False

    async def run_timer(self):
        while True:
            if not self.paused:
                self.time_left -= timedelta(seconds=1)
                self.display()
            await asyncio.sleep(1)

    def display(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "Pomodoro Timer")
        self.stdscr.addstr(1, 0, str(self.time_left))
        self.stdscr.addstr(2, 0, "Press 'p' to pause/resume")
        self.stdscr.addstr(3, 0, "Press 'q' to quit")
        self.stdscr.refresh()

    def start(self):
        curses.curs_set(0)
        self.display()
        self.timer = asyncio.ensure_future(self.run_timer())

        while True:
            key = self.stdscr.getkey()
            if key == 'p':
                self.paused = not self.paused
            elif key == 'q':
                self.timer.cancel()
                break

if __name__ == "__main__":
    curses.wrapper(lambda stdscr: PomodoroTUI(stdscr).start)