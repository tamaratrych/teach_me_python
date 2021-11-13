import os
from _datetime import datetime


class Log():
    dirname = os.path.dirname(__file__)
    game_log = os.path.join(dirname, 'logging.py')
    num_session = os.path.join(dirname, 'num_session.py')

    number_current_session = None
    number_game = 1

    def write_in_file(self, file_name, message, mode="a"):
        try:
            with open(file_name, mode, encoding="UTF-8") as file:
                file.write(message)
        except IOError:
            print("Ошибка записи в файл")

    def get_num_session(self):
        try:
            with open(self.num_session, "r", encoding="UTF-8") as file:
                self.number_current_session = str(int(file.read()) + 1)
        except (FileNotFoundError, ValueError):
            self.number_current_session = "1"

    def count_session(self):
        num_session = self.get_num_session()
        self.write_in_file(num_session, num_session, "w")
        self.number_current_session = num_session

    def log_start_game(self):
        message = f"Session #{self.number_current_session}. Start game #{self.number_game} at {datetime.now().isoformat()}\n"
        self.write_in_file(self.game_log, message)

    def log_finish_game(self):
        message = f"Session #{self.number_current_session}. Finish game #{self.number_game} at {datetime.now().isoformat()}\n"
        self.write_in_file(self.game_log, message)
        self.number_game += 1

    def log_step(self, user, step):
        message = f"Session #{self.number_current_session}; game #{self.number_game}; player's name {user.name}; player's step {step[0]}_{step[1]}\n"
        self.write_in_file(self.game_log, message)