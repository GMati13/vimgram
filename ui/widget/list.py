import urwid

class List(urwid.ListBox):
    def __init__(self, **args):
        super().__init__(args)

    def append_child(self, child, pos=0):
        if pos == 'end':
            self.body.append(child)
        else:
            self.body.insert(pos, child)

    def remove_child(self, child):
        if type(child) is int:
            self.body.pop(child)
        else:
            self.body.remove(child)
