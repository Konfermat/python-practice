# list1 = []
# # list2 = list()
# # append(добавление в конец)
# list1.append(5)
# list1.append(3)
# list1.append(7)
# list1.append(2)
# list1.append(5)
# list1.append(3)
# list1.append(7)
# list1.append(2)
# print(list1)
# print(list1[2])
# list1[2] = 5
# print(list1)
# # range(n, k, s)
# print(list1[1:6:2])
# print(list1[-1:-5:-2])
# print(list1[3::2])
# print(list1[::-1])
# # remove() -первое вхождение элемента
# list1.remove(3)
# print(list1)
# # pop() -удаление с конца (по индексу)
# # с возвращаемым значением
# p = list1.pop(4)
# print(p, list1)
#
# list2 = ['a', 'b', 'c']
# # extend - объединение
# list1.extend(list2)
# print(list1, list2)
# # sort - сортировка однородного списка
# list2.sort()
# print(list1, list2)
# # reverse - перевернуть
# list1.reverse()
#

nums = ['10', '20', '55', '32', '88']
# nums1 = [10, 20, 55]
# join - объединение (только строковые значения)
# print(', '.join(nums))
# # len()
# print(len(nums))
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix[1][1])

# for n in matrix:
#     for m in n:
#         print(m)
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j])
# Memory error
# num = []
# while True:
#     num.append(1)

# RuntimeError
fr = ['apple', 'banana', 'cherry']
for f in fr[:]: #итерация по копии
    if f =='banana':
        fr.remove(f)


# IndexError
if len(fr) > 3:
    print(fr[3])
else:
    print('вне диапозона')