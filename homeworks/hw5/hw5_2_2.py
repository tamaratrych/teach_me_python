"""2
Дан словарь с кодированием строк азбуки Морзе
2.1 Реализовать функцию кодирующую текст в морзе строку на вход которой подается строка текста, в ответ возвращается
строка закодированная азбукой морзе. В качестве разделителя морзе символов использовать пробел.
Пробел кодируется тоже как пробел
2.2 Реализовать функцию декодирующую морзе строку обратно в читаемый текст.
Обратите внимание что используется только символы латинского Алфавита в lower case.
При этом строка должна всегда начинаться с заглавной буквы
"""

MORSE = {'.-': 'a', '-...': 'b', '-.-.': 'c',
         '-..': 'd', '.': 'e', '..-.': 'f',
         '--.': 'g', '....': 'h', '..': 'i',
         '.---': 'j', '-.-': 'k', '.-..': 'l',
         '--': 'm', '-.': 'n', '---': 'o',
         '.--.': 'p', '--.-': 'q', '.-.': 'r',
         '...': 's', '-': 't', '..-': 'u',
         '...-': 'v', '.--': 'w', '-..-': 'x',
         '-.--': 'y', '--..': 'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
         }
my_morse = ".- -. -.--  - . -..- - "
my_str = 'b s dvd'

"""
morse_to_str - cтрока латиницей + цифры
- Входные данные: закодированная строка (тип str)
- Что делает функция: каждый сивмол переводит в латиницу, первый символ переводит в верхний регистр
- Выходные данные: закодированная строка (тип str)
"""
def str_to_morse(any_text, cipher_dict):
    result = ''
    for itm in any_text:
        if itm == ' ':
            result += itm
        else:
            for morse, symbol in cipher_dict.items():
                if itm == symbol:
                    result += morse
                    result += ' '
    return result

test_str = str_to_morse(my_str, MORSE)
print(test_str)


def str_to_morse2(any_text, cipher_dict):
    reverse_dict = dict(zip(cipher_dict.values(), cipher_dict.keys()))
    result = ''
    for symbol in any_text.lower():
        result += ' ' if symbol == ' ' else (reverse_dict[symbol] + ' ')
    return result

print(str_to_morse2(my_str, MORSE))

"""
morse_to_str -
- Входные данные: закодированная строка (тип str)
- Что делает функция: каждый сивмол переводит в латиницу, первый символ переводит в верхний регистр
- Выходные данные: раскодированная строка
"""
def morse_to_str(any_morse, cipher_dict):
    result = ''
    temp_list = any_morse.strip().split(' ')
    for symbol in temp_list:
        result += ' ' if symbol == '' else cipher_dict[symbol]
    result = str.capitalize(result)
    return result

print(morse_to_str(my_morse, MORSE))
print(morse_to_str(test_str, MORSE))