import urwid
import asyncio
import vimgram.styles.palette as palette

def init(frame):
    global loop

    loop = urwid.MainLoop(
        frame,
        palette.palette,
        event_loop=urwid.AsyncioEventLoop(loop=asyncio.get_event_loop()),
        handle_mouse=False
    )

    loop.screen.set_terminal_properties(colors=256)

    return loop
