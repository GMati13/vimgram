from urwid import Columns
from urwid import Text

class Dialog(Columns):
    def __init__(self, dialog_data):
        super().__init__([Text(dialog_data)])
