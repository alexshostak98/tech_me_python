interface_string = {
    "rules": "",
    "hello": "Добро пожаловать в Игру Крестики Нолики",
    "enter_name": "Введите Ваше имя",
    "game_type": "С кем вы желаете играть {variants}",
    "ask_step": "Ход #{step_num} игрока {user}",
    "win": "На #{step_num} ходу победил игрок {user}",
    "new_game": "Желаете начать новую игру? {variants}",
    "draw": "На {step_num} ходу произошла ничья",
    "wrong_step": """Ход выполнен не корректно, убедитесь, что:
    - введены две координаты;
    - координаты являются целыми числами от 0 до 2;
    - координаты не вводились ранее."""
}

input_template_variants = {
    "game_type": lambda template, **kwargs: template.format(variants=("U", "C")),
    "new_game": lambda template, **kwargs: template.format(variants=("Y", "N")),
    "enter_name": lambda template, **kwargs: template.format(**kwargs),
}

template_variants = {
    "ask_step": lambda template, **kwargs: template.format(**kwargs),
    "win": lambda template, **kwargs: template.format(**kwargs),
    "draw": lambda template, **kwargs: template.format(**kwargs),
}

user_template = (
    ("name", lambda *args, **kwargs: input("ВВЕДИТЕ ВАШЕ ИМЯ")),
    ("symbol", lambda symbol, *args, **kwargs: symbol),
    ("steps", lambda *args, **kwargs: list()),
    ("all_steps", lambda *args, **kwargs: set()),
    ("user_type", lambda user_type, *args, **kwargs: user_type),
)

log_templates = {
    'start_time': lambda start_time: f'\nНачало игры: {start_time}\n',
    'game_mode': lambda game_mode: f'Режим игры: {game_mode}\n',
    'begin_user': lambda begin_user: f'Начавший игрок: {begin_user}\n',
    'steps': lambda step_num, user, step_time: f'Ход {step_num} игрока {user} совершен в {step_time}\n',
    'win': lambda step_num, user: f'На {step_num} ходу победил игрок {user}',
    'draw': lambda step_num: f'На {step_num} ходу произошла ничья',
}

game_type = {
    "U": lambda x: " ",
    "C": lambda x: " "
}
