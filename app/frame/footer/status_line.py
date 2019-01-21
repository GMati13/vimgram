from ui.element.info_line import InfoLine
from app.mode.mode import mode
from urwid import Text
import app.formatter as f
import const.tg as t
import tg.action.users as tg

class StatusLine(InfoLine):
    def __init__(self):
        self.mode_status = (3, mode)
        self.name = Text('loading...')
        self.user = None
        super().__init__([
            self.mode_status,
            self.name
        ])

    def get_user_info(self):
        self.user = tg.get_me()
        self.name.set_text(f.get_name(self.user, is_chat=False))

    def get_user_id(self):
        if self.user is None:
            return None
        return self.user[t.id]

status_line = StatusLine()
