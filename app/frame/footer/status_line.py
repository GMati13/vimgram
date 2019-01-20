from ui.element.info_line import InfoLine
from app.mode.mode import mode
from urwid import Text

class StatusLine(InfoLine):
    def __init__(self):
        self.mode_status = (3, mode)
        self.username = Text('loading...')
        super().__init__([
            self.mode_status,
            self.username
        ])

status_line = StatusLine()
