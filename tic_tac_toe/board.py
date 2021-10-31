from constants import SIZE_BOARD


def create_board(size=SIZE_BOARD):
    """
    This function creates a square matrix filled with 0.
    The size is specified in a constant
    (the size of the matrix is an odd number)
    """
    # if size & 1:
        # with open("ttt_log.txt", "a") as file:
        #     file.write("The size of the board is an even number\n")
    return [[0 for _ in range(size)] for i in range(size)]


def print_board(board):
    """
    This function displays a board with zeros and crosses (player moves)
    """
    print('#'*4 + f'{"#".join([str(i) for i in range(SIZE_BOARD)])}##')
    for i, line in enumerate(board):
        str_line = "|".join([str(i) for i in line])
        print(i, "#", str_line, "#")
    print("#"*(len(board)*2+5))


def check_victory(board):
    """
    This function return True if any diagonal, row or column contains one symbol ("X" or "O")
    """
    def chek_line(line):
        line_set = set(line)
        if (0 not in line_set and len(line_set) == 1):
            raise ValueError("CHECK_LINE")
        return False

    diagonal = map(lambda idx: board[idx][idx], range(0, SIZE_BOARD))
    diagonal_invert = map(lambda idx: board[idx][SIZE_BOARD - idx - 1], range(0, SIZE_BOARD))
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


