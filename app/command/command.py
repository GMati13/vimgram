import shlex
import app.command.app.app as app
import app.command.test.test as test
from app.frame.footer.command_line import command_line
from app.mode.mode import mode
import const.error as error

def do_command(line):
    args = shlex.split(line)

    if args[0] in app.commands:
        result = app.do_command(line, args)
        if result:
            command_line.set_edit_text(result)
    elif args[0] in test.commands:
        result = test.do_command(line, args)
        if result:
            command_line.set_edit_text(result)
    else:
        command_line.set_edit_text(error.command_unknown.format(command=args[0]))
    mode.toggle_mode('normal')

command_line.on_enter = do_command
