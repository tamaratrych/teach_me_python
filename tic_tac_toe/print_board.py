board = (
            ["X", "O", "X"],
            ["O", "O", "X"],
            ["X", "O", "O"]
        )



def print_board(board):
    print("#####1#2#3##")
    for i, line in enumerate(board, 1):
        str_line = "|".join(line)
        print(i, " #", str_line, "#")
    print("#"*(len(board)*2+6))

print_board(board)