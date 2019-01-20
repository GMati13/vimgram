from ui.widget.list import List
from app.component.messages.message import Message

class Messages(List):
    def __init__(self):
        super().__init__()

    def show_messages(self, messages):
        for message in messages:
            self.append_child(Message(message))
        self.scroll_end()

messages = Messages()
