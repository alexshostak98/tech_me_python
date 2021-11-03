import os

# SYMBOLS = ("\033[31mX\033[0m", "\033[33mO\033[0m")
SYMBOLS = ("X", "O")

COMP_NAMES = [
    "R2D2",
    "C3PO",
    "WALLE",
    "DALEK",
]

GAME_RULES = """Аргументы игры:
Системные:
- [0-ой] - зарезервирован системой, всегда хранит путь к запускаемому файлу;
- [1-ый] help - выводит на экран информацию о доступных аргументах для запуска через коммандную строку и правила игры.
Игровые:  
- [1-ый] game_mode (COMP/USER) - позволяет выбрать режим игры через коммандную строку;
- [2-ой] user_name1 - позволяет выбрать имя первого игрока через коммандную строку;
- [3-ий] user_name2 - позволяет выбрать имя второго игрока через коммандную строку
  (доступен только при выборе режима игры USER).
  
Правила игры:
Игроки по очереди ставят на свободные клетки поля 3×3 знаки
(один всегда крестики, другой всегда нолики).
Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает.
Если ни одному из игроков не удалось выстроить 3 свои фигуры в ряд, объявляется ничья.
Первый ход делает игрок, ставящий крестики.
"""

BOARD_SIZE = 3

RESTART_GAME = ('Y', 'N')

MODES = ('COMP', 'USER')

ALL_STEPS_VARIANTS = set((i, j) for i in range(BOARD_SIZE) for j in range(BOARD_SIZE))

ROOT_DIR_PATH = os.path.dirname(os.path.abspath(__file__))

LOGS_DIR_NAME = 'logs'

LOGS_DIR_PATH = os.path.join(ROOT_DIR_PATH, LOGS_DIR_NAME)

LOGS_FILES_NAME = {
    "game_init": os.path.join(LOGS_DIR_PATH, "game_init"),
    "steps": os.path.join(LOGS_DIR_PATH, "steps"),
    "game_end": os.path.join(LOGS_DIR_PATH, "game_end"),
    "game_num": os.path.join(LOGS_DIR_PATH, "game_num")
}
