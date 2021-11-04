import random

from templates import user_interface


def make_step(step_number, user, board, possible_steps):
    """
    This function asks the user a step, checks if the user can make this step
    """
    def get_step(step_number, user):
        while True:
            input_step = user_interface("ask_step", step_number=step_number, name=user["name"]).split(" ")
            try:
                new_step = tuple(map(lambda x:int(x), input_step))
                return new_step
            except (ValueError, IndexError):
                user_interface("wrong_input")

    def check_stepable(new_step):
        if new_step in possible_steps:
            return new_step
        user_interface("wrong_step")

    flag = True
    while flag:
        new_step = get_step(step_number, user)
        if check_stepable(new_step) == new_step:
            user["user_steps"].append(possible_steps.pop(possible_steps.index(new_step)))
            board[new_step[0]][new_step[1]] = user["symbol"]
            flag = False


def comp_step(step_number, user, board, possible_steps):
    """
    This function makes random step for the computer
    """
    step = random.choice(possible_steps)
    board[step[0]][step[1]] = user["symbol"]
    user["user_steps"].append(possible_steps.pop(possible_steps.index(step)))


user_step = {
    "user": make_step,
    "comp": comp_step
}
