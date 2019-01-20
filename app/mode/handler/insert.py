from app.component.messages.message_input import message_input
from app.shortcut.insert import shortcut
from app.frame.body.body import body
from app.frame.body.chat import chat

def on_key_press(key):
    if key in shortcut:
        shortcut[key]()

message_input.input.on_key_press = on_key_press

def enter(previous_mode, next_mode):
    try:
        body.set_focus(1)
    except Exception:
        body.set_focus(0)
    chat.set_focus('footer')
