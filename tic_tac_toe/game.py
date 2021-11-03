import sys
from itertools import cycle

from board import get_board, board_match, print_board
from steps import user_step
from users import ask_mode, init_users
from interface import user_interface
from constants import RESTART_GAME, MODES
from logs import init_log_message, write_to_file, get_game_num


def game_init(board_size: int) -> dict:
    print(user_interface("hello"))
    mode = None
    try:
        argv_mode = sys.argv[1]
        if argv_mode.upper() in MODES:
            mode = argv_mode
    except IndexError:
        pass
    if not mode:
        mode = ask_mode()
    users = init_users(mode)
    game_num = get_game_num()
    log_message = init_log_message('game_init', game_num, mode=mode, user1=users[0]['name'], user2=users[1]['name'])
    write_to_file('game_init', log_message)
    return {
        "users": users,
        "board": get_board(board_size),
        'game_num': game_num
    }


def game_end(step_num: int, winner: dict, game_num: int) -> bool:
    if winner:
        print(user_interface('win', step_num=step_num, user=winner["name"]))
        log_message = init_log_message('win', game_num, user=winner['name'], step_num=step_num)
        write_to_file('game_end', log_message)
    else:
        print(user_interface('draw', step_num=step_num))
        log_message = init_log_message('draw', game_num, step_num=step_num)
        write_to_file('game_end', log_message)
    while True:
        user_input = user_interface('new_game', variants='/'.join(RESTART_GAME)).upper()
        if user_input in RESTART_GAME:
            return user_input == RESTART_GAME[0]
        print(user_interface('choice_error'))


def game_cycle(users: list, board: list, game_num: int) -> (int, dict, int):
    winner = None
    step_num = None
    steps = set()
    for step_num, user in enumerate(cycle(users), 1):
        user["all_steps"] = steps
        print(user_interface('ask_step', step_num=step_num, user=user['name']))
        if step_num == 1:
            print_board(board)
        step = user_step(user, board)
        log_step = ':'.join(map(str, step))
        user["steps"].append(step)
        steps.add(step)
        print_board(board)
        log_message = init_log_message('steps', game_num, user=user['name'], step=log_step, step_num=step_num)
        write_to_file('steps', log_message)
        if board_match(board):
            winner = user
            break
        if step_num > 8:
            break
    return step_num, winner, game_num
