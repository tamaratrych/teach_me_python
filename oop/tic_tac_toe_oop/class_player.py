import random
#from class_board import Board
from itertools import chain

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
        step = random.choice(list(board.all_steps.difference(chain.from_iterable(board.done_steps.values()))))
        return step


class User(Player):

    def get_name(self, name):
        if name:
            return name
        return input("Как ваше имя?\n")

    def make_step(self, board) -> "tuple[int, int]":
        while True:
            step = input(f"Ход игрока {self.name}. Сделайте шаг: введите координаты через пробел\n").split(" ")
            try:
                step = int(step[0]), int(step[1])
                if step in board.all_steps.difference(chain.from_iterable(board.done_steps.values())):
                    return step
                print("Вы ввели занятую ячейку или ячейку вне игрового поля. Попробуйте еще раз.")
                continue
            except (IndexError, ValueError):
                print(f"Ошибка ввода. Введите два числа через пробел от 0 до {board.size-1}")


# b = Board(3)
# # p = User("x")
# #print(p.name)
# # p.make_step(b)
# p = Player("x")
# a = p.make_step(b)
# print(a)