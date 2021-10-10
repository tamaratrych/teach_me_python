"""
3 Даны 2 списка и список чисел, написать процедуру и распределить числа по спискам
числа четные должны попасть в список even, числа нечетные должны попасть в список odd
"""
numbers = [44, 22, 54, 87, 345, 912, 654, 18, 33, 76, 11]
even = []
odd = []
numbers = set(numbers)

all_numbers = [i for i in range(min(numbers), max(numbers)+1)]
even = all_numbers[all_numbers[0]%2::2]
even = set(even)
even = even & numbers

all_numbers = set(all_numbers)
odd = all_numbers - even
odd = set(odd)
odd = odd & numbers


print('четные числа из списка:', *even)
print('нечетные числа из списка:',*odd)