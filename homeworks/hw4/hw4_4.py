# Дано 2 целых числа, написать алгоритм поиска наибольшего общего делителя

numbers = list(input("Введите два числа через пробел\n>>>").split())

max_number = int(max(numbers))
min_number = int(min(numbers))

while min_number:
    x = max_number // min_number
    result = min_number
    min_number = max_number % min_number
    #print(max_number) # если ввести 140 0 96, по принтуется: 96 140 96 44 8 (Я ожидала 140 96 44 8)
    #max_number = (max_number - min_number) / x # почему здесь деление на 0?
    max_number = result
else:
    print(result)
