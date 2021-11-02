from itertools import cycle
from datetime import datetime

from board import get_board, board_match, print_board
from steps import user_step
from users import ask_mode, init_users
from interface import user_interface
from constants import RESTART_GAME
from logs import logging


def game_init(board_size: int) -> dict:
    print(user_interface("hello"))
    logging('start_time', start_time=datetime.now())
    return {
        "users": init_users(ask_mode()),
        "board": get_board(board_size),
    }


def game_end(step_num: int, winner: dict) -> bool:
    if winner:
        print(user_interface('win', step_num=step_num, user=winner["name"]))
        logging('win', step_num=step_num, user=winner["name"])
    else:
        print(user_interface('draw', step_num=step_num))
        logging('draw', step_num=step_num)
    while True:
        user_input = user_interface('new_game', variants='/'.join(RESTART_GAME)).upper()
        if user_input in RESTART_GAME:
            return user_input == RESTART_GAME[0]
        print(user_interface('wrong_choice'))


def game_cycle(users: list, board: list) -> (int, dict):
    winner = None
    step_num = None
    steps = set()
    for step_num, user in enumerate(cycle(users), 1):
        user["all_steps"] = steps
        print(user_interface('ask_step', step_num=step_num, user=user['name']))
        logging('steps', step_num=step_num, user=user['name'], step_time=datetime.time(datetime.now()))
        if step_num == 1:
            print_board(board)
        step = user_step(user, board)
        user["steps"].append(step)
        steps.add(step)
        print_board(board)
        if board_match(board):
            winner = user
            break
        if step_num > 8:
            break
    return step_num, winner
