from collections import defaultdict

import class_game
import class_log
import class_player
import class_board

SIZE_BOARD = 3

def main():
    new_game = class_game.Game()
    logging = class_log.Log()
    logging.get_num_session()
    logging.count_session()
    new_game.print_help()
    new_game.hello()
    logging.log_start_game()
    new_game.choose_mode()
    player_1 = class_player.User("X")
    player_2 = class_player.User("O") if new_game.chosen_mode == new_game.MODE["1"] else class_player.Player("O")
    board = class_board.Board(SIZE_BOARD)
    users = (player_1, player_2)
    revenge = "Y"
    while revenge == "Y":
        new_game.game_cycle(board, users, logging)
        logging.log_finish_game()
        revenge = new_game.finish_game()
        if revenge == "Y":
            board.done_steps = defaultdict(set)


if __name__ == "__main__":
    main()
