import random
from class_board import Board

class Player():

    def __init__(self, symbol, name=None):
        self.symbol = symbol
        self.name = self.get_name(name)

    NAMES = (
        "Computer",
        "Kiberg",
        "Moska",
        "Susanin",
        "Elochka",
    )

    def get_name(self, name):
        if name:
            return name
        return random.choice(self.NAMES)

    def make_step(self, board) -> "tuple[int, int]":
        return random.choice(board.all_steps.difference(board.done_steps))


class User(Player):

    def get_name(self, name):
        if name:
            return name
        return input("Как ваше имя?\n")

    def make_step(self, board) -> "tuple[int, int]":
        while True:
            step = input("Сделайте шаг: введите коортинаты через пробел\n").split(" ")
            try:
                step = int(step[0]), int(step[1])
                if step in board.all_steps.difference(board.done_steps):
                    return step
                print("Вы ввели занятую ячейку или ячейку вне игрового поля. Попробуйте еще раз.")
                continue
            except (IndexError, ValueError):
                print(f"Ошибка ввода. Введите два числа через пробел от 0 до {board.size-1}")


# b = Board(3)
# p = User("x")
#print(p.name)
# p.make_step(b)