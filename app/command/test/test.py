from app.component.dialogs.dialogs import dialogs
import const.error as error
commands = [ 'a', 'append' ]

__alias = {
    'append': [ 'append', 'a' ],
    'dialog': [ 'dialog', 'd' ]
}

def do_command(line, args):
    if args[0] in __alias['append']:
        if len(args) != 3:
            return error.command_has_n_arguments.format(command=args[0], n=2)
        else:
            if args[1] in __alias['dialog']:
                dialogs.append_dialog(args[2])
            else:
                return error.command_bad_argument.format(argument=args[1])
