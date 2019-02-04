from . import command_line, status_line
import urwid

toolbar = urwid.ListBox([
    status_line.status_line_styled,
    command_line.command_line_styled
])

toolbar_styled = urwid.BoxAdapter(toolbar, 2)
