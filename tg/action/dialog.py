from tg.client import client
import const.tg as tg

def get_gialogs():
    dialogs = client.get_dialogs()
    return (dialogs[tg.total_count], dialogs[tg.dialogs])
