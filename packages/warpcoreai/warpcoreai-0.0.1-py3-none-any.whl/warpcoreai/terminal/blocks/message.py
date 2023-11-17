import re
from rich.box import MINIMAL
from rich.markdown import Markdown
from rich.panel import Panel
from base import Base


class Message(Base):
    def __init__(self):
        super().__init__()

        self.type = "message"
        self.message = ""
        self.has_run = False

    def update_message(self, new_message):
        """
        Update the message content and refresh the display.
        """
        self.message = new_message
        self.refresh()

    def refresh(self):
        # De-stylize any code blocks in markdown
        content = self._textify_markdown_code_blocks(self.message)

        markdown = Markdown(content.strip())
        panel = Panel(markdown, box=MINIMAL)
        self.live.update(panel)
        self.live.refresh()

    @staticmethod
    def _textify_markdown_code_blocks(text):
        """
        Convert markdown code blocks to 'text' to make them black and white.
        """
        lines = text.split("\n")
        inside_code_block = False

        for i, line in enumerate(lines):
            if re.match(r"^```(\w*)$", line.strip()):
                inside_code_block = not inside_code_block
                if inside_code_block:
                    lines[i] = "```text"

        return "\n".join(lines)
