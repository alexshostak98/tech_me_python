import os
from datetime import datetime

from constants import LOGS_FILES_NAME, LOGS_DIR_NAME
from templates import log_template, log_string
from interface import user_interface


def get_game_num() -> int:
    inc = 1
    try:
        with open(LOGS_FILES_NAME["game_num"], "r", encoding="UTF-8") as file:
            data = file.read()
            data = int(data) + inc
        write_to_file("game_num", str(data), "w")
        return data
    except FileNotFoundError:
        os.mkdir(LOGS_DIR_NAME)
        write_to_file("game_num", str(inc), "w")
        return inc
    except IOError:
        print(user_interface("log_error"))


def write_to_file(name: str, message: str, access_type="a"):
    try:
        with open(LOGS_FILES_NAME[name], access_type, encoding="UTF-8") as file:
            file.write(message)
    except IOError:
        print(user_interface("log_error"))


def init_log_message(template_name: str, game_num: int, **log_data) -> str:
    write_time = datetime.now()
    log_message = log_template[template_name](log_string[template_name], game_num, write_time, **log_data)
    return log_message
