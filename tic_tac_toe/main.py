from constants import BOARD_SIZE
from board import get_board
from game import game_init, game_cycle, game_end


def main() -> None:
    game_vars = game_init(BOARD_SIZE)
    end_result = True
    while end_result:
        result_game = game_cycle(**game_vars)
        end_result = game_end(*result_game)
        if end_result:
            game_vars["board"] = get_board(BOARD_SIZE)


if __name__ == '__main__':
    main()
