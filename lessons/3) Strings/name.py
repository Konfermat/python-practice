# # Списковое включение
# list1 = [1, 2, 3, 4]
#
# list1 = [x**2 for x in list1]
# list2 = [x**3 for x in range(10)]
# # [выражение for элемент in итерируемый объект if условие]
# print(list1)
# print(list2)

# list3 = ['3', '6', '8', '10']
# list3 = [int(x) for x in list3]
# print(list3)

# list4 = [x**2 for x in range(10) if x % 2 == 0]
# print(list4)
# pairs = [(x, y) for x in range(3) for y in range(3)]
# print(pairs)
# # это короче и проще с точки зрения отработки

# строки
# str1 = "1234567890"
# Будет ошибка
# str1[0] = "b"

# print(str1[0])
# print(str1[1:-2])
# print(str1[1:-2:2])
# print(str1[::-1])

# методы строк

# str2 = "hello, woRld!"
# print(str2.strip()) # удаление пробелов
# pos = str2.find('World') # поиск элементов (первое вхождение)
# # -1 если не найдено
# print(pos)
#
# print(str2.upper()) # в верхний регистр
# print(str2.lower()) # в нижний регистр
# print(str2.title()) # каждое слово с заглавной
# print(str2.capitalize()) # первый символ в строке
# str_to_list = str2.strip().split(", ")
# print(str_to_list)
# connect = ", ".join(str_to_list)
# print(connect)

# конкатенация строк
# "a" + 23 + "b" # выдаст ошибку TypeError. Только для строк.
# str4 = "a" + "b" + "c"
# print(str4)
# str5 = "a" * 3
# print(str5)
# # интерполяция строк
# print(f'{str5 * 3} = asdfasdf')

# print("HHHhhhh".isupper()) # возвращает булевое значение
# print("HHH".isupper())
# print("HHH...".isupper())
# isupper() islower() istitle() iscapitalize()
# print("Hello".isalpha())
# print("Hello World1234".isalpha())
# print("Приветик".isalpha())
# print(" ".isalpha())
# print()
# print("123".isdigit())
# print("1a23".isdigit())
# print("1,23".isdigit())
# print("1.23".isdigit())
# print(" ".isdigit())

# print("ggg666".isalnum()) # True если все цифры или буквы
# print("666".isalnum())
# print("asdfasd...".isalnum())
# print('123'.isdecimal()) # Если все десятичное число
# print('1?'.isdecimal())
# print('1.2'.isdecimal())
# print('IV'.isdecimal())

# # Множества
# set1 = {1, 5, 3, 4, 5, 6, 7}
# set2 = set()
# print(set1)

set3 = {1, 2, 3, 4}
set4 = {3, 4, 5, 6}
print(set3.union(set4)) # объединение
print(set3.intersection(set4)) # пересечение
print(set3.difference(set4)) # разность
print(set4.difference(set3)) # разность





