from datetime import datetime

name = "Василий"
surname = "Иванов"
age = 33
height = 182
birth_year = int(datetime.now().strftime('%Y')) - age
bio = name + ' ' + surname + ' ' + str(birth_year) + ' ростом ' + str(height) + 'см'
print(bio)