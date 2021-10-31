import itertools

from users import get_users
from templates import user_interface
from board import create_board, check_victory
from constants import MODE, SIZE_BOARD
from steps import user_step


def start_game():
    user_interface("rules")
    user_interface("hello")
    board = create_board()
    mode = user_interface('game_type')
    users = get_users(MODE[mode])
    return (board, users)


def game_cycle(board, users):
    for num_step in range(SIZE_BOARD**2):
        for user in itertools.cycle(users):
            user_step[user["user_mode"]](num_step, user, board)
            if check_victory(board):
                user_interface("win", name=user["name"], step_number=num_step)
                break
    user_interface("draw")

board, users = start_game()
print(board, users)
game_cycle(board, users)


