import sys


class Game():

    MODE = {"1": "user", "2": "comp"}
    chosen_mode = None

    def hello(self):
        print("Добро пожаловать в игру!")

    def choose_mode(self):
        argv = ""
        try:
            argv = sys.argv[1].lower()
        except IndexError:
            pass
        if argv in self.MODE.values():
            self.chosen_mode = argv
        else:
            while True:
                try:
                    self.chosen_mode = self.MODE[input(f"С кем хотите играть?\n{self.MODE}")]
                    break
                except KeyError:
                    print("Некорректный вводю Попробуйте еще раз.")

    # def game_cycle(board, users, possible_steps):
    #     print_board(board)
    #     for num_step, user in enumerate(itertools.cycle(users), 1):
    #         user_step[user["user_mode"]](num_step, user, board, possible_steps)
    #         print_board(board)
    #         if check_victory(board):
    #             user_interface("win", name=user["name"], step_number=num_step)
    #             message = f"Result of the game: {user['name']} is a winner\n"
    #             write_in_file("game_log", message)
    #             return None
    #         if num_step == 9:
    #             user_interface("draw")
    #             message = f"Result of the game: draw\n"
    #             write_in_file("game_log", message)
    #             return None
    #
    # def finish_game(self):
    #     while True:
    #         agreement = user_interface("new_game").upper()
    #         if agreement not in AGREEMENT:
    #             user_interface("wrong_input")
    #             continue
    #         return agreement

    def print_help(self):
        try:
            argv = sys.argv[1]
            if argv == '-h':
                print("Выбирете режим игры 'comp' или 'user'")
                sys.exit(0)
        except IndexError:
            pass

# h = Game()
# h.chose_mode
# h.