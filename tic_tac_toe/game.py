from itertools import cycle

from command_line import command_line_mode
from board import get_board, board_match, print_board
from steps import user_step
from users import get_users, ask_mode
from interface import user_interface
from constants import RESTART_GAME
from logs import init_log_message, write_to_file, get_game_num


def game_init(board_size: int) -> dict:
    print(user_interface("hello"))
    command = command_line_mode()
    mode = command if command else ask_mode()
    users = get_users(mode)
    game_num = get_game_num()
    log_message = init_log_message("game_init", game_num, mode=mode, user1=users[0]["name"], user2=users[1]["name"])
    write_to_file("game_init", log_message)
    return {
        "users": users,
        "board": get_board(board_size),
        "game_num": game_num
    }


def game_end(step_num: int, winner: dict, game_num: int) -> bool:
    if winner:
        print(user_interface("win", step_num=step_num, user=winner["name"]))
        log_message = init_log_message("win", game_num, user=winner["name"], step_num=step_num)
        write_to_file("game_end", log_message)
    else:
        print(user_interface("draw", step_num=step_num))
        log_message = init_log_message("draw", game_num, step_num=step_num)
        write_to_file("game_end", log_message)
    while True:
        user_input = user_interface("new_game", variants='/'.join(RESTART_GAME)).upper()
        if user_input in RESTART_GAME:
            return user_input == RESTART_GAME[0]
        print(user_interface("choice_error"))


def game_cycle(users: list, board: list, game_num: int) -> (int, dict, int):
    winner = None
    step_num = None
    all_steps = set()
    print_board(board)
    for step_num, user in enumerate(cycle(users), 1):
        user["all_steps"] = all_steps
        print(user_interface("ask_step", step_num=step_num, user=user["name"]))
        step = user_step(user, board)
        print_board(board)
        user["steps"].append(step)
        all_steps.add(step)
        log_step = ":".join(map(str, step))
        log_message = init_log_message("steps", game_num, user=user["name"], step=log_step, step_num=step_num)
        write_to_file("steps", log_message)
        if board_match(board):
            winner = user
            break
        if step_num > 8:
            break
    return step_num, winner, game_num
