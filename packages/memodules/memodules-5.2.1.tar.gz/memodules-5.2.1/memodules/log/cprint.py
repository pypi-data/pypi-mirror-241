def cprint(*args, color: str, undo_when_exit: bool = True):
    print(color, end='')
    print(*args, end='')
    if undo_when_exit:
        print('\033[0m')


def gray(*values, default: bool = True):
    cprint(*values, color='\033[90m', undo_when_exit=default)


def red(*values, default: bool = True):
    cprint(*values, color='\033[91m', undo_when_exit=default)


def green(*values, default: bool = True):
    cprint(*values, color='\033[92m', undo_when_exit=default)


def yellow(*values, default: bool = True):
    cprint(*values, color='\033[93m', undo_when_exit=default)


def blue(*values, default: bool = True):
    cprint(*values, color='\033[94m', undo_when_exit=default)


def magenta(*values, default: bool = True):
    cprint(*values, color='\033[95m', undo_when_exit=default)


def turquoise(*values, default: bool = True):
    cprint(*values, color='\033[96m', undo_when_exit=default)


def border(*values, default: bool = True):
    cprint(*values, color='\033[97m', undo_when_exit=default)


if __name__ == '__main__':
    blue('test', 'to', 'debug')
