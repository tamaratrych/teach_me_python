import itertools
import datetime
#from itertools import cycle
import random
"""
Игра Крестики нолики
"""
"""
Правила игры:
Игровое поле 3х3
участвуют 2 игрока
игроки ходят поочереди
каждый игрок имеет индивидуальный символ который ставит на свободную ячейку игрового поля
Победитель определяется по следующим правилам:
символ игрока заполняет горизонталь, вертикаль или диагональ
возможный исход игры когда нет победителя
"""
# TODO: Играть с компуктером
# TODO: Игровое поле в виде Матрицы 3на3 не изменяемо.
# TODO: Ячейка игрового поля будет изменяться,
"""(
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
)"""
# TODO: Игрок Словарь - ТИП пользователя

# TODO: Управляющий игрой распорядитель

# TODO: Функция матчинга игрового поля на наличие победителя
# TODO: Определение возможности хода
# TODO: Функция Взаимодействия с пользователем на предмет хода
# TODO: Функция совершения хода записывает на игровое поле в ячейку самого пользователя

interface_string = {
    "rules": "следуйте инструкциям и наслаждайтесь игрой",
    "hello": "Здравствуй игрок",
    "enter_name": "Игрок #{user_number}: Введите свое имя",
    "game_type": "С кем вы желаете играть {variants}",
    "ask_step": "Ход #{step_number} игрока {name}",
    "win": "Победил игрок {name} на ходу #{step_number}",
    "new_game": "Желаете начать новую игру? {variants}",
    "draw": "Ничья победителей нет",
    "wrong_step": "Вы ввели занятую ячейку или ячейку вне игрового поля. Попытайтесь снова.",
    "comp_step": "ход компьютера {variants}"
}

template_variants = {
    "game_type": lambda template, **kwargs: template.format(variants=("U", "C")),
    "ask_step": lambda template, **kwargs: template.format(**kwargs),
    "win": lambda template, **kwargs: template.format(**kwargs),
    "new_game": lambda template, **kwargs: template.format(variants=("Y", "N")),
    "enter_name": lambda template, **kwargs: template.format(**kwargs),
    "comp_step": lambda  template, **kwargs: template.format(**kwargs)
}

game_type = {
    "U": lambda x: " ",
    "C": lambda x: " "
}


def user_interface(template_name, **template_vars):
    if template_name in template_variants:
        ask_str = template_variants[template_name](interface_string[template_name], **template_vars)
        user_input = input(ask_str)
        return user_input
    else:
        print(interface_string[template_name])


def matrix_match(board):
    def chek_line(line):
        line_set = set(line)
        if (0 not in line_set and len(line_set) == 1):
            raise ValueError("CHECK_LINE")
        return False

    board_len = len(board)
    diagonal = map(lambda idx: board[idx][idx], range(0, board_len))
    diagonal_invert = map(lambda idx: board[idx][board_len - idx - 1], range(board_len - 1, -1, -1))
    try:
        _ = any(map(chek_line, (diagonal, diagonal_invert)))
        for row, column in zip(board, zip(*board)):
            _ = any(map(chek_line, (row, column)))
    except ValueError as exc:
        if 'CHECK_LINE' in exc.args:
            return True
        else:
            raise exc
    return False

board = (
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
    )
board_lengh = len(board)

def game(users: list, board):
    # 1 должна циклично итерироваться по пользователям либо написать свой цикличный итератор либо найти его в itertools
    # Опрашивать пользователя на предмет хода
    # Проверяем возможность хода
    # Проверяем выйгрышный вариант
    # Либо поздравить с победой, либо обьявить Ничью

    def step_ability(x, y):
        if 0 <= x < board_lengh and 0 <= y < board_lengh and board[x][y] == 0:
            return True
        return False

    def chek_line(board):
        cells = []
        for line in board:
            cells.extend(line)
        cells = set(cells)
        if not any(cell == 0 for cell in cells):
            return True
        return False
    n = 1
    for user in itertools.cycle(users):
        for _ in itertools.cycle([1]):
            new_step = user_interface("ask_step", step_number=int(n), name=user).split(" ")
            x, y = int(new_step[0]), int(new_step[1])
            if step_ability(x, y):
                board[x][y] = user
                with open("ttt_log.txt", "a") as file:
                    file.write(f'{user} на ходу #{str(n)} сделал шаг {str(x)}, {str(y)}\n')
                break
            else:
                user_interface("wrong_step")
                continue
        if matrix_match(board):
            user_interface("win", name=user, step_number=int(n))
            with open("ttt_log.txt", "a") as file:
                file.write(f'{user} победил на ходу #{str(n)}\n')
            break
        if chek_line(board):
            user_interface("draw")
            with open("ttt_log.txt", "a") as file:
                file.write("Игра закончилась ничьей\n")
            break
        n += 0.5


def choose_type_game(user_names):
    user_interface("hello")
    name = user_interface("enter_name", user_number=1)
    user_names.append(name)
    game_type = user_interface("game_type")
    if game_type == "U":
        name = user_interface("enter_name", user_number=2)
        user_names.append(name)
    elif game_type == "C":
        user_names.append("computer")
    return game_type


def empty_cells(board):
    zero_cells = []
    for line in range(board_lengh):
        for colm in range(board_lengh):
            if board[line][colm] == 0:
                zero_cells.append((line, colm))
    return zero_cells


def comp_step(zero_cells):
    step = random.choice(zero_cells)
    board[step[0]][step[1]] = "computer"
    return step


def game_comp_usr(users, board):
    def step_ability(x, y):
        if 0 <= x < board_lengh and 0 <= y < board_lengh and board[x][y] == 0:
            return True
        return False

    def chek_line(board):
        cells = []
        for line in board:
            cells.extend(line)
        cells = set(cells)
        if not any(cell == 0 for cell in cells):
            return True
        return False

    n = 1
    for user in itertools.cycle(users):
        print(user)
        if user != "computer":
            for _ in itertools.cycle([1]):
                new_step = user_interface("ask_step", step_number=int(n), name=user).split(" ")
                x, y = int(new_step[0]), int(new_step[1])
                if step_ability(x, y):
                    board[x][y] = user
                    with open("ttt_log.txt", "a") as file:
                        file.write(f'{user} на ходу #{str(n)} сделал шаг {str(x)}, {str(y)}\n')
                    break
                else:
                    user_interface("wrong_step")
                    continue
        if user == "computer":
            zero_cells = empty_cells(board)
            cell = comp_step(zero_cells)
            user_interface("comp_step", variants=cell)
         #   print(interface_string["comp_step"].format(variants=cell))
        if matrix_match(board):
            user_interface("win", name=user, step_number=int(n))
            break
        if chek_line(board):
            user_interface("draw")
            break
        n += 0.5


def main():
    now = datetime.datetime.now()
    with open("ttt_log.txt", "w") as file:
        file.write(str(now))
        file.write("Начало игры\n")
    user_interface("rules")
    new_game = "Y"
    while new_game == "Y":
        user_names = []
        board = (
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        )
        game_type = choose_type_game(user_names)
        if game_type == "U":
            game(user_names, board)
        else:
            game_comp_usr(user_names, board)
        new_game = user_interface("new_game")
    now = datetime.datetime.now()
    with open("ttt_log.txt", "a") as file:
        file.write(str(now))
        file.write("Конец игры\n")


main()