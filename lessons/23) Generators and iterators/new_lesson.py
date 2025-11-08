# # iter() объект для перебора итерируемого объекта
#
# numbers = [1, 2, 3]
# iterator = iter(numbers)
# # while True:
# #     try:
# #         print(next(iterator)) # 1
# #     except StopIteration:
# #         break
# # print(next(iterator)) # 4 Stop iteration ошибка
# # такой же как for i in range(12): делает тоже самое
#
# with open('f.txt', 'r', encoding='utf-8') as file:
#     iterator = iter(file)
#     for _ in range(10):
#         print(next(iterator).strip())

# генераторы yield (уайлд) это уже функция
# def generator():
#     # замораживает состояния памяти
#     # для ручного управления состояния
#     # полезность в быстроте
#     # при работе с бесконечными последовательностями
#     yield 1
#     yield 2
#     yield 3
#
#     gen = generator()
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))

# простой пример
# def count_up_to(limit):
#     count = 1
#     while count <= limit:
#         yield count
#         count += 1
#     for n in count_up_to(5):
#         print(n)

# пример для наглядности эффективности
# списковое включение

# import sys
# num_list = [x**2 for x in range(1000)] # списковое включение
# # способ экономного создания
# num_gen = (x**2 for x in range(1000)) # генераторное выражение
#
# # генератор словаря
# sq_dict = {x: x**2 for x in range(5)}
# # генератор множества
# sq_set = {x**2 for x in range(5)}
#
# print(f'размер списка: {sys.getsizeof(num_list)} байт ')
# print(f'размер генератора: {sys.getsizeof(num_gen)} байт ')
# print(f'размер словаря: {sys.getsizeof(sq_dict)} байт ')
# print(f'размер множества: {sys.getsizeof(sq_set)} байт ')

# def read_file(filename):
#     with open(filename, 'r', encoding='utf-8') as file:
#         for line in file:
#             yield line.strip()
#
# for line in read_file('log.txt'):
#     print(line)

# истощение генератора
# если ген попадает в генерацию то он истощается
gen = (x for x in range(3))
# ген можно сохранить
tmp = gen
print(sum(tmp)) # 3
print(list(gen)) # [] генератор истощен

print(sum(gen)) # 3
print(list(gen)) # [] генератор истощен
gen = (x for x in range(3))
print(list(gen)) # [0, 1, 2]
print(list(gen)) # [] генератор истощен
