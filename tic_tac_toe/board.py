from constants import BOARD_SIZE


def get_board() -> list:
    return [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]


def get_diagonals(board: list) -> tuple:
    diagonal = tuple(map(lambda idx: board[idx][idx], range(BOARD_SIZE)))
    diagonal_invert = tuple(map(lambda idx: board[idx][BOARD_SIZE - idx - 1], range(BOARD_SIZE)))
    return diagonal, diagonal_invert


def board_match(board: list) -> bool:
    def chek_line(line: tuple) -> bool:
        line_set = set(line)
        if 0 not in line_set and len(line_set) == 1:
            return True
        return False

    diagonals = get_diagonals(board)
    result = any(map(chek_line, (*diagonals, *board, *zip(*board))))
    return result


def step_match(board: list) -> tuple:
    def check_lines(lines, l_type) -> tuple:
        for idx, item in enumerate(lines):
            if (item.count("X") == 2 or item.count("O") == 2) and 0 in item:
                idx2 = item.index(0)
                steps = {
                    "row": (idx, idx2),
                    "column": (idx2, idx),
                    "diag": (idx2, idx2),
                    "inv_diag": (idx2, len(item) - idx2 - 1)
                }
                return steps[l_type]
        return tuple()

    diagonals = get_diagonals(board)
    line_list = [[board, "row"], [zip(*board), "column"], [[diagonals[0]], "diag"], [[diagonals[1]], "inv_diag"]]
    for line, line_type in line_list:
        result = check_lines(line, line_type)
        if result:
            return result


def print_board(board: list) -> None:
    title_row = f"##{'#'.join(map(str, range(len(board))))}#"
    str_rows = '\n'.join(map(lambda itm: f"{itm[0]}#{'|'.join(map(str, itm[1]))}#", enumerate(board)))
    print(f"{title_row}\n{str_rows}\n{'#' * len(title_row)}")
