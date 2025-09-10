from random import randint, shuffle
print('Добро пожаловать в программу генерации пароля')
print('Длинна сгенерированного пароля возможна от 8 до 100 символов включительно.')

try:
    num = int(input('Введите длинну пароля: '))
    if num > 100:
        print('Ошибка. Число должно быть не больше 100.')
        exit()
    elif num < 8:
        print('Ошибка. Чмсло должно быть не меньше 8.')
        exit()
except ValueError:
    print('Ошибка. Число введено неправильно.')
    exit()

try:
    reminder = num - 4
except IndentationError:
    print('Ошибка! Ввод был пуст.')
    exit()

# создаем список списков который содержит нужные для пароля символы
characters_matrix = [[chr(ch) for ch in range(97, 123)], [chr(ch) for ch in range(65, 91)], [chr(ch) for ch in range(33, 48)], [str(ch) for ch in range(10)]]

result = []

# генерируем первые 4 числа
for i in range(4):
    result.append(characters_matrix[i][randint(0, len(characters_matrix[i]) - 1)])
print(result)
# генерируем остаток
for i in range(reminder):
    rnd = randint(0, 3)
    result.append(characters_matrix[rnd][randint(0, len(characters_matrix[rnd])-1)])

print(f'Ваш пароль из {num} символов готов: {''.join(result)}')
    