import sys

from constants import MODES


def except_decorate(func):
    def wrapper(self):
        try:
            return func(self)
        except IndexError:
            pass

    return wrapper


class CommandLine:

    def __init__(self):
        self.args = sys.argv
        self.mode = self.modes()
        self.name = self.user_names()

    @except_decorate
    def help(self):
        if self.args[1] == "help":
            print("Help")
            # print(user_interface("help"))
            sys.exit()

    @except_decorate
    def modes(self):
        argv_mode = self.args[1].title()
        if argv_mode in MODES:
            return argv_mode

    @except_decorate
    def user_names(self):
        return self.args[2:]
