import urwid
from app.frame.body.body import body
from app.frame.footer.footer import footer
from app.frame.header.header import header
from ui.decorator.decorator import Grey, DarkGreyStatic

class AppFrame(urwid.Frame):
    def __init__(self):
        super().__init__(
            header=Grey(header),
            body=DarkGreyStatic(body),
            footer=footer,
            focus_part='body'
        )

frame = AppFrame()
