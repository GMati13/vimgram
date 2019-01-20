from urwid import Text
from app.config.startup import start_mode
import const.error as error
from importlib import import_module

class ModeException(Exception):
    def __init__(self, message):
        super().__init__(message)

class Mode(Text):
    __modes = {
        'normal',
        'command'
    }

    __current_mode = start_mode
    __previous_mode = None

    def __init__(self):
        super().__init__(self.label_format(self.__current_mode))

    def label_format(self, mode):
        return '[{m}]'.format(m=mode[:1].upper())
    
    def toggle_mode(self, mode):
        if mode not in self.__modes:
            raise ModeException(error.mode_can_not_be(mode=mode))
        self.__previous_mode = self.__current_mode
        self.on_toggle(self.__previous_mode, mode)
        self.set_text(self.label_format(mode))

    def get_mode(self):
        return self.__current_mode
    
    def get_previous_mode(self):
        return self.__previous_mode

    def on_toggle(self, previous_mode, next_mode):
        import_module('app.mode.handler.{m}'.format(m=next_mode)).enter(previous_mode, next_mode)

mode = Mode()
