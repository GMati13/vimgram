import urwid

class List(urwid.ListBox):
    def __init__(self, **args):
        super().__init__(args)
