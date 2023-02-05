from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer
from timer import TimerWidget
from pomodoro import Pomodoro

class TimerApp(App):
    """A simple Textual app."""
    # CSS_PATH = "styles.css"
    def __init__(self):
        super().__init__()
        self.pomo = Pomodoro(50)
        self.timer = TimerWidget(self.pomo)

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode"), 
                ("r", "toggle_dark", "Refresh timer")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Container(self.timer)

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark
    
    def refresh_timer(self) -> None:
        """Refresh the timer."""
        self.compose()

if __name__ == "__main__":
    app = TimerApp()
    app.run()