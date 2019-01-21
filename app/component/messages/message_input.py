from ui.element.input import Input
from ui.element.info_line import InfoLine
from app.mode.mode import mode
from ui.decorator.decorator import Grey, DarkGrey
from urwid import BoxAdapter, ListBox

class _Input(Input):
    def __init__(self):
        super().__init__()

    def on_focus(self):
        mode.toggle_mode('insert')

class MessageInput(BoxAdapter):
    def __init__(self):
        self.info_line = InfoLine()
        self.input = _Input()
        super().__init__(ListBox([
            Grey(self.info_line),
            DarkGrey(self.input)
        ]), 2)

message_input = MessageInput()
