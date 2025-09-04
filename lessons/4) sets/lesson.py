# все структуры данных являются итерируеммыми объектами но не упорядочными
# set3 = {1, 2, 3, 4}
# set4 = {3, 4, 5, 6}
# print(set3.union(set4)) # объединение
# print(set3.intersection(set4)) # пересечение
# print(set3.difference(set4)) # разность
# print(set4.difference(set3)) # разность
# print(set3.symmetric_difference(set4)) # симетричная разность
# print(set3 | set4) # union
# print(set3 & set4) # intersection
# print(set3 - set4) # difference
# print(set3 ^ set4) # symmetric_difference

# more sets

# a = {1, 2, 3, 4}
# a.add(5) # может добавится в любое место, но скорее всего в конец
# print(a)
# a.remove(2) # удаление
# print(a)
# # a.remove(12) # даст ошибку KeyError
# a.discard(12) # как remove но не даст ошибку при неправильном значении
# print(a) # вернет без изменений
# # a.clear() # очистит множество
# a_copy = a.copy()
# print(id(a))
# print(id(a_copy))
# # for i in a:
# #     a.add(9) # даст ошибку RuntimeError из за попытки изменения в итерации

b = {1, 2}
c = {1, 2, 3, 4, 5}
print(b.issubset(c)) # подмножество
print(c.issubset(b))
print(b <= c)
print(c <= b)
print(b.issuperset(c)) # надможество
print(c.issuperset(b))
print(b >= c)
print(c >= b)

d = {2, 1}
print(b == d) # равенство
# строки, числа, кортеж и другие не изменяемые типы данных могут работать в с методами множеств


