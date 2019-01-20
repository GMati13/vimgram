from app.component.dialogs.dialogs import dialogs
from app.frame.body.body import body
import const.error as error

commands = [ 'a', 'append', 'load', 'l', 'toggle-char', 'tgc', 'toggle-dialogs', 'tgd' ]

__alias = {
    'append': [ 'append', 'a' ],
    'dialog': [ 'dialog', 'd' ],
    'load'  : [ 'load',   'l' ],
    'toggle-chat': [ 'toggle-chat', 'tgc' ],
    'toggle-dialogs': [ 'toggle-dialogs', 'tgd' ]
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
    elif args[0] in __alias['load']:
        if len(args) != 2:
            return error.command_has_n_arguments.format(command=args[0], n=1)
        else:
            if args[1] in __alias['dialog']:
                dialogs.load_dialogs()
            else:
                return error.command_bad_argument.format(argument=args[1])
    elif args[0] in __alias['toggle-chat']:
        if line not in __alias['toggle-chat']:
            return error.command_has_no_arguments.format(command=args[0])
        else:
            dialogs.toggle_messages()
    elif args[0] in __alias['toggle-dialogs']:
        if line not in __alias['toggle-dialogs']:
            return error.command_has_no_arguments.format(command=args[0])
        else:
            body.toggle_dialogs()
