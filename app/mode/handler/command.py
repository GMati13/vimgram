from app.frame.frame import frame
from app.shortcut.command import shortcut
from app.frame.footer.command_line import command_line

def on_key_press(key):
    if key in shortcut:
        shortcut[key]()

command_line.on_key_press = on_key_press

def enter(previous_mode, next_mode):
    frame.set_focus('footer')
    command_line.set_caption(':')
    command_line.clear()
