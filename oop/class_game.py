import sys
import itertools


class Game():

    MODE = {"1": "user", "2": "comp"}
    AGREEMENT = ("Y", "N")
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
            mode = "\n".join(f"{key}: {value}" for key, value in self.MODE.items())
            while True:
                try:
                    self.chosen_mode = self.MODE[input(f"С кем хотите играть?\n{mode}\n>>>")]
                    break
                except KeyError:
                    print("Некорректный вводю Попробуйте еще раз.")

    def game_cycle(self, board, users, logging):
        board.print_board()
        for num_step, user in enumerate(itertools.cycle(users), 1):
            step = user.make_step(board)
            board.add_step(step, user)
            logging.log_step(user, step)
            board.print_board()
            if board.check(user):
                print(f"Победил {user.name} на шаге #{num_step}")
                message = f"Result of the game: {user.name} is a winner\n"
                logging.write_in_file(logging.game_log, message)
                return None
            if num_step == 9:
                print("Ничья")
                message = f"Result of the game: draw\n"
                logging.write_in_file(logging.game_log, message)
                return None

    def finish_game(self):
        agreement_str = ", ".join(self.AGREEMENT)
        while True:
            play_again = input(f"Желаете сыграть еще раз? {agreement_str}\n>>> ").upper()
            if play_again not in self.AGREEMENT:
                print("Некорректный ввод. Попробуйте еще раз.")
                continue
            return play_again

    def print_help(self):
        try:
            argv = sys.argv[1]
            if argv == '-h':
                print("Выбирете режим игры 'comp' или 'user'")
                sys.exit(0)
        except IndexError:
            pass