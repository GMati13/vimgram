import urwid
from vimgram.components.buffer import Buffer
import vimgram.utils.normalize as normalize
import vimgram.styles.decorator as decorator
from vimgram.components.toolbar.command_line import command_line
from vimgram.client import client
import time
import threading

class Dialog(Buffer):
    def __init__(self, dialog):
        self.status = None
        self.chat_type = dialog['chat']['type']
        self.chat_id = dialog['chat']['id']
        self.username = urwid.Text(normalize.username(chat=dialog['chat']), wrap='clip')
        self.username_styled = decorator.DialogUsername(
            urwid.Padding(self.username, left=1)
        )
        self.top_message = dialog['top_message']
        if self.top_message:
            self.date_top_message = urwid.Text(normalize.date(self.top_message['date']), align='right')
        else:
            self.date_top_message = Text('', align='right')
        self.date_top_message_styled = decorator.DialogTime(urwid.Padding(self.date_top_message, right=1))
        self.date_top_message_width = 9
        
        super().__init__([
            self.username_styled,
            self.date_top_message_styled
        ])

    def update_top_message_date(self):
        if self.top_message:
            self.date_top_message.set_text(normalize.date(self.top_message['date']))
    
    def update_top_message(self, message):
        self.top_message = message
        self.update_top_message_date()
