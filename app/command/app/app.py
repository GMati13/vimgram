from app.command.app.exit import app_exit
import const.error as error

commands = [ 'quit', 'q' ]

__alias = {
    'quit': [ 'quit', 'q' ]
}

def do_command(line, args):
    if args[0] in __alias['quit']:
        if line not in __alias['quit']:
            return error.command_has_no_arguments.format(command=args[0])
        else:
            app_exit()
