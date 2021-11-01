import itertools

"""
Игра Крестики нолики
"""
"""
Правила игры:
Игровое поле 3х3
участвуют 2 игрока
игроки ходят поочереди
каждый игрок имеет индивидуальный символ который ставит на свободную ячейку игрового поля
Победитель определяется по следующим правилам:
символ игрока заполняет горизонталь, вертикаль или диагональ
возможный исход игры когда нет победителя
"""
# TODO: Играть с компуктером
# TODO: Игровое поле в виде Матрицы 3на3 не изменяемо.
# TODO: Ячейка игрового поля будет изменяться,
"""(
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
)"""
# TODO: Игрок Словарь - ТИП пользователя

# TODO: Управляющий игрой распорядитель

# TODO: Функция матчинга игрового поля на наличие победителя
# TODO: Определение возможности хода
# TODO: Функция Взаимодействия с пользователем на предмет хода
# TODO: Функция совершения хода записывает на игровое поле в ячейку самого пользователя

interface_string = {
    "rules": "",
    "hello": "Здравствуй игрок",
    "enter_name": "Игрок #{user_number}: Введите свое имя",
    "game_type": "С кем вы желаете играть {variants}",
    "ask_step": "Ход #{step_number} игрока {name}",
    "win": "Победил игрок {name} на ходу #{step_number}",
    "new_game": "Желаете начать новую игру? {variants}",
    "draw": "Ничья победителей нет",
    "wrong_step": """Ход выполнен не корректно, убедитесь, что:
    - введены две координаты;
    - координаты являются целыми числами от 0 до 2;
    - координаты не вводились ранее."""
}

template_variants = {
    "game_type": lambda template, **kwargs: template.format(variants=("U", "C")),
    "ask_step": lambda template, **kwargs: template.format(**kwargs),
    "win": lambda template, **kwargs: template.format(**kwargs),
    "new_game": lambda template, **kwargs: template.format(variants=("Y", "N")),
    "enter_name": lambda template, **kwargs: template.format(**kwargs),
}

game_type = {
    "U": lambda x: " ",
    "C": lambda x: " "
}


def user_interface(template_name, **template_vars):
    if template_name in template_variants:
        ask_str = template_variants[template_name](interface_string[template_name], **template_vars)
        user_input = input(ask_str)
        return user_input
    else:
        print(interface_string[template_name])


def matrix_match(board):
    def chek_line(line):
        line_set = set(line)
        if (0 not in line_set and len(line_set) == 1):
            raise ValueError("CHECK_LINE")
        return False

    board_len = len(board)
    diagonal = map(lambda idx: board[idx][idx], range(0, board_len))
    diagonal_invert = map(lambda idx: board[idx][board_len - idx - 1], range(board_len - 1, -1, -1))
    try:
        _ = any(map(chek_line, (diagonal, diagonal_invert)))
        for row, column in zip(board, zip(*board)):
            _ = any(map(chek_line, (row, column)))
    except ValueError as exc:
        if 'CHECK_LINE' in exc.args:
            return True
        else:
            raise exc
    return False


matrix_board = (
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
)

users_list = ['Дмитрий', 'Сергей']


def step_possibility(board):
    for row in board:
        if 0 in row:
            return True
    return False


def step_check(user_input, board):
    board_len = len(board)
    user_input = user_input.strip().split(' ')
    user_input_len = len(user_input)
    coordinate = []
    try:
        for item in user_input:
            if item.isdigit() and int(item) in range(board_len) and user_input_len == 2:
                coordinate.append(int(item))
        if board[coordinate[0]][coordinate[1]] == 0:
            return coordinate
        else:
            raise IndexError
    except IndexError:
        user_interface('wrong_step')


def save_step(coord, board, user):
    board[coord[0]][coord[1]] = user
    return board


def game(users: list, board):
    step_number = 1
    for idx, user in enumerate(itertools.cycle(users)):
        if step_possibility(board):
            error = True
            while error:
                ask_step = user_interface('ask_step', name=user, step_number=step_number)
                new_step = step_check(ask_step, board)
                if new_step:
                    error = not error
            win_check = matrix_match(save_step(new_step, board, user))
            if win_check:
                result = user_interface('win', name=user, step_number=step_number)
                return result
        else:
            return user_interface('draw')
        if idx % 2:
            step_number += 1


# должна циклично итерироваться по пользователям либо написать свой цикличный итератор либо найти его в itertools
# Опрашивать пользователя на предмет хода
# Проверяем возможность хода
# Проверяем выйгрышный вариант
# Либо поздравить с победой, либо обьявить Ничью


def main():
    game(users_list, matrix_board)


main()
