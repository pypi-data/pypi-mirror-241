from rich import print as rich_print
from rich.markdown import Markdown
from rich.rule import Rule


def display_markdown_message(message):
    """
    Display a markdown message. Works with multiline strings and preserves formatting.
    Automatically beautifies single line blockquotes.

    Args:
        message (str): The markdown message to be displayed.
    """

    try:
        rich_print(Markdown(message))

        if message.count('\n') == 0 and message.startswith(">"):
            # Aesthetic spacing for single line blockquotes
            print("")
    except Exception as e:
        print(f"Error displaying markdown: {e}")

    # Print a rule for separation if the message contains a horizontal rule
    if '---' in message:
        rich_print(Rule(style="white"))
