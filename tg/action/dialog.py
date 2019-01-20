from tg.client import client
import const.tg as tg

def get_dialogs():
    dialogs = client.get_dialogs()
    return (dialogs[tg.total_count], dialogs[tg.dialogs])

def get_history(chat_id):
    history = client.get_history(chat_id)
    return (history[tg.total_count], history[tg.messages])
