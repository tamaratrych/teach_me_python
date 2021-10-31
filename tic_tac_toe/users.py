from templates import user_interface
from globals import SYMBOLS


def creat_user(symbol):
    return {
        "name": user_interface("enter_name"),
        "symbol": symbol,
        "user_steps": [],
        "user_mode": "user"
    }


def creat_comp(symbol):
    return {
        "name": "Computer",
        "symbol": symbol,
        "user_steps": [],
        "user_mode": "comp"
    }

second_player = {
    "user": lambda symbol: creat_user(symbol=SYMBOLS[1]),
    "comp": lambda symbol: creat_comp(symbol=SYMBOLS[1])
}

def get_users(mode):
    users = [creat_user(SYMBOLS[0])]
    users.append(second_player[mode](SYMBOLS[1]))
    return users