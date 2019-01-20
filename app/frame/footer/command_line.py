import urwid
from ui.element.input import Input

class CommandLine(Input):
    def __init__(self):
        super().__init__()

command_line = CommandLine()
