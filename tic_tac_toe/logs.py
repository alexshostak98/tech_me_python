import os
from datetime import datetime

from constants import LOGS_FILES_NAME, LOGS_DIR_NAME
from templates import log_template, log_string
from interface import user_interface


def get_game_num() -> int:
    inc = 1
    try:
        file = open(LOGS_FILES_NAME["game_num"], "r", encoding="UTF-8")
    except FileNotFoundError:
        os.mkdir(LOGS_DIR_NAME)
        write_to_file("game_num", str(inc), "w")
        return inc
    try:
        data = file.read()
        if not data:
            return inc
        inc = int(data) + 1
        return inc
    except IOError:
        print(user_interface("log_error"))
    finally:
        file.close()
        write_to_file("game_num", str(inc), "w")


def write_to_file(name: str, message: str, access_type="a"):
    file = open(LOGS_FILES_NAME[name], access_type, encoding="UTF-8")
    try:
        file.write(message)
    except IOError:
        print(user_interface("log_error"))
    finally:
        file.close()


def init_log_message(template_name: str, game_num: int, **log_data) -> str:
    write_time = datetime.now()
    log_message = log_template[template_name](log_string[template_name], game_num, write_time, **log_data)
    return log_message
