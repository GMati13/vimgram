from app.mode.mode import mode

shortcut = {
    ':': lambda: mode.toggle_mode('command'),
    'enter': lambda: mode.toggle_mode('insert'),
    'i': lambda: mode.toggle_mode('insert')
}
