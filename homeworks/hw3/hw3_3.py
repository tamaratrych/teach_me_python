"""
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

user_input = input("Введите данные\n>>>").split()
user_words = list(enumerate(user_input, 1))

words_count = len(user_input)
n = 0
while n < words_count:
      #print(user_words[n][0], user_words[n][1][:10])
      print(f'{user_words[n][0]}: {user_words[n][1][:10]:^12}')
      n+=1