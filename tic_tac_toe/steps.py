import random

from constants import ALL_STEPS_VARIANTS
from interface import user_interface


def get_step() -> tuple:
    result = []
    steps = user_interface('enter_step').split(" ")
    for itm in steps:
        try:
            result.append(int(itm))
        except ValueError:
            result.append(itm)
            break
    return tuple(result)


def chek_step(step: tuple, user: dict) -> bool:
    if step in ALL_STEPS_VARIANTS.difference(user['all_steps']):
        return True
    return False


def user_step(user: dict, board: list) -> tuple:
    if user["user_type"] == "COMP":
        step = auto_step(user)
        if chek_step(step, user):
            board[step[0]][step[1]] = user["symbol"]
            return step
    while True:
        step = get_step()
        if chek_step(step, user):
            board[step[0]][step[1]] = user["symbol"]
            return step
        else:
            print(user_interface('wrong_step'))
            continue


def auto_step(user: dict) -> tuple:
    return random.choice(tuple(ALL_STEPS_VARIANTS.difference(user["all_steps"])))
