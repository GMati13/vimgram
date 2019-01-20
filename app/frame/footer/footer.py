from urwid import BoxAdapter, ListBox
from app.frame.footer.command_line import command_line
from app.frame.footer.status_line import status_line
from ui.decorator.decorator import Grey, Dark

class Footer(BoxAdapter):
    def __init__(srlf):
        super().__init__(ListBox([
            Dark(status_line),
            Grey(command_line)
        ]), height=2)

footer = Footer()
