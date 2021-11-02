from constants import SYMBOLS, MODES
from templates import user_template
from interface import user_interface
from logs import logging


def create_users(symbol: str, mode: str) -> dict:
    user = {}
    for itm in user_template:
        user[itm[0]] = itm[1](symbol=symbol, user_type=mode)
    return user


def get_user(mode: str, symbol: str) -> dict:
    user = create_users(symbol=symbol, mode=mode)
    return user


def ask_mode() -> str:
    user_modes = {idx: itm for idx, itm in enumerate(MODES, 1)}

    modes_str = "\n".join(f"{key}: {value}" for key, value in user_modes.items())
    modes_string = user_interface('game_mode', variants=modes_str)

    while True:
        try:
            mode_input = int(modes_string)
            mode = user_modes[mode_input]
            logging('game_mode', game_mode=mode)
            return mode
        except (ValueError, KeyError):
            print(user_interface('wrong_choice'))
        continue


def init_users(mode: str) -> list:
    users = []
    for symbol, mode in zip(SYMBOLS, ("USER", mode)):
        user = get_user(mode, symbol)
        users.append(user)
        logging('user', user=user['name'])
    return users
