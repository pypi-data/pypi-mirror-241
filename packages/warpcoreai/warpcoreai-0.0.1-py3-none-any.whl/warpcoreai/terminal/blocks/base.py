from rich.console import Console
from rich.live import Live
from rich.panel import Panel


class Base:
    """
    A visual "block" on the terminal to display specific cases or scenarios.
    """

    def __init__(self, title="Case Block"):
        self.console = Console()
        self.live = Live(
            auto_refresh=False, console=self.console, vertical_overflow="visible"
        )
        self.title = title
        self.content = ""
        self.live.start()

    def update_from_message(self, message):
        """
        Update the displayed content based on the provided message.
        """
        self.content = message
        self.refresh()

    def end(self):
        """
        End the live display.
        """
        self.refresh()
        self.live.stop()

    def refresh(self):
        """
        Refresh the display with the current content.
        """
        panel = Panel(self.content, title=self.title)
        self.live.update(panel, refresh=True)

    def add_content(self, additional_content):
        """
        Add more content to the existing content.
        """
        self.content += f"\n{additional_content}"
        self.refresh()

    def set_title(self, new_title):
        """
        Set a new title for the block.
        """
        self.title = new_title
        self.refresh()
