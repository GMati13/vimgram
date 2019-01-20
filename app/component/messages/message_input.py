from ui.element.input import Input
from ui.widget.list import List
from ui.element.info_line import InfoLine
from app.mode.mode import mode
from ui.decorator.decorator import Grey, DarkGrey
from urwid import BoxAdapter

class MessageInput(BoxAdapter):
    def __init__(self):
        self.info_line = InfoLine()
        self.input = Input(multiline=True)
        super().__init__(List([
            Grey(self.info_line),
            DarkGrey(self.input)
        ]), 2)

    def on_focus(self):
        mode.toggle_mode('insert')

message_input = MessageInput()
