import threading
import re
from . import normal

class Keys:
    def __init__(self):
        self.keys = ''
        self.timeout = threading.Timer(0, lambda: 0)

    def on_update(self):
        pass

    def append_key(self, key):
        self.timeout.cancel()

        self.keys += self.parse_key(key)
        self.on_update()

        regex = '^{keys}.*'.format(keys=re.sub('\.', '\.', self.keys))
        number_of_matches = len(list(filter(
            lambda keys: re.search(regex, keys) is not None,
            key_binds().keys()
        )))
        
        if number_of_matches == 0:
            self.incorrect()
            return
        if number_of_matches == 1 and self.keys in key_binds():
            self.do()
            return

        self.timeout = threading.Timer(1, self.process_keys)
        self.timeout.start()

    def parse_key(self, key):
        if key == ' ':
            return '<space>'
        if key == '<0>':
            return '<ctrl-space>'
        if key == 'meta <0>':
            return '<meta-ctrl-space>'
        if len(key) > 1:
            return '<{key}>'.format(key=re.sub(' ', '-', key))
        return key

    def process_keys(self):
        if self.empty():
            return
        if self.keys in key_binds():
            self.do()
        else:
            self.incorrect()

    def do(self):
        print(key_binds()[self.keys])
        self.clear()

    def incorrect(self):
        print('inccorrect')
        self.clear()

    def empty(self):
        return self.keys == ''

    def clear(self):
        self.keys = '';
        self.on_update()

def key_binds():
    return normal.key_binds;

keys = Keys()
