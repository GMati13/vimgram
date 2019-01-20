import shlex
import app.command.app.app as app
from app.frame.footer.command_line import command_line
from app.mode.mode import mode
import const.error as error

def do_command(line):
    args = shlex.split(line)

    if args[0] in app.commands:
        result = app.do_command(line, args)
        if result:
            command_line.set_edit_text(result)
    else:
        command_line.set_edit_text(error.command_unknown.format(command=args[0]))
    mode.toggle_mode('normal')

command_line.on_enter = do_command
