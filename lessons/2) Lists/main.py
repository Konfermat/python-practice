'''
# списки
list1 = []
# list2 = ()
list1.append(1)
list1.append(2)
list1.append(3)
list1.append(4)
list1.append(5)
list1.append(6)
list1.append(7)

print(list1)
print(list1[2])
# list1[2] = 5
print(list1)
#range(n, k, s)
# print(list1[1:3])
print(list1[1:6:2])
# print(list1[-1])
print(list1[-1:-5:-2])
print(list1[:5])
print(list1[::2])
print(list1[::-1])
print(list1)
# remove - удаление первого вхождение элемента
list1.remove(3)
print(list1)
# pop() удаление с конца по идексу или возвращение удаленного к переменной
p = list1.pop()
print(p, list1)

list2 = ['a', 'c', 'f']
list1.extend(list2)
print(list1, list2)
# sort() сортировка однородного списка
print(list2)
list2.sort()
print(list2)
'''

# reverse - перевернуть
#
nums = ['12', '23', '53', '41']
# join - объединение работает только со строками
# print(nums)
# print(', '.join(nums))
# # len()
# print(len(nums))

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix[1][1])

# перебор матрицы
# for n in matrix:
#     for m in n:
#         print(m)
#     # print(n)
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j])

fr = ['apple', 'banana', 'orange']
# for f in fr[:]: # итерация по копии
    # fr.remove(f)
    # if f == "banana":
    #     fr.remove(f)
