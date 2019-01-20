from ui.widget.list import List
from app.component.dialogs.dialog import Dialog
import tg.action.dialog as tg

class Dialogs(List):
    def __init__(self):
        super().__init__()
        self.__maximized_messages = True
        self.on_toggle = lambda: None

    def render(self, size, focus=False):
        if not focus and len(self.body):
            self.body[self.focus_position].unmark_dialog()
        elif len(self.body):
            self.body[self.focus_position].mark_dialog()
        return super().render(size, focus)

    def append_dialog(self, dialog):
        self.append_child(Dialog(dialog, self.__maximized_messages), 'end')

    def remove_dialog(self, dialog):
        self.remove_child(Dialog(dialog))

    def load_dialogs(self):
        self.body.clear()
        self.__total_count, self.__dialogs = tg.get_gialogs()
        for dialog in self.__dialogs:
            self.append_dialog(dialog)

    def keypress(self, size, key):
        if len(self.body) < 1:
            return super().keypress(size, key)
        self.body[self.focus_position].unmark_dialog()
        return super().keypress(size, key)

    def minimize_messages(self):
        if not self.__maximized_messages:
            return
        for dialog in self.body:
            dialog.minimize_messages()
            self.__maximized_messages = False

    def maximize_messages(self):
        if self.__maximized_messages:
            return
        for dialog in self.body:
            dialog.maximize_messages()
            self.__maximized_messages = True

    def toggle_messages(self):
        self.on_toggle(not self.__maximized_messages)
        if self.__maximized_messages:
            self.minimize_messages()
        else:
            self.maximize_messages()

dialogs = Dialogs()
