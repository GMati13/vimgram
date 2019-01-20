import urwid

class Input(urwid.Edit):
    def __init__(self):
        super().__init__()
        self.on_key_press = lambda: None

    def keypress(self, size, key):
        _key = self.on_key_press(key)
        if _key is None:
            return super().keypress(size, key)
        if _key is False:
            return
        return super().keypress(size, _key)
    
    def clear(self):
        self.edit_text = ''
