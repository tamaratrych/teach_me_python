import random

from globals import possible_steps
from templates import user_interface


def make_step(step_number, user, board):
    def get_step(step_number, user):
        while True:
            input_step = user_interface("ask_step", step_number=step_number, name=user["name"]).split(" ")
            try:
                new_step = tuple(int(input_step[0]), int(input_step[1]))
                return new_step
            except ValueError:
                user_interface("wrong_input")

    def check_stepable(new_step):
        while True:
            try:
                if new_step in possible_steps:
                    return new_step
            except ValueError:
                user_interface("wrong_step")

    new_step = get_step(step_number, user["name"])
    new_step = check_stepable(new_step)
    user["user_steps"].append(possible_steps.pop(new_step))
    board[new_step[0]][new_step[1]] = user["symbol"]


def comp_step(step_number, user, board):
    step = random.choice(possible_steps)
    board[step[0]][step[1]] = user["symbol"]
    user["user_steps"].append(possible_steps.pop(step))


user_step = {
    "user": make_step,
    "comp": comp_step
}