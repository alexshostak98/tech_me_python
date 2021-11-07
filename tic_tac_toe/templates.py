from random import choice

from constants import COMP_NAMES, GAME_RULES

interface_string = {
    "help": GAME_RULES,
    "hello": "Добро пожаловать в Игру Крестики Нолики",
    "game_mode": "Выберите режим игры\n{variants}\n>>",
    "enter_name": "Введите Ваше имя\n>>",
    "enter_step": "Введите координаты хода через пробел\n>>",
    "ask_step": "Ход #{step_num} игрока {user}",
    "win": "На #{step_num} ходу победил игрок {user}",
    "draw": "На {step_num} ходу произошла ничья",
    "new_game": "Сыграем еще раз? {variants}\n>>",
    "step_error": """Ход выполнен не корректно, убедитесь, что:
    - введены две координаты;
    - координаты являются целыми числами от 0 до 2;
    - координаты не вводились ранее.""",
    "choice_error": "Некорректный ввод. Попробуйте снова",
    "log_error": "Ошибка чтения лога",
}

log_string = {
    "game_init": "{}#{}#{mode}#{user1}#{user2}\n",
    "steps": "{}#{}#{user}#{step}#{step_num}\n",
    "win": "{}#{}#Победитель-{user}#{step_num}\n",
    "draw": "{}#{}#Ничья#{step_num}\n",
}

input_template_variants = {
    "game_mode": lambda template, **kwargs: template.format(**kwargs),
    "new_game": lambda template, **kwargs: template.format(**kwargs),
    "enter_name": lambda template, **kwargs: template.format(**kwargs),
    "enter_step": lambda template, **kwargs: template.format(**kwargs),
}

template_variants = {
    "ask_step": lambda template, **kwargs: template.format(**kwargs),
    "win": lambda template, **kwargs: template.format(**kwargs),
    "draw": lambda template, **kwargs: template.format(**kwargs),
}

log_template = {
    "game_init": lambda template, *args, **kwargs: template.format(*args, **kwargs),
    "steps": lambda template, *args, **kwargs: template.format(*args, **kwargs),
    "win": lambda template, *args, **kwargs: template.format(*args, **kwargs),
    "draw": lambda template, *args, **kwargs: template.format(*args, **kwargs),
}

user_template = (
    ("name", lambda user_type, *args, **kwargs: input(
        interface_string["enter_name"]) if user_type == "USER" else choice(COMP_NAMES)),
    ("symbol", lambda symbol, *args, **kwargs: symbol),
    ("steps", lambda *args, **kwargs: list()),
    ("all_steps", lambda *args, **kwargs: set()),
    ("user_type", lambda user_type, *args, **kwargs: user_type),
)
