# import random     random.randint()
# from random import randint   randint()
from random import randint as r

lotto = []
while len(lotto) < 6:
    num = r(1, 20)
    if num not in lotto:
        lotto.append(num)

user_input = []
print('Введите число от 1 до 6: ')
i = 1
while len(user_input) < 6:
    try:
        n = int(input(f'Num {i}: '))
        if n < 1 or n > 20:
            print('диапозон чисел 1-20')
        else:
            user_input.append(n)
            i += 1
    except ValueError:
        print("error")


cnt = 0
for n in user_input:
    if n in lotto:
        cnt += 1
print(cnt)
if (cnt <= 1):
    print('Увы, не повезло')
elif (cnt <= 3):
    print("Неплохо!")
elif (cnt <= 5):
    print("Очень близко!")
else:
    print("Джекпот!")

# print(user_input)
# print(lotto)
# print(cnt)

