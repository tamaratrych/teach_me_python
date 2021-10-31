""" 3
На вход функции подается строка, вернуть булевое является эта строка полиндромом или нет
проверочная строка "Пал, а норов худ и дух ворона лап."
Полиндром это строка которая читается в обе стороны одинаково, при этом знаки препинания числа и непечатные символы
игнорируются
"""

some_str = "Пал, а норов худ и дух ворона лап."


def check_palindrome(input_str):
    temp_list = [i for i in input_str.lower() if i.isalpha()]
    for i in range(len(temp_list)//2):
        if not (temp_list[i] == temp_list[(-1-i)]):
            return False
    return True

print(check_palindrome(some_str))


"""
1. Получить список из буквенных символов (для проверки символа используется функция isalpha().
При этом предварительно входную строку перевести в нижний регистр, чтобы нивелировать разницу заглавных и строчных букв.
2. Проверить список посимвольно: сравнивать с двух концов, двигаясь навстречу.
Середину списка определить длиной списка деленной нацело на 2 (если нечетное число,
то средний символ будет ровно посередине и никак не повлияет на решение, полиндром ли это.
3. Двигаясь от начала списка к середине, увеличивается индекс элемента списка, т.е. мы берем элемент temp_list[i].
Двигаясь с конца списка к середине, уменьшается индекс элемента списка, т.к. последний индекс списка -1, 
то нужно его и уменьшать на каждой итерации: мы берем элемент -1-i.
4. При первом же несовпадении равностоящих от концов списка букв, возвращается False,и функция завершает работу.
Если пройдем полный цикл и все проверяемые пары элементов равны между собой, то входная строка - полиндром,
и функция вернет True.
"""