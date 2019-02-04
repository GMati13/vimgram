import urwid
import vimgram.components.divider as divider
import threading
import vimgram.utils.normalize as normalize
from vimgram.utils.time import seconds_to_next_day
from vimgram.components.dialog import Dialog
from vimgram.client import client
import time

class LeftDrawer(urwid.ListBox):
    def __init__(self):
        super().__init__([])

    def load_dialogs(self):
        def _():
            dialogs = client.get_dialogs()
            for d in dialogs['dialogs']:
                dialog = Dialog(d)
                self.body.append(dialog)
                time.sleep(0.03)
            
        threading.Thread(target=_).start()
        self.update_top_message_date()

    def update_top_message_date(self):
        def _():
            for dialog in self.body:
                dialog.update_top_message_date()
            threading.Timer(seconds_to_next_day(), _)
        threading.Timer(seconds_to_next_day(), _)

    def update_dialog_top_message(self, message):
        for dialog in self.body:
            if  dialog.chat_id == message['chat']['id']:
                dialog.update_top_message(message)
                self.body.insert(0, self.body.pop(self.body.index(dialog)))
                break

left_drawer = LeftDrawer()

left_drawer_styled = urwid.Columns([
    left_drawer,
    divider.vertical
])
