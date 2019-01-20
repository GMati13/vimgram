from urwid import Text, Padding
from ui.widget.buffer import Buffer
import const.tg as tg
import app.formatter as f
from ui.decorator.decorator import Black, DarkGreyStatic, BlackTertiary
from app.theme.theme import target_theme as theme

class Dialog(Buffer):
    def __init__(self, dialog, maximized=True):
        self.__maximized_messages = maximized
        chat = dialog[tg.chat]
        self.__type = chat[tg.type]
        self.__title = Text(str(f.get_name(chat)), wrap='clip')
        self.__id = chat[tg.id]
        message = dialog[tg.top_message]
        self.__message = Text(str(self.__generate_message(message)), wrap='clip')
        self.__date = Text(str(f.formate_date(message[tg.date])), align='right', wrap='clip')
        self.__d_message = self.__decorate_message(self.__message)
        self.__d_date = self.__decorate_date(self.__date)
        
        widgets = [
            (35, Black(Buffer([
                (24, Padding(self.__title, left=1)),
                (10, Padding(self.__d_date, right=0))
            ]))),
            (self.__d_message)
        ]
        
        super().__init__(widgets if maximized else widgets[:1])

    
    def __generate_message(self, message):
        if message[tg.text] is None:
            return tg.media_file
        return message[tg.text].split('\n')[0]

    def mark_dialog(self):
        self.__d_message.set_attr_map({ None: theme.black_secondary })
        self.__d_date.set_attr_map({ None: theme.black_p_tertiary })
    
    def unmark_dialog(self):
        self.__d_message.set_attr_map({ None: theme.dark_grey_secondary })
        self.__d_date.set_attr_map({ None: theme.black_s_tertiary })

    def __decorate_date(self, date):
        return BlackTertiary(date)

    def __decorate_message(self, message):
        return DarkGreyStatic(Padding(message, right=1, left=1))
    
    def minimize_messages(self):
        if not self.__maximized_messages:
            return
        self.remove_column(1)
        self.__maximized_messages = not self.__maximized_messages

    def maximize_messages(self):
        if self.__maximized_messages:
            return
        self.append_column(self.__d_message, 'end')
        self.__maximized_messages = not self.__maximized_messages
