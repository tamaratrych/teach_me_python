def main():
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
