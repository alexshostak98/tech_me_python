from random import choice

from constants import COMP_NAMES


class CompUser:
    def __init__(self, symbol, name=None):
        self.name = self.get_name(name)
        self.symbol = symbol

    def get_name(self, name):
        return name if name else choice(COMP_NAMES)

    def get_step(self):
        pass


class HumUser(CompUser):
    def get_name(self, name):
        return name if name else input(interface_string["enter_name"])

    def get_step(self):
        result = []
        steps = user_interface("enter_step").split(" ")
        for itm in steps:
            try:
                result.append(int(itm))
            except ValueError:
                break
        return tuple(result)
