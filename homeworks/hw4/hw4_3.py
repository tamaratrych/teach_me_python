"""
Имеется 2 кортежа с координатами Ферзя и Пешки на шахматной доске
Определить Бьет ли Ферзь пешку
координаты хранятся (x, y)
"""
messages = (
    'Ферзь бьет пешку',
    'Ферзь не бьет пешку'
)
queen = (1, 6)
pawn = (2, 6)

difference = []
if queen[0] == pawn[0] or queen[1] == pawn[1]:
    print(messages[0])
else:
    for x, y in zip(queen, pawn):
        difference.append(abs(x - y))
    print(messages[0]) if difference[0] == difference[1] else print(messages[1])

