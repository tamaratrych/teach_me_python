from constants import MODE, AGREEMENT


interface_string = {
    "rules": "следуйте инструкциям и наслаждайтесь игрой",
    "hello": "Здравствуй игрок",
    "enter_name": "Введите свое имя\n>>>",
    "game_type": "С кем вы желаете играть\n{variants}\n>>>",
    "ask_step": "Ход #{step_number} игрока {name} ",
    "win": "Победил игрок {name} на ходу #{step_number}",
    "new_game": "Желаете начать новую игру? {variants} ",
    "draw": "Ничья победителей нет",
    "wrong_step": "Вы ввели занятую ячейку или ячейку вне игрового поля. Попытайтесь снова.",
    "wrong_input": "Ошибка ввода. Попытайтесь снова.",
    # "log_game": "Session #{number_current_session}. {extreme_point} game #{num_game} at {dt}\n",
    # "log_step": "Session #{number_current_session}; game #{num_game}; player's name {name}; player's step {step}\n"
}

template_variants = {
    "game_type": lambda template, **kwargs: template.format(variants=MODE),
    "ask_step": lambda template, **kwargs: template.format(**kwargs),
    "win": lambda template, **kwargs: template.format(**kwargs),
    "new_game": lambda template, **kwargs: template.format(variants=AGREEMENT),
    "enter_name": lambda template, **kwargs: template.format(**kwargs),
    # "log_game": lambda template, **kwargs: template.format(**kwargs),
    # "log_step": lambda template, **kwargs: template.format(**kwargs),
}


def user_interface(template_name, **template_vars):
    if template_name in template_variants:
        ask_str = template_variants[template_name](interface_string[template_name], **template_vars)
        user_input = input(ask_str)
        return user_input
    else:
        print(interface_string[template_name])