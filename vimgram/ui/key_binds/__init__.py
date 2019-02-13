import threading
from . import normal

class Keys:
    def __init__(self):
        self.keys = []
        self.timeout = threading.Timer(0, lambda: 0)

    def append_key(self, key):
        self.keys.append(key)
        self.timeout.cancel()
        self.timeout = threading.Timer(2, self.process_keys)
        self.timeout.start()

    def process_keys(self):
        if self.keys == []:
            return
        print(self.keys)
        self.keys = []

keys = Keys()

def key_binds(key):
    global keys
    keys.append_key(key)
