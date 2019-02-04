import urwid
from vimgram.components.buffer import Buffer
import vimgram.styles.decorator as decorator

status_line = Buffer()

status_line_styled = decorator.StatusLine(status_line)
