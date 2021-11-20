from collections import defaultdict


class Board:

    # size - размер доски
    # содержимое таблица доски (матрица)
    # выбывшие ячейки в виде кортежей
    # Отображение доски
    # Принять ход
    # Проверка на матчинг

    # TODO: Создать класс реализующий доску для игры в крестики нолики
    # TODO: Метод установки шага на доску
    # TODO: Метод проверки что есть победитель
    # TODO: Метод печати доски на экран

    def __init__(self, size):
        self.size = size
        self.all_steps = set((n, m) for n in range(self.size) for m in range(self.size))
        self.done_steps = defaultdict(set)
        self.ttt_board = self._get_board()

    def _get_board(self):
        return [[0 for _ in range(int(self.size))] for i in range(int(self.size))]

    def print_board(self):
        first_line = '#' * 4 + f'{"#".join([str(i) for i in range(self.size)])}##'
        body_board = []
        for i, line in enumerate(self.ttt_board):
            str_line = "|".join([str(i) for i in line])
            temp = str(i) + "# " + str_line + " #\n"
            body_board.append(temp)
        last_line = "#" * (self.size * 2 + 4)
        print(first_line, "\n", *body_board, last_line)

    def add_step(self, step: "tuple[int, int]", user):
        self.done_steps[user.symbol].add(step)
        self.ttt_board[step[0]][step[1]] = user.symbol

    def check(self, user) -> bool:
        for itm in self.get_lines():
            if (not itm.difference(self.done_steps[user.symbol])):
                return True
        return False

    def get_lines(self):
        diagonals = (
            {(i, i) for i in range(self.size)},
            {(i, self.size - i - 1) for i in range(self.size)},
        )

        for itm in diagonals:
            yield itm

        horizontals_verticals = (
            ({(i, j) for i in range(self.size)} for j in range(self.size)),
            ({(i, j) for j in range(self.size)} for i in range(self.size)),
        )

        for itm in horizontals_verticals:
            yield from itm