import random

from constants import ALL_STEPS_VARIANTS
from board import step_match
from interface import user_interface


def get_step() -> tuple:
    result = []
    steps = user_interface("enter_step").split(" ")
    for itm in steps:
        try:
            result.append(int(itm))
        except ValueError:
            break
    return tuple(result)


def chek_step(step: tuple, user: dict) -> bool:
    if step in ALL_STEPS_VARIANTS.difference(user["all_steps"]):
        return True
    return False


def user_step(user: dict, board: list) -> tuple:
    if user["user_type"] == "COMP":
        step = auto_step(user, board)
        if chek_step(step, user):
            board[step[0]][step[1]] = user["symbol"]
            return step
    while True:
        step = get_step()
        if chek_step(step, user):
            board[step[0]][step[1]] = user["symbol"]
            return step
        else:
            print(user_interface("step_error"))
            continue


def auto_step(user: dict, board: list) -> tuple:
    if not user["steps"]:
        step = (1, 1) if (1, 1) not in user["all_steps"] else (0, 0)
        return step
    item = step_match(board)
    if len(user["steps"]) == 1:
        step = item or (((2, 2) if (2, 2) not in user["all_steps"] else (2, 1)) if (1, 1) in user["steps"] else (2, 0))
        return step
    step = item if item else random.choice(tuple(ALL_STEPS_VARIANTS.difference(user["all_steps"])))
    return step
