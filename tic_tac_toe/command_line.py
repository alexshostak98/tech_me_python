import sys

from constants import MODES
from interface import user_interface


def command_line_help() -> None:
    try:
        if sys.argv[1] == "help":
            print(user_interface("help"))
            sys.exit()
    except IndexError:
        pass


def command_line_mode() -> str:
    try:
        argv_mode = sys.argv[1].upper()
        if argv_mode in MODES:
            return argv_mode
        else:
            return ''
    except IndexError:
        pass


def command_line_users() -> list:
    try:
        return sys.argv[2:]
    except IndexError:
        return []
