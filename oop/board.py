from typing import Tuple


class Board:

    def __init__(self, size):
        self.size = size
        self.view = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.all_steps = set((n, m) for n in range(self.size) for m in range(self.size))
        self.done_steps = set()

    def print_board(self):
        title_row = f"##{'#'.join(map(str, range(self.size)))}#"
        str_rows = '\n'.join(map(lambda itm: f"{itm[0]}#{'|'.join(map(str, itm[1]))}#", enumerate(self.view)))
        print(f"{title_row}\n{str_rows}\n{'#' * len(title_row)}")

    def add_step(self, step: Tuple[int, int], user) -> None:
        self.view[step[0]][step[1]] = user.symbol
        self.done_steps.add(step)

    def empty_steps(self) -> set:
        steps = self.all_steps.difference(self.done_steps)
        return steps

    def get_diagonals(self) -> tuple:
        diagonal = tuple(map(lambda idx: self.view[idx][idx], range(self.size)))
        diagonal_invert = tuple(map(lambda idx: self.view[idx][self.size - idx - 1], range(self.size)))
        return diagonal, diagonal_invert

    def chek_line(self, line: tuple) -> bool:
        line_set = set(line)
        if 0 not in line_set and len(line_set) == 1:
            return True
        return False

    def chek(self) -> bool:
        diagonals = self.get_diagonals()
        result = any(map(self.chek_line, (*diagonals, *self.view, *zip(*self.view))))
        return result

    def chek_1(self):
        diagonals = self.get_diagonals()
        result = map(self.chek_line, (
            (self.view, "row"), (zip(*self.view), "column"), ([diagonals[0]], "diag"), ([diagonals[1]], "inv_diag")))
        return result

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
