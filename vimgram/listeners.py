from vimgram.client import client
from vimgram.components.body.left_drawer import left_drawer
from vimgram.components.toolbar.command_line import command_line

@client.on_user_status()
def handle_user_status(c, status):
    pass

@client.on_message()
def handle_on_message(c, message):
    left_drawer.update_dialog_top_message(message)

@client.on_deleted_messages()
def handle_on_deleted_messages(c, messages):
    command_line.set_edit_text(str(messages))
