import os
from pyrogram import Client

vimgram_workdir = os.path.join(os.environ['HOME'], '.vimgram')
if not os.path.exists(vimgram_workdir):
    os.mkdir(vimgram_workdir)
vimgram_session = os.path.join(vimgram_workdir, 'vimgram.session')

client = Client(
    'vimgram',
    api_id='403859',
    api_hash='118250775a656486d2bb61f85746168e',
    workdir=vimgram_workdir,
    app_version='Vimgram 0.2.1'
)

print('Vimgram v0.2.1 by Roman Kovalyov <https://github.com/GMati13>')
client.start()
