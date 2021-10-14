"""
Дано 2 Матрицы
Необходимо получить произведение данных матриц
"""

matrix1 = [[5, 3], [1, 7], [4,2]] # matrix m x n
matrix2 = [[2, 0, 6, 7, 3, 9], [4, 2, 8, 3, 6, 4]] # matrix n x k

m = len(matrix1)
print(m)
n = len(matrix1[0])
k = len(matrix2[0])

new_matrix = [[0]*k]*m
print(new_matrix)
for i in range(m):
    for j in range(n):
        for l in range(k):
            new_matrix[i][k] += matrix1[i][j] * matrix2[j][k]
        #row.append(a)
 #   new_matrix.append(row)

print(new_matrix)

