from rich.box import MINIMAL
from rich.console import Group
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table

from base import Base


class Code(Base):
    """
    Code Blocks display code and outputs in different languages.
    You can also set the active line(s) and change the theme.
    """

    def __init__(self, theme="monokai"):
        super().__init__()

        self.type = "code"
        self.language = ""
        self.output = ""
        self.code = ""
        self.active_lines = set()
        self.theme = theme
        self.margin_top = True

    def set_active_lines(self, lines):
        """
        Set one or more active lines. Accepts a single line number or a list of line numbers.
        """
        if isinstance(lines, int):
            self.active_lines = {lines}
        elif isinstance(lines, (list, set, tuple)):
            self.active_lines = set(lines)

    def set_theme(self, theme):
        """
        Set the syntax highlighting theme.
        """
        self.theme = theme

    def refresh(self):
        code = self.code.strip()
        if not code:
            return

        code_table = Table(show_header=False, show_footer=False, box=None, padding=0, expand=True)
        code_table.add_column()

        code_lines = code.split("\n")
        for i, line in enumerate(code_lines, start=1):
            style = "black on white" if i in self.active_lines else None
            syntax = Syntax(line, self.language, theme=self.theme, line_numbers=False, word_wrap=True)
            code_table.add_row(syntax, style=style)

        code_panel = Panel(code_table, box=MINIMAL, style="on #272722")
        output_panel = Panel(self.output, box=MINIMAL, style="#FFFFFF on #3b3b37") if self.output else ""

        group_items = [code_panel, output_panel] if self.output else [code_panel]
        if self.margin_top:
            group_items = [""] + group_items
        group = Group(*group_items)

        self.live.update(group)
        self.live.refresh()
