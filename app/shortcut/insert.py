from app.mode.mode import mode
from app.frame.body.body import body

def esc():
    body.maximize_dialogs()
    mode.toggle_mode('normal')

shortcut = {
    'esc': esc
}
