import itertools
import sys

from users import get_users
from templates import user_interface
from board import create_board, check_victory, print_board
from constants import MODE, SIZE_BOARD, AGREEMENT, ttt_help
from steps import user_step


def start_game():
    """
    This function initiates a game: creat a board and defines players
    """
    user_interface("rules")
    user_interface("hello")
    board = create_board()
    chosen_mode = ""
    try:
        argv = sys.argv[1]
        if argv in user_step:
            chosen_mode = argv
    except IndexError:
        mode = user_interface('game_type')
        chosen_mode = MODE[mode]
    users = get_users(chosen_mode)
    return (board, users)


def game_cycle(board, users, possible_steps):
    """
    This function fills the board with "O" and "X"(alternate steps of the players)
    until the winner will be determined or a draw will be established
    """
    for num_step, user in enumerate(itertools.cycle(users), 1):
        user_step[user["user_mode"]](num_step, user, board, possible_steps)
        print_board(board)
        if check_victory(board):
            user_interface("win", name=user["name"], step_number=num_step)
            return None
        if num_step == 9:
            user_interface("draw")
            return None


def finish_game():
    """
    This function restart (revenge) or finish the game
    """
    while True:
        agreement = user_interface("new_game")
        if agreement not in AGREEMENT:
            user_interface("wrong_input")
            continue
        return agreement


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
