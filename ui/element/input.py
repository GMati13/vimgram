import urwid

class Input(urwid.Edit):
    def __init__(self, multiline=False):
        super().__init__(multiline=multiline)
        self.on_key_press = lambda key: None
        self.on_enter = lambda key: None

    def render(self, size, focus):
        if focus:
            self.on_focus()
        return super().render(size, focus)
    
    def on_focus(self):
        pass

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
