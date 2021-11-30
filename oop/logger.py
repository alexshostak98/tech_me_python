import os
from datetime import datetime

from constants import LOGS_FILES_NAME, LOGS_DIR_NAME
from templates import log_template, log_string
from interface import user_interface

log_string = {
    "game_init": "{game_num}#{write_time}#{mode}#{user_1}#{user_2}\n",
    "steps": "{game_num}#{write_time}#{user}#{step}#{step_num}\n",
    "win": "{game_num}#{write_time}#Победитель-{user}#{step_num}\n",
    "draw": "{game_num}#{write_time}#Ничья#{step_num}\n",
}


class Logger:

    def __init__(self):
        self.inc = 1
        self.game_num = 1
        self.session_num = 1

    def get_game_num(self):
        try:
            with open(LOGS_FILES_NAME["game_num"], "r", encoding="UTF-8") as file:
                prev_num = file.read()
                self.game_num = int(prev_num) + self.inc
        except FileNotFoundError:
            os.mkdir(LOGS_DIR_NAME)
        except IOError:
            print(user_interface("log_error"))
        self.write_to_file('game_num', str(self.game_num), 'w')
        return self.game_num

    def get_session_num(self):
        self.session_num += self.inc
        return self.session_num

    def write_to_file(self, name: str, message: str, access_type="a"):
        try:
            with open(LOGS_FILES_NAME[name], access_type, encoding="UTF-8") as file:
                file.write(message)
        except IOError:
            print(user_interface("log_error"))

    def get_log_message(self, string_name: str, **log_data):
        write_time = datetime.now()
        log_message = log_string[string_name].format(game_num=self.game_num, write_time=write_time, **log_data)
        return log_message
