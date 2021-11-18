from collections import defaultdict
import sys

import class_game
import class_log
import class_player
import class_board

class LogicGame:
    SIZE_BOARD = 3
    new_game = class_game.Game()
    board = class_board.Board(SIZE_BOARD)

    def run_game(self):
        logging = class_log.Log()
        logging.get_num_session()
        logging.count_session()
        self.new_game.print_help()
        self.new_game.hello()
        logging.log_start_game()
        self.new_game.choose_mode()
        users = self.create_users()
        revenge = "Y"
        while revenge == "Y":
            self.new_game.game_cycle(self.board, users, logging)
            logging.log_finish_game()
            revenge = self.new_game.finish_game()
            if revenge == "Y":
                self.board.done_steps = defaultdict(set)

    def create_users(self):
        name = None
        try:
            name = sys.argv[2]
        except IndexError:
            pass
        player_1 = class_player.User("X", name)
        name = None
        try:
            name = sys.argv[3]
        except IndexError:
            pass
        player_2 = class_player.User("O", name) if self.new_game.chosen_mode == self.new_game.MODE["1"] else class_player.Player("O")
        return (player_1, player_2)


