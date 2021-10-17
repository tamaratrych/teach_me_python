"""
range -
Входные данные - начало нумерации (по умолчанию 0), окончание нумерации и шаг нумерации (по умолчанию 1)
Что делает: выдает порядковые числа от старта до окончания с указанным шагом
Выходные данные - последовательность чисел
"""

def my_range(stop, start=0, step=1):
    if step <= 0 or start > stop:
        print("Неверные параметры")
    else:
        iter = start
        while iter < stop:
            print(iter)
            iter += step

my_range(10, 5, 2)

# for i in range(1):
#     print(i)

