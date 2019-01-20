import urwid

class Window(urwid.BoxAdapter):
    def __init__(self, **args):
        super().__init__(args)
