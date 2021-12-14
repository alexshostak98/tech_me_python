from constants import SYMBOLS, BOARD_SIZE, MODES, RESTART_GAME
from board import Board
from command_line import CommandLine
from itertools import cycle
from logger import Logger

import users


class Lobby:

    # TODO: Реализовать логирование метода для записи в файл game_init
    def __init__(self, mode=None, name=None):
        self.mode = mode if mode else self.ask_mode()
        self.users = self.get_users(name)
        self.board = Board(BOARD_SIZE)
        self.game_num = logger.get_game_num()

    # TODO: попытаться облегчить метод ask_mode
    def ask_mode(self) -> str:
        user_modes = {idx: itm for idx, itm in enumerate(MODES, 1)}
        modes_str = "\n".join(f"{key}: {value}" for key, value in user_modes.items())

        while True:
            try:
                modes_string = input(f"Выберите режим игры\n{modes_str}\n>>")
                mode_input = int(modes_string)
                mode = user_modes[mode_input]
                return mode
            except (ValueError, KeyError):
                print("Ошибка ввода")
            continue

    # TODO: Реализовать корректную работу метода с параметром name
    def get_users(self, name):
        result = []
        for symbol, mode in zip(SYMBOLS, ("User", self.mode)):
            user = getattr(users, mode)(symbol=symbol, name=name)
            result.append(user)
        return result

    # TODO: Реализовать логирование метода для записи в файл steps
    def run_game(self) -> (int, dict, int):
        self.board.print_board()
        for step_num, user in enumerate(cycle(self.users), 1):
            print(f"Шаг {step_num} игрока {user.name}")
            self.user_step(user)
            self.board.print_board()
            if self.board.chek():
                self.game_end(step_num, user)
                break
            if step_num == self.board.size ** 2:
                self.game_end(step_num)
                break

    def user_step(self, user):
        while True:
            step = user.get_step(self.board)
            if self.chek_step(step):
                self.board.add_step(step, user)
                break
            else:
                print("Ошибка ввода")
                continue

    def chek_step(self, step) -> bool:
        return True if step in self.board.empty_steps() else False

    # TODO: Реализовать логирование метода для записи в файл game_end
    def game_end(self, step_num, winner=None):
        if winner:
            print(f"На {step_num} ходу победил игрок {winner.name}")
        else:
            print(f"На ходу {step_num} произошла ничья")
        self.restart_game()

    # TODO: Реализовать передачу параметра session_num в требуемые методы для логирования
    def restart_game(self):
        while True:
            user_input = input(f"Сыграем еще раз {'/'.join(RESTART_GAME)}").upper()
            if user_input == RESTART_GAME[0]:
                session_num = logger.get_session_num()
                self.board = Board(BOARD_SIZE)
                self.run_game()
            elif user_input == RESTART_GAME[1]:
                break
            else:
                print("Ошибка выбора")


if __name__ == '__main__':
    c_line = CommandLine()
    c_line.help()
    logger = Logger()
    print("Добро пожаловать в игру")
    lobby = Lobby(c_line.mode, c_line.name)
    lobby.run_game()
