"""
Дано 2 Матрицы
Необходимо получить произведение данных матриц
"""

matrix1 = [[5, 3], [1, 7], [4,2]] # matrix m x n
matrix2 = [[2, 0, 6, 7, 3, 9], [4, 2, 8, 3, 6, 4]] # matrix n x k

element = 0
new_matrix = []
for row in matrix1:
    rows = []
    for column in zip(*matrix2):
        for element1, element2 in zip(row, column):
            element += element1 * element2
        rows.append(element)
        element = 0
    new_matrix.append(rows)

print(new_matrix)
