import itertools

from users import get_users
from templates import user_interface
from board import create_board, check_victory
from constants import MODE, SIZE_BOARD, AGREEMENT
from steps import user_step


def start_game():
    """
    This function initiates a game: creat a board and defines players
    """
    user_interface("rules")
    user_interface("hello")
    board = create_board()
    mode = user_interface('game_type')
    users = get_users(MODE[mode])
    return (board, users)


def game_cycle(board, users):
    """
    This function fills the board with "O" and "X"(alternate steps of the players)
    until the winner will be determined or a draw will be established
    """
    for num_step in range(SIZE_BOARD**2+1, 1):
        for user in itertools.cycle(users):
            user_step[user["user_mode"]](num_step, user, board)
            if check_victory(board):
                user_interface("win", name=user["name"], step_number=num_step)
                return None
    user_interface("draw")


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
    board, users = start_game()
    new_game = "Y"
    while new_game == "Y":
        game_cycle(board, users)
        new_game = finish_game()
        if new_game == "Y":
            board = create_board()

if __name__ == "__main__":
    main()