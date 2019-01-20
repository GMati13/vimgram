from urwid import AttrMap
from app.theme.theme import target_theme as theme

class Black(AttrMap):
    def __init__(self, widget):
        super().__init__(widget, theme.secondary, theme.primary)

class BlackInverse(AttrMap):
    def __init__(self, widget):
        super().__init__(widget, theme.primary, theme.secondary)

class Grey(AttrMap):
    def __init__(self, widget):
        super().__init__(widget, theme.grey_secondary, theme.grey_primary)

class GreyInverse(AttrMap):
    def __init__(self, widget):
        super().__init__(widget, theme.grey_primary, theme.grey_secondary)

class DarkGrey(AttrMap):
    def __init__(self, widget):
        super().__init__(widget, theme.dark_grey_secondary, theme.dark_grey_primary)

class DarkGreyInverse(AttrMap):
    def __init__(self, widget):
        super().__init__(widget, theme.dark_grey_primary, theme.dark_grey_secondary)
