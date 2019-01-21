from urwid import AttrMap
from app.theme.theme import target_theme as theme

class Green(AttrMap):
    def __init__(self, widget):
        super().__init__(widget, theme.message_green, theme.dark_grey_primary)
