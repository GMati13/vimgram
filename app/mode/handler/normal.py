from app.frame.footer.command_line import command_line
from app.shortcut.normal import shortcut
from app.frame.frame import frame
from app.frame.body.body import body

def on_key_press(key):
    if key in shortcut:
        shortcut[key]()

def enter(previous_mode, next_mode):
    frame.set_focus('body')
    body.set_focus(0)
    command_line.set_caption('')
