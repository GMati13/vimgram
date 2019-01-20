import urwid
import asyncio
from app.frame import frame

app = urwid.MainLoop(
    frame,
    event_loop=urwid.AsyncioEventLoop(loop=asyncio.get_event_loop()),
    handle_mouse=False
)

app.screen.set_terminal_properties(colors=256)

app.run()
