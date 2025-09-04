print("Добро пожаловать в программу по учету времени учебы за неделю.")
hoursInTotal = 0
while True:
    try:
        days = int(input("Введите количество учебных дней для подсчета: "))
        if days < 0:
            print("Ошибка ввода. Количество дней должно быть положительным.")
            continue
        elif days > 7:
            print("Ошибка ввода. Число должно быть не больше семи.")
            continue
    except ValueError:
        print(" Ошибка ввода. Нужно ввести число.")
        continue

    cnt = 0
    while not cnt == days:
        try:
            tmp = int(input(f"Введите количество часов проведенных за {cnt+1} день: "))
            if tmp > 24:
                print("Ошибка ввода. Вы не могли учится больше 24 часов в этот день.")
                continue
            elif tmp < 0:
                print("Ошибка ввода. Количество часов должно быть положительным.")
                continue
            else:
                hoursInTotal += tmp
        except ValueError:
            print("Ошибка ввода. Нужно ввести число.")
            continue
        cnt += 1
    break
print(f"Количество часов проведенных за учебой равно: {hoursInTotal}")

