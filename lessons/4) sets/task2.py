# Первое сообщение: 384729
# Второе сообщение: 418305
# Общие символы: ['3', '4', '8']
# Уникальные для первой цивилизации: ['2', '7', '9']
# Весь известный алфавит: ['0', '1', '2', '3', '4', '5', '7', '8', '9'
from enum import unique

while True:
    msg1 = input('Введите первое сообщение: ')
    msg2= input('Введите второе сообщение: ')
    if msg1.isdigit() and msg2.isdigit():
        set1 = set(msg1)
        set2 = set(msg2)

        ob = sorted(list(set1 & set2))
        uniq = sorted(list(set1 - set2))
        all = sorted(list(set1 | set2))

        print(f'Общие символы: {ob}')
        print(f'Уникальные для первой цивилизации: {uniq}')
        print(f'Весь известный алфавит: {all}')
        break
    else:
        print('Ошибка ввода. ')
        continue

