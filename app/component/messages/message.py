from ui.widget.buffer import Buffer
from urwid import Text, Padding
import app.formatter as formatter
import const.tg as t
from ui.decorator.decorator import DarkGreyTertiary
from ui.decorator.message import Green
from app.frame.footer.status_line import status_line

class Message(Buffer):
    def __init__(self, message):
        text = ''
        if message['media']:
            text = t.media_file
        else:
            text = str(message['text'])
        date = formatter.formate_date(message['date'])
        if message[t.from_user][t.id] == status_line.get_user_id():
            widget_list = [
                (9, Padding(DarkGreyTertiary(Text(date)), left=1)),
                Green(Padding(Text(text), right=1))
            ]
        else:
            widget_list = [
                (9, Padding(DarkGreyTertiary(Text(date)), left=1)),
                Padding(Text(text), right=1)
            ]
        super(Message, self).__init__(widget_list, dividechars=1)
