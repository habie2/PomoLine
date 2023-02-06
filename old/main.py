from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Header, Footer
from controlers import ControlersContainer
from title import TitleWidget
from timer import TimerWidget


class PomoApp(App):
    """A simple Textual app."""
    #CSS_PATH = "styles.css"

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Container(TitleWidget())
        yield Container(TimerWidget(), ControlersContainer())

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

if __name__ == "__main__":
    app = PomoApp()
    app.run()