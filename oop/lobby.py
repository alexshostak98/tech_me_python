from constants import SYMBOLS, BOARD_SIZE, MODES
from board import Board
from itertools import cycle

import users


class Lobby:
    def __init__(self, mode=None, name=None):
        print(user_interface("hello"))
        self.mode = mode if mode else self.ask_mode()
        self.users = self.get_users(mode, name)
        self.board = Board(BOARD_SIZE)

    def get_users(self, mode, name):
        for symbol, mode in zip(SYMBOLS, ("HumUser", mode)):
            yield users.mode(symbol=symbol, name=name)

    def ask_mode(self) -> str:
        user_modes = {idx: itm for idx, itm in enumerate(MODES, 1)}
        modes_str = "\n".join(f"{key}: {value}" for key, value in user_modes.items())

        while True:
            try:
                modes_string = user_interface("game_mode", variants=modes_str)
                mode_input = int(modes_string)
                mode = user_modes[mode_input]
                return mode
            except (ValueError, KeyError):
                print(user_interface("choice_error"))
            continue

    def run_game(self, game_num: int) -> (int, dict, int):
        winner = None
        step_num = None
        self.board.print_board()
        for step_num, user in enumerate(cycle(self.users), 1):
            print(user_interface("ask_step", step_num=step_num, user=user["name"]))
            self.user_step(user)
            self.board.print_board()
            if self.board.chek():
                winner = user
                break
            if step_num == self.board.size ** 2:
                break
        return step_num, winner, game_num

    def chek_step(self, step, board: Board) -> bool:
        return True if step in board.empty_steps() else False

    def user_step(self, user):
        while True:
            step = user.get_step()
            if self.chek_step(step, self.board):
                self.board.add_step(step, user)
                break
            else:
                print(user_interface("step_error"))
                continue
