from constants import BOARD_SIZE
from board import get_board
from game import game_init, game_cycle, game_end
from command_line import command_line_help


def main() -> None:
    command_line_help()
    game_vars = game_init(BOARD_SIZE)
    end_result = True
    while end_result:
        result_game = game_cycle(**game_vars)
        end_result = game_end(*result_game)
        if end_result:
            game_vars["board"] = get_board(BOARD_SIZE)
            game_vars["users"][0]["steps"].clear()
            game_vars["users"][1]["steps"].clear()


if __name__ == "__main__":
    main()
