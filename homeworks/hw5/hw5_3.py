"""3
Реализовать функцию my_func(),
которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

def my_func(a, b, c):
    temp_list = [a, b, c]
    temp_list.sort(reverse=1)
    _ = temp_list.pop()
    print(sum(temp_list))

my_func(-2, 554, 0)