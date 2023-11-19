from pathlib import Path
import sys


class InputHandler:

    name = 'input'
    text: str = ''

    def __init__(self, value):
        """Handlers take the value of the command line option"""
        if value:
            self.text = Path(value).read_text()
        elif not sys.stdin.isatty():
            self.text = sys.stdin.read()

    def __str__(self):
        return self.text
