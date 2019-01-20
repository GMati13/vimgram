from ui.widget.buffer import Buffer
from urwid import Text, Padding
import app.formatter as formatter
import const.tg as t
from ui.decorator.decorator import DarkGreyTertiary

class Message(Buffer):
    def __init__(self, message):
        text = ''
        if message['media']:
            text = t.media_file
        else:
            text = str(message['text'])
        date = formatter.formate_date(message['date'])
        widget_list = [
            (9, Padding(DarkGreyTertiary(Text(date)), left=1)),
            Padding(Text(text), right=1)
        ]
        super(Message, self).__init__(widget_list, dividechars=1)
