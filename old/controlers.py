from textual.containers import Container
from textual.widgets import Button

class ControlersContainer(Container):
    '''Container for Start, Pause and Stop buttons.'''
    def compose(self):
        yield Button('Start', id='start')
        yield Button('Pause', id='pause')
        yield Button('Stop', id='stop')