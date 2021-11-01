import random

from constants import COMP_NAMES, SYMBOLS
from templates import user_template
from logs import logging


def create_user(symbol: str) -> dict:
    user = {}
    for itm in user_template:
        user[itm[0]] = itm[1](symbol=symbol, user_type="USER")
    return user


def create_comp(symbol: str) -> dict:
    return {
        "name": random.choice(COMP_NAMES),
        "symbol": symbol,
        "steps": [],
        "all_steps": set(),
        "user_type": "COMP",
    }


MODES = {
    "COMP": {"creator": create_comp},
    "USER": {"creator": create_user},
}


def get_user(mode: str, symbol: str) -> dict:
    return MODES[mode]["creator"](symbol=symbol)


def ask_mode() -> str:
    user_modes = {idx: itm for idx, itm in enumerate(MODES, 1)}

    modes_str = "\n".join(f"{key}: {value}" for key, value in user_modes.items())
    modes_string = f"Выберите номер режима игры\n{modes_str}"

    while True:
        try:
            mode_input = int(input(modes_string))
            mode = user_modes[mode_input]
            logging('game_mode', game_mode=mode)
            return mode
        except ValueError:
            print("Недопустимый ввод, введите только число")
        except KeyError:
            print("Недопустимое значение, повторите ввод")
        continue


def create_users(mode: str) -> list:
    users = []
    for symbol, mode in zip(SYMBOLS, ("USER", mode)):
        user = get_user(mode, symbol)
        users.append(user)
    logging('begin_user', begin_user=users[0]['name'])
    return users
