from game import start_game, game_cycle, finish_game, print_help
from board import create_board
from steps import get_empty_steps


def main():
    print_help()
    board, users = start_game()
    possible_steps = get_empty_steps()
    new_game = "Y"
    while new_game == "Y":
        game_cycle(board, users, possible_steps)
        new_game = finish_game()
        if new_game == "Y":
            board = create_board()
            possible_steps = get_empty_steps()


if __name__ == "__main__":
    main()

