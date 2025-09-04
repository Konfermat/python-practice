# x = 10  # int
# y = 3.5  # float
# t = True  # bool
# f = False  # bool
# s = 'Stroka'  # str
# l = [1, 4, True, 'str']  # list
# tup = (4, 2, 1)  # tuple
# se = {5, 6, 8}  # set
# di = {'a': 1, 'b': 2, 'c': 3}  # dict not ordered

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(type(name))
# print(type(age))
# Ctrl + Alt + L = Format your code

# if age > 18:
#     print("You are old.")
# elif age >= 0 and age <= 18:
#     print("You are too young.")
# else:
#     print("Invalid age.")
# print(f'You are {age} years old.')


# && || !
# and or not

# + - / * ** // %

# print(5 // 2) # 2
# print(9 // 4) # 2
# print(7 % 2) # 1
# print(6 % 9) # 6

# login = 'Seal_al'
# password = '1234'
# user_login = input('Enter your login: ')
# if login == user_login:
#     user_pass = input('Enter your password: ')
#     if password == user_pass:
#         print('Login is successful')
#     else:
#         print('Password is incorrect')
# else:
#     print('Login is incorrect')

'''
Ситуация: мы создаем простое интерактивное приложение, которое
позволяет пользователю ввести номер своей скидочной карты и
размер скидки.

Задача: написать программу, которая позволяет пользователю ввести
номер своей скидочной карты и размер скидки, а затем проверяет
корректность размера скидки.

Задача 3: напишите программу, которая позволяет вводить
пользователю сумму покупки и возраст. Если сумма покупки
превышает 100 долларов, предоставляется скидка 10%.
Дополнительно, если покупатель старше 65 лет, он получает
дополнительную скидку 5%.
'''
from subprocess import check_output

'''
# Решение
amount = float(input('Введите сумму покупки: '))
age = int(input('Введите возраст: '))
discount = 0
if amount > 100:
    discount += 10

if age > 65:
    discount += 5;

final_price = amount * (1 - discount / 100)
if discount == 0:
    print('Скидки нет.')
else:
    print(f'Общая скидка: {discount}\nСумма:{final_price:.2f} ')
'''

'''
Циклы
'''
# for i in range(10):
#     print(i)
#
# for _ in range(10):
#     print("Hello")

'''
range(n)
range(n, k)
range(n, k, step)
n - начало диапазона (0)
k - конец диапазона не включая значение
step - шаг (1)
for i in range(10):
print(i)
'''

'''
# строка не изменяемый тип данных
a = 'hello'
print(id(a))
b = 'hello'
print(id(b))
a = 'hello!'
print(id(a))
'''

# цикл for
# строка упорядочный тип данных
# str1 = "10"
# str1 = "asdfzxcv"
# for char in str1:
#     print(char, end='')

# str2 = "asdfzxcv"
# for ch in range(len(str2)):
#     print(f'{ch}: {str2[ch]}')

# цикл while
'''
message = "Mr. Bones! I want to get off your wild ride!"
count = 1
while count < 10:
    count += 1
    print(count, message)
'''
'''
count = 0
while count < 20:
    print(count)
    if count == 5:
        break
    count += 1
'''
'''
count = 0
while count < 20:
    if count == 2 or count == 10 or count == 15:
        count += 1
        continue
    print(count)
    count += 1
'''

# Исключения
'''
ValueError, FileNotFoundError, TypeError, ZeroDivisionError. ...
'''

# Исключения
# try:
#     print(10 / 0)
# except BaseException as e:
#     print(e)
# Пробуй за интерпретатором через BaseException искать исключения
'''
try:
    n = input()
    print(10 / n)
except ZeroDivisionError:
    print("Делить на 0 нельзя")
except KeyboardInterrupt:
    print("Введите значение")
except ValueError:
    print("Введите значение")
'''

'''
Задача 3: разработайте программу для подсчета среднего количества
товаров, поступивших на склад за указанное количество дней.
Программа должна сначала запрашивать у пользователя количество
дней для анализа. Затем для каждого дня должна запрашиваться
количество товаров, поступивших на склад. В конце программа должна
вывести среднее количество товаров, поступивших за день. Если ввод
данных некорректен (например, введено отрицательное число дней
или товаров, или нечисловое значение), программа должна сообщать
об ошибке и предлагать повторный ввод.
'''

while True:
    try:
        days = int(input('Введите кол-во дней: '))
        if days <= 0:
            print('Ввелите положительное число')
            continue
        break
    except ValueError:
        print("Введите целое число")

total_goods = 0
for i in range(days + 1):
    while True:
        try:
            goods = int(input(f'Кол-во товаров за день {i}:'))
            if goods < 0:
                print('введите положительное число')
                continue
            total_goods += goods
            break
        except ValueError:
            print('введите число')
avg = total_goods / days
print(f'AVG товара за день: {avg:.2f}')