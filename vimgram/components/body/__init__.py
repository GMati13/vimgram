from . import history, left_drawer, right_drawer
import urwid
from vimgram.components.buffer import Buffer

class Body(Buffer):
    def __init__(self):
        self.right_drawer_width = 35
        self.left_drawer_width = 35
        self.left_drawer = (self.left_drawer_width, left_drawer.left_drawer_styled)
        self.right_drawer = (self.right_drawer_width, right_drawer.right_drawer_styled)

        super().__init__([
            self.left_drawer,
            history.history_styled,
            self.right_drawer
        ])

    def component_on_render(self, size, focus):
        cols, rows = size
        if cols < 140:
            try:
                self.remove_column(self.get_right_drawer())
            except ValueError:
                pass
            if cols < 75:
                try:
                    self.remove_column(self.get_left_drawer())
                except ValueError:
                    pass

    def get_right_drawer(self):
        return (right_drawer.right_drawer_styled, (
            'given',
            self.right_drawer_width,
            False
        ))

    def get_left_drawer(self):
        return (left_drawer.left_drawer_styled, (
            'given',
            self.left_drawer_width,
            False
        ))

body = Body()

body_styled = body
