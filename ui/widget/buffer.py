import urwid

class Buffer(urwid.Columns):
    def __init__(self, columns=[], dividechars=0):
        super().__init__(columns, dividechars)

    def append_column(self, column, pos=0):
        if pos == 'end':
            self.contents.append((column, self.options()))
        else:
            self.contents.insert(pos, (column, self.options()))

    def remove_column(self, column):
        if type(column) is int:
            self.contents.pop(column)
        else:
            self.contents.remove(column)
