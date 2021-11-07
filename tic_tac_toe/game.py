import itertools
import sys

from users import get_users
from templates import user_interface
from board import create_board, check_victory, print_board
from constants import MODE, AGREEMENT, ttt_help
from steps import user_step
from logging import count_session, log_game, write_in_file, log_step


@count_session
def start_game():
    """
    This function initiates a game: create a board and defines players
    """
    # count_session()
    user_interface("rules")
    user_interface("hello")
    board = create_board()
    chosen_mode = ""
    try:
        argv = sys.argv[1]
        if argv in user_step:
            chosen_mode = argv
    except IndexError:
        while True:
            try:
                mode = user_interface('game_type')
                chosen_mode = MODE[mode]
                break
            except KeyError:
                user_interface("wrong_input")
    users = get_users(chosen_mode)
    return (board, users)


@log_game
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
            message = f"Result of the game: {user['name']} is a winner\n"
            write_in_file("game_log", message)
            return None
        if num_step == 9:
            user_interface("draw")
            message = f"Result of the game: draw\n"
            write_in_file("game_log", message)
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


def print_help():
    try:
        argv = sys.argv[1]
        if argv == '-h':
            ttt_help()
            sys.exit(0)
    except IndexError:
        pass