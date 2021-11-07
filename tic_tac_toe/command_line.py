import sys

from constants import MODES
from interface import user_interface


def command_line_help():
    try:
        if sys.argv[1] == "help":
            print(user_interface("help"))
            sys.exit()
    except IndexError:
        pass


def command_line_mode():
    try:
        argv_mode = sys.argv[1]
        if argv_mode.upper() in MODES:
            return argv_mode.upper()
        else:
            raise IndexError
    except IndexError:
        pass


def command_line_users():
    try:
        return sys.argv[2:]
    except IndexError:
        pass
