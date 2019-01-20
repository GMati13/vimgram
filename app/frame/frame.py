import urwid
from app.frame.body.body import body
from app.frame.footer.footer import footer
from app.frame.header.header import header
from ui.decorator.decorator import Grey, Dark

class AppFrame(urwid.Frame):
    def __init__(self):
        super().__init__(
            header=Dark(header),
            body=Grey(body),
            footer=footer,
            focus_part='body'
        )

frame = AppFrame()
