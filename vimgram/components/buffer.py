import urwid

class Buffer(urwid.Columns):
    def __init__(self, widget_list=[]):
        self.__size = (0, 0)
        self.__focus = False
        self.state = {}
        super().__init__(widget_list)

    def render(self, size, focus):
        if self.__focus and not focus:
            self.component_on_blur()
        canvas = super().render(size, focus)
        if self.__size != size:
            self.component_on_resize(new_size=size, old_size=self.__size)
        self.__size = size
        self.component_on_render(size=size, focus=focus)
        if not self.__focus and focus:
            self.component_on_focus()
        self.__focus = focus
        return canvas

    def component_on_blur(self):
        pass
    
    def component_on_focus(self):
        pass

    def component_on_resize(self, new_size, old_size):
        pass

    def component_on_render(self, size, focus):
        pass

    def set_state(self, state:dict):
        if self.component_will_update(old_state=self.state, new_state=state) is False:
            return
        old_state = self.state.copy()
        for key, value in state.items():
            self.__sate[key] = value
        self.component_did_update(new_state=self.state, old_state=old_state)

    def component_will_update(old_state:dict, new_state:dict):
        pass
    
    def component_did_update(new_state:dict, old_state:dict):
        pass

    def keypress(self, size, key):
        _key = self.component_on_key_press(key)
        if _key is False:
            return key
        if _key is not None:
            key = _key
        return super().keypress(size, key)
    
    def component_on_key_press(self, key:str):
        pass

    def insert_column(self, column, pos=-1):
        self.contents.insert(pos, (column, self.options()))

    def remove_column(self, pos):
        self.contents.remove(pos)
