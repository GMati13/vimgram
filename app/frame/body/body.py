from ui.widget.buffer import Buffer
from app.component.dialogs.dialogs import dialogs

class Body(Buffer):
    def __init__(self):
        super().__init__([dialogs])

body = Body()
