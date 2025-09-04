# есть два способа работы с файлами

# open
# file = open('text.text')
# закрывате файлы это безапаснее и стабильнее
# file.close()

# with сам закрывает
# режимы открытия 'r'-чтение(только чтение)
# ('имя файла.txt', 'режим', 'кодировка') as псевдоним
# as это "элиапс"
# with open('book.txt', 'r', encoding='utf-8') as f:
#     # r - ошибка sесли не найден
#     # w - перезапись - создаст если нету файла
#     # a - дозаписть - он тоже
#     # rb, wb, ab - бинарный
# #     content = f.read()
# # print(content)
#
#     # удалит пробелы в конце и в начале
#     # for line in f:
#     #     print(line.strip())
#
#     # # выведет первую строку
#     # print(f.readline())
#     # # выведет символы
#     # print(f.readline(10))
#
#     # выведет текст ввиде списка
#     print(f.readlines())

with open('text.txt', 'w', encoding='utf=8') as f:
    # перезаписывает файл
    # через 'a' он будет дополнять
    f.write('hello\n')
    f.write('world')
