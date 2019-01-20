import urwid

class Input(urwid.Edit):
    def __init__(self):
        super().__init__()
        self.on_key_press = lambda: None
        self.on_enter = lambda: None

    def keypress(self, size, key):
        _key = self.on_key_press(key)
        if _key is None:
            super().keypress(size, key)
            if key is 'enter':
                self.on_enter(self.edit_text)
        elif _key is False:
            return
        else:
            super().keypress(size, _key)
            if _key is 'enter':
                self.on_enter(self.edit_text)
    
    def clear(self):
        self.edit_text = ''
