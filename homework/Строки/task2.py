math = input('Введите арифметическое выражение без пробелов(число операция число): ')

operation = ['+', '-', '*', '/']
exact = [opr for opr in math if opr in operation]
try:
    exact = str(exact[0])
except IndexError:
    print('Ошибка. Введенный оператор неизвестен или введен неправильно.')
    exit()
math = math.split(exact)
try:
    math = [float(x) for x in math]
except ValueError:
    print('Ошибка. Число указанно неверно.')
    exit()

try:
    for _ in range(len(operation)):
        if exact == '+':
            print('%.2f' % (math[0] + math[1]))
            exit()
        elif exact == '-':
            print('%.2f' % (math[0] - math[1]))
            exit()
        elif exact == '*':
            print('%.2f' % (math[0] * math[1]))
            exit()
        elif exact == '/':
            print('%.2f' % (math[0] / math[1]))
            exit()
except ZeroDivisionError:
    print('Ошибка. Деление на ноль запрещено.')
    exit()

