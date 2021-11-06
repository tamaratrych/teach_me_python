from datetime import datetime

from globals import number_current_session, number_game


def write_in_file(file_name, message, mode="a", ):
    try:
        with open(file_name, mode, encoding="UTF-8") as file:
            file.write(message)
    except IOError:
        print("Ошибка записи в файл")


def get_num_session():
    try:
        with open("number_session", "r", encoding="UTF-8") as file:
            num_session = str(int(file.read()) + 1)
    except FileNotFoundError:
        num_session = "1"
    return num_session


def count_session(func):
    def wraper():
        num_session = get_num_session()
        write_in_file("number_session", num_session, "w")
        global number_current_session
        number_current_session = num_session
        return func()
    return wraper


def log_game(func):
    def wrapper(*args):
        global number_game
        message = f"Session #{number_current_session}. Start game #{number_game} at {datetime.now().isoformat()}\n"
        write_in_file("game_log", message)
        func(*args)
        message = f"Session #{number_current_session}. Finish game #{number_game} at {datetime.now().isoformat()}\n"
        write_in_file("game_log", message)
        number_game += 1
    return wrapper


def log_step(func):
    def wrapper(*args):
        func(*args)
        params = args
        step_coordinates = params[1]["user_steps"][len(params[1]["user_steps"])-1]
        message = f"Session #{number_current_session}; game #{number_game}; player's name {params[1]['name']}; player's step {step_coordinates}\n"
        write_in_file("game_log", message)
    return wrapper