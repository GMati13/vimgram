from app.frame.footer.command_line import command_line
from app.shortcut.normal import shortcut
from app.frame.frame import frame

def on_key_press(key):
    if key in shortcut:
        shortcut[key]()

def enter(previous_mode, next_mode):
    frame.set_focus('body')
    command_line.set_caption('')
