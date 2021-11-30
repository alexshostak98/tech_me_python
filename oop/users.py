from random import choice

from board import Board
from constants import COMP_NAMES


class Comp:
    def __init__(self, symbol, name=None):
        self.name = self.get_name(name)
        self.symbol = symbol

    def get_name(self, name):
        return name if name else choice(COMP_NAMES)

    def get_step(self, board: Board):
        return choice(tuple(board.empty_steps()))


class User(Comp):
    def get_name(self, name):
        return name if name else input("Введите ваше имя")

    def get_step(self, board: Board):
        step = []
        input_step = input("Введите ваш ход").split(" ")
        for itm in input_step:
            try:
                step.append(int(itm))
            except ValueError:
                break
        return tuple(step)
