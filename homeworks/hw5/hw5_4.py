"""4
Функция принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без операторов ** * (без умножения и без возведения в степень).
Можно и нужно использовать сложение (+) и возможно деление (/)
"""

error_messages = (
    "Ошибка ввода. Функция возводит в степень только положительные числа",
    "Ошибка ввода. Показатель степени должен быть отрицательным целым числом",
)

def my_pow(x, y):
    if not str(x).replace('.', '', 1).isdigit() or int(x) == 0:
        return print(error_messages[0])
    if not (str(y)[0] == '-' and str(y).replace('-', '', 1).isdigit()) or int(y) == 0:
        return print(error_messages[1])
    delimiter = int(x)
    for itr in range(abs(int(y))-1):
        delimiter *= delimiter
    result = 1 / delimiter
    return result

result = my_pow('5', '-2')

print(result)
