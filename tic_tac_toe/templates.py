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
}

template_variants = {
    "game_type": lambda template, **kwargs: template.format(variants=MODE),
    "ask_step": lambda template, **kwargs: template.format(**kwargs),
    "new_game": lambda template, **kwargs: template.format(variants=AGREEMENT),
    "enter_name": lambda template, **kwargs: template.format(**kwargs),
}


def user_interface(template_name, **template_vars):
    if template_name in template_variants:
        ask_str = template_variants[template_name](interface_string[template_name], **template_vars)
        user_input = input(ask_str)
        return user_input
    else:
        print(interface_string[template_name])