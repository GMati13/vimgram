import urwid
from app.frame.footer.command_line import command_line
from app.frame.footer.status_line import status_line

class Footer(urwid.BoxAdapter):
    def __init__(srlf):
        super().__init__(urwid.ListBox([]), height=0)

footer = Footer()
