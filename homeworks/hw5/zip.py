"""
zip-
Входные данные - итерируемые объекты
Что делает - соединяет в кортежи элементы входных данных по соответсвующему индексу
Выходные элементы новый итерируемый объект, каждый элемент которого (кортеж) состоит из соответствующих по индексу элементов входных объектов
"""

def my_zip(iter1, iter2):
    result = []
    next_tupple = []
    for i in range(min(len(iter1), len(iter2))):
        next_tupple.append(iter1[i])
        next_tupple.append(iter2[i])
        result.append(tuple(next_tupple))
        next_tupple = []
    return result

print(my_zip([1, 2, 3, 8, 9], [4, 5, 6, 7]))

# for i in zip([1, 2, 3, 8, 9], [4, 5, 6, 7]):
#     print(i)