import urwid
import asyncio
from vimgram.ui.frame import frame
from vimgram.ui.theme import palette
from vimgram.ui.key_binds import keys

app = urwid.MainLoop(
    frame,
    palette,
    event_loop=urwid.AsyncioEventLoop(loop=asyncio.get_event_loop()),
    unhandled_input=keys.append_key,
    handle_mouse=False
)

app.screen.set_terminal_properties(colors=256)
