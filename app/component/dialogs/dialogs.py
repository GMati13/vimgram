from ui.widget.list import List
from app.component.dialogs.dialog import Dialog

class Dialogs(List):
    def __init__(self):
        super().__init__()

    def append_dialog(self, dialog):
        self.append_child(Dialog(dialog), 'end')

    def remove_dialog(self, dialog):
        self.remove_child(Dialog(dialog))

dialogs = Dialogs()
