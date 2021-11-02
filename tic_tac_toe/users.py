from templates import user_interface
from constants import SYMBOLS
import  sys


def creat_user(symbol):
    return {
        "name": user_interface("enter_name"),
        "symbol": symbol,
        "user_steps": [],
        "user_mode": "user"
    }

def creat_user(symbol, player_name):
    user = {
        #"name": user_interface("enter_name"),
        "symbol": symbol,
        "user_steps": [],
        "user_mode": "user"
    }
    if player_name == "":
        player_name = user_interface("enter_name")
        user.update(name=player_name)
    else:
        user.update(name=player_name)
    return user

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
    """
    This function returns a pair of players depend on mode
    """
    player_name = ""

    try:
        if len(sys.argv) == 3:
            player_name = sys.argv[2]
    except IndexError:
        player_name = ""
    users = [creat_user(SYMBOLS[0], player_name)]
    users.append(second_player[mode](SYMBOLS[1]))
    return users