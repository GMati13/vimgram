from ui.widget.buffer import Buffer

class InfoLine(Buffer):
    def __init__(self, columns=[]):
        super().__init__(columns, 1)
