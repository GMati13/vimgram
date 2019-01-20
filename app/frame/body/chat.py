from urwid import Frame
from app.component.messages.message_input import message_input
from app.component.messages.messages import messages
import tg.action.dialog as tg
import const.tg as t

class Chat(Frame):
    def __init__(self):
        self.__chat = None
        self.__storage = {}
        super().__init__(body=messages, footer=message_input, focus_part='footer')

    def get_chat_id(self):
        return None if self.__chat is None else self.__chat[t.id]

    def load_history(self, chat):
        self.__chat = chat
        self.__total_count, self.__messages = tg.get_history(chat[t.id])
        messages.clear()
        messages.show_messages(self.__messages)

chat = Chat()
