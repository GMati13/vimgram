import urwid
import asyncio
from app.frame.frame import frame
from app.theme.theme import target_theme as theme
from app.mode.handler.normal import on_key_press
import app.mode.handler.command

app = urwid.MainLoop(
    frame,
    theme.palette,
    event_loop=urwid.AsyncioEventLoop(loop=asyncio.get_event_loop()),
    unhandled_input=on_key_press,
    handle_mouse=False
)

app.screen.set_terminal_properties(colors=256)

app.run()
