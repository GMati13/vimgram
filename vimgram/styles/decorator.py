
import urwid
import vimgram.styles.attr_map.composite as c

class Main(urwid.AttrMap):
    def __init__(self, widget):
        super().__init__(widget, c.main_label)

class Divider(urwid.AttrMap):
    def __init__(self, widget):
        super().__init__(widget, c.divider_label)

class StatusLine(urwid.AttrMap):
    def __init__(self, widget):
        super().__init__(widget, c.status_line_label)

class InfoLine(urwid.AttrMap):
    def __init__(self, widget):
        super().__init__(widget, c.info_line_label)

class DialogUsername(urwid.AttrMap):
    def __init__(self, widget):
        super().__init__(widget, c.dialog_username_label)

class DialogStatus(urwid.AttrMap):
    def __init__(self, widget):
        super().__init__(widget, c.dialog_status_label)

class DialogTime(urwid.AttrMap):
    def __init__(self, widget):
        super().__init__(widget, c.dialog_time_label)
