import urwid
import vimgram.components.body as body
import vimgram.components.infobar as infobar
import vimgram.components.toolbar as toolbar
import vimgram.styles.decorator as decorator

frame = urwid.Frame(
    body=body.body_styled,
    header=infobar.infobar_styled,
    footer=toolbar.toolbar_styled,
    focus_part='footer'
)

frame_styled = decorator.Main(frame)
