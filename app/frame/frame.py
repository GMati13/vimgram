import urwid
from app.frame.body import body
from app.frame.footer import footer
from app.frame.header import header

frame = urwid.Frame(
    header=header,
    body=body,
    footer=footer,
    focus_part='footer'
)
