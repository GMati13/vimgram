import urwid
import vimgram.components.divider as divider

right_drawer = urwid.ListBox([])

right_drawer_styled = urwid.Columns([
    divider.vertical,
    right_drawer
])
