import sys

from game import start_game, game_cycle, finish_game
from constants import SIZE_BOARD, ttt_help
from board import create_board


def main():
    try:
        argv = sys.argv[1]
        if argv == '-h':
            ttt_help()
            return None
    except IndexError:
        pass
    board, users = start_game()
    possible_steps = [(idx, idy) for idx in range(SIZE_BOARD) for idy in range(SIZE_BOARD)]
    new_game = "Y"
    while new_game == "Y":
        game_cycle(board, users, possible_steps)
        new_game = finish_game()
        if new_game == "Y":
            board = create_board()
            possible_steps = [(idx, idy) for idx in range(SIZE_BOARD) for idy in range(SIZE_BOARD)]


if __name__ == "__main__":
    main()

