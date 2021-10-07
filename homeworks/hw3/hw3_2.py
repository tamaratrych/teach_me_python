"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
"""

months = {
    '1': 'зима',
    '2': 'зима',
    '3': 'весна',
    '4': 'весна',
    '5': 'весна',
    '6': 'лето',
    '7': 'лето',
    '8': 'лето',
    '9': 'осень',
    '10': 'осень',
    '11': 'осень',
    '12': 'зима',
}

check_month_number = tuple(months.keys())
print (check_month_number)

n=0
month_number = input('Введите число\n>>>')
while n < 4:
    if month_number in check_month_number:
        print(months[month_number])
        break
    else:
        month_number = input('Введите число от 1 до 12\n>>>')
        n +=1
else:
    print('Вы 5 раз ввели значение, не соответствующее номеру месяца')
