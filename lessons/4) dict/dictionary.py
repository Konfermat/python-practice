# словари ключ значение
# dict1 = {}
# dict2 = dict()
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict1['apple'] = 'green'
# dict1['orange'] = 'orange'
# # ключи в словаре должные быть уникальными значения не обязательно
# print(*dict1)
# dict2 = {(1, 2): 'blue'}
#
# print(dict1.keys()) # возвращает список ключей
# print(dict1.values()) # возвращает список значений
# print(dict1.items()) # список элементов
#
# for k, v in dict1.items():
#     print(k)
#     print(v)
# t = (6, 7)
# k, v = t
# # подсказка по четвертому заданию из третьего урока
# # используй библиотеку string
# import string
# upper = string.ascii_uppercase
# lower = string.ascii_lowercase
# digits = string.digits
# special = string.punctuation
# # spec = '!@#$%^&*()'
# # добить остаточную длинну пароля ранд символами
# print(special)

# методы словарей

dict1 = {'a': 1, 'b': 2, 'c': 3}
# get значение по ключю
a = dict1.get('age', 'Такого нет')
print(a)
print(dict1)

# update можно разом дополнить несколько значений одним методом update
dict1.update({'age': 55, 'city': 'NSK'})
print(dict1)

# pop удаляет по ключу и возвращает значение
# Еслм ключ не существует то ошибка
# dict1.pop('age')
# age = dict1.pop('age')
# print(age)

# del удление полностью элемента ключ-значение но не возвращает его
del dict1['city']
print(dict1)

# кортеж не изменяемый список, итерируемый.
# создав кортеж с одним элементом можно (1,) а не (1)
# со списком [1] пойдет но лучше практиковать [1,]

tuple1 = (1, 5, 3, 4)
print(tuple1[0])
t2 = (7,)
t3 = 1, 2, 3, 4 # так можно но не нужно
print(t2)
print(t3)
#count()


