from urwid import ListBox

class List(ListBox):
    def __init__(self, widgets=[]):
        self.__size = (1, 1)
        super().__init__(widgets)

    def render(self, size, focus):
        canvas = super().render(size, focus)
        self.__size = (canvas.rows(), canvas.cols())
        return canvas

    def keypress(self, size, key):
        if key in ['j', 'k', 'J','K']:
            if key is 'j':   self.select_next()
            elif key is 'k': self.select_prev()
            elif key is 'J': super().keypress(size, 'down')
            elif key is 'K': super().keypress(size, 'up')
            return
        return super().keypress(size, key)

    def select_next(self):
        if self.focus_position + 1 < len(self.body):
            self.set_focus(self.focus_position + 1)

    def select_prev(self):
        if self.focus_position > 0:
            self.set_focus(self.focus_position - 1)

    def scroll_end(self):
        super().keypress(self.__size, 'end')
        super().keypress(self.__size, 'end')

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

    def clear(self):
        self.body.clear()
