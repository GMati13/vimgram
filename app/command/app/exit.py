import sys
from tg.client import client

def app_exit():
    client.stop()
    sys.exit()
