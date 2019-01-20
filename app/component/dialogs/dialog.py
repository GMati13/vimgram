from urwid import Text, Padding
from ui.widget.buffer import Buffer
import const.tg as tg
import app.formatter as f
from ui.decorator.decorator import Black, DarkGreyStatic
from app.theme.theme import target_theme as theme

class Dialog(Buffer):
    def __init__(self, dialog):
        chat = dialog[tg.chat]
        self.__type = chat[tg.type]
        self.__title = Text(str(self.__generate_title(chat)), wrap='clip')
        self.__id = chat[tg.id]
        message = dialog[tg.top_message]
        self.__message = DarkGreyStatic(Padding(Text(str(self.__generate_message(message)), wrap='clip'), right=1, left=1))
        self.__date = Text(str(f.formate_date(message[tg.date])), align='right', wrap='clip')
        super().__init__([
            (35, Black(Buffer([
                (24, Padding(self.__title, left=1)),
                (10, Padding(self.__date, right=1))
            ]))),
            (self.__message)
        ])

    def __generate_title(self, chat):
        if chat[tg.type] is tg.private:
            title = chat[tg.first_name]
            if chat[tg.last_name]:
                title += ' ' + chat[tg.last_name]
            return title
        return chat[tg.title]
    
    def __generate_message(self, message):
        if message[tg.text] is None:
            return tg.media_file
        return message[tg.text].replace('\n', ' ')

    def mark_dialog(self):
        self.__message.set_attr_map({ None: theme.black_secondary })
    
    def unmark_dialog(self):
        self.__message.set_attr_map({ None: theme.dark_grey_secondary })
