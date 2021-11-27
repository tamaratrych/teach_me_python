# from tic_tac_toe import matrix_match
from board import create_board

"""
Test of a board
"""
def board_test():
    for size in range(3, 8):
        board = create_board()
        assert len(board) & 1 == 1, "Size of the board is an even number"
        assert (len(board) == len(min(board)) and len(min(board)) == len(max(board))), "Wrong size of the board"
        assert all([i for i in board]), "Not all elements - 0"


board_test()
print("Finish test")
# def test_matrix():
#     matrix_tests = (
#         (([1, 1, 1],
#           [0, 0, 0],
#           [0, 0, 0]), True),
#
#         (([0, 0, 0],
#           [1, 1, 1],
#           [0, 0, 0]), True),
#
#         (([0, 0, 0],
#           [0, 0, 0],
#           [2, 2, 2]), True),
#
#         (([0, 1, 2],
#           [0, 0, 1],
#           [1, 1, 2]), False),
#
#         (([1, 0, 0],
#           [1, 0, 0],
#           [1, 0, 0]), True),
#
#         (([0, 1, 0],
#           [0, 1, 0],
#           [0, 1, 0]), True),
#
#         (([0, 0, 2],
#           [0, 0, 2],
#           [0, 0, 2]), True),
#         (([2, 1, 2],
#           [0, 1, 2],
#           [0, 0, 1]), False),
#         (([1, 1, 2],
#           [0, 1, 2],
#           [0, 0, 1]), True),
#         (([2, 1, 1],
#           [0, 1, 2],
#           [1, 0, 1]), True),
#     )

#     for test in matrix_tests:
#         assert tic_tac_toe.matrix_match(test[0]) is test[1], test[0]
#
# test_matrix()

