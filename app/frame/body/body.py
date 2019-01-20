from ui.widget.buffer import Buffer
from urwid import Text, ListBox
from app.component.dialogs.dialogs import dialogs
from app.frame.body.chat import chat

class Body(Buffer):
    def __init__(self):
        self.__maximized_dialogs = True
        self.__minimized_messages = False
        dialogs.on_toggle = self.handle_toggle_messages
        self.__dialogs = dialogs
        super().__init__([self.__dialogs])

    def minimize_dialogs(self):
        if len(self.contents) and self.__maximized_dialogs:
            self.remove_column(0)
            self.__maximized_dialogs = False

    def maximize_dialogs(self):
        if not self.__maximized_dialogs:
            if self.__minimized_messages:
                self.contents.insert(0, (self.__dialogs, self.options('given', 35)))
            else:
                self.append_column(self.__dialogs)
            self.__maximized_dialogs = True

    def toggle_dialogs(self):
        if chat.get_chat_id() is None:
            return
        if self.__maximized_dialogs:
            self.minimize_dialogs()
        else:
            self.maximize_dialogs()

    def handle_toggle_messages(self, maximized):
        self.__minimized_messages = False;
        if not maximized:
            self.__minimized_messages = True;
            self.remove_column(0)
            self.contents.append((self.__dialogs, self.options('given', width_amount=35)))
            self.append_column(chat, 'end')
        else:
            self.remove_column(1)
            self.remove_column(0)
            self.append_column(self.__dialogs, 0)

body = Body()
