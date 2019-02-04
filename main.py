import vimgram.app.loop as loop
import vimgram.components.frame as frame
import vimgram.client as client
import vimgram.components.body.left_drawer as left_drawer

loop.init(frame.frame_styled)
left_drawer.left_drawer.load_dialogs()
import vimgram.listeners
loop.loop.run()
