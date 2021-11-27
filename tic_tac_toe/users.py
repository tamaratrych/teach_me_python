from templates import user_interface
from constants import SYMBOLS
import sys


def creat_user(symbol, player_name):
    user = {
        "symbol": symbol,
        "user_steps": [],
        "user_mode": "user"
    }
    if player_name == "":
        player_name = user_interface("enter_name")
    user.update(name=player_name)
    return user


def creat_comp(symbol, player_name=""):
    return {
        "name": "Computer",
        "symbol": symbol,
        "user_steps": [],
        "user_mode": "comp"
    }

second_player = {
    "user": lambda symbol, player_name: creat_user(symbol, player_name),
    "comp": lambda symbol, player_name: creat_comp(symbol, player_name)
}

def get_users(mode):
    """
    This function returns a pair of players depend on mode
    """
    player_name = ""
    try:
        if 5 > len(sys.argv) > 2:
            player_name = sys.argv[2]
    except IndexError:
        player_name = ""
    users = [creat_user(SYMBOLS[0], player_name)]
    try:
        if len(sys.argv) == 4:
            player_name = sys.argv[3]
    except IndexError:
        player_name = ""
    users.append(second_player[mode](SYMBOLS[1], player_name))
    return users