
# Флаг для тестов
test_flag = False

if test_flag:
    participants_1 = set('Иванов, Попов, Сидоров, Кузнецов'.strip().lower().title().split(', '))
    participants_2 = set('Петров, Иванов, Сидоров'.strip().lower().title().split(', '))
    participants_3 = set('Попов, Иванов, Соловьев'.strip().lower().title().split(', '))
else:
    participants_1 = set(input('Введите через запятую первый список участников: ').strip().lower().title().split(', '))
    participants_2 = set(input('Введите через запятую второй список участников: ').strip().lower().title().split(', '))
    participants_3 = set(input('Введите через запятую третий список участников: ').strip().lower().title().split(', '))

all_three = participants_1 & participants_2 & participants_3
min_one = (participants_1 - all_three).union((participants_2 - all_three).union(participants_3 - all_three))

only_two = (participants_1 & participants_2).union((participants_1 & participants_3).union(participants_2 & participants_3))
only_one = (participants_1 - only_two).union((participants_2 - only_two).union(participants_3 - only_two))
only_two = only_two - all_three


print('Во всех трех конкурсах участвовали: ')
print(*all_three, sep=', ')
print()
print('Минимум в одном конкурсе участвовали: ')
print(*min_one, sep=', ')
print()
print('Участвовали только в одном конкурсе: ')
print(*only_one, sep=', ')
print()
print('Участвовали только в двух конкурсах: ')
print(*only_two, sep=', ')
print()
