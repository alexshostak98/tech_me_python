from random import choice

from constants import COMP_NAMES

interface_string = {
    "rules": """Игроки по очереди ставят на свободные клетки поля 3×3 знаки 
    (один всегда крестики, другой всегда нолики). 
    Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает.
    Если ни одному из игроков не удалось выстроить 3 свои фигуры в ряд, объявляется ничья. 
    Первый ход делает игрок, ставящий крестики.""",
    "hello": "Добро пожаловать в Игру Крестики Нолики",
    "game_mode": "Выберите режим игры\n{variants}\n>>",
    "enter_name": "Введите Ваше имя\n>>",
    "enter_step": "Введите координаты хода через пробел\n>>",
    "ask_step": "Ход #{step_num} игрока {user}",
    "win": "На #{step_num} ходу победил игрок {user}",
    "draw": "На {step_num} ходу произошла ничья",
    "new_game": "Сыграем еще раз? {variants}\n>>",
    "wrong_step": """Ход выполнен не корректно, убедитесь, что:
    - введены две координаты;
    - координаты являются целыми числами от 0 до 2;
    - координаты не вводились ранее.""",
    "wrong_choice": "Некорректный ввод. Попробуйте снова",
}

log_string = {
    'start_time': '\nНачало игры: {start_time}\n',
    'game_mode': 'Режим игры: {game_mode}\n',
    'user': 'Игрок: {user}\n',
    'steps': 'Ход {step_num} игрока {user} совершен в {step_time}\n',
    'win': 'На {step_num} ходу победил игрок {user}\n',
    'draw': 'На {step_num} ходу произошла ничья\n',
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

log_templates = {
    'start_time': lambda template, **kwargs: template.format(**kwargs),
    'game_mode': lambda template, **kwargs: template.format(**kwargs),
    'user': lambda template, **kwargs: template.format(**kwargs),
    'steps': lambda template, **kwargs: template.format(**kwargs),
    'win': lambda template, **kwargs: template.format(**kwargs),
    'draw': lambda template, **kwargs: template.format(**kwargs),
}

user_template = (
    ("name", lambda user_type, *args, **kwargs: input(interface_string['enter_name']) if user_type == 'USER' else choice(COMP_NAMES)),
    ("symbol", lambda symbol, *args, **kwargs: symbol),
    ("steps", lambda *args, **kwargs: list()),
    ("all_steps", lambda *args, **kwargs: set()),
    ("user_type", lambda user_type, *args, **kwargs: user_type),
)
