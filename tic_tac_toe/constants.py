SIZE_BOARD = 3 # Size of a matrix (board) has to be an odd number

SYMBOLS = ("X", "O")

MODE = {
    "1": "user",
    "2": "comp"
}

AGREEMENT = ("Y", "N")

def ttt_help():
    print("Поддерживаемые аргументы:\ncomp имя_игрока\nuser имя_первого_игрока имя_второго_игрока")