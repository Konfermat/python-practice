from random import shuffle as sf
player_map = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "$"]
atempts = 0

sf(player_map)

print('Добро пожаловать в программу "Охота за сокровищами".')
print('За три попытки вам нужно угадать на  где лежит сокровище.')

while True and atempts < 3:
    try:
        answer = int(input('Выберите позицию от 1 до 10: '))
        if player_map[answer - 1] == "$":
            print("Поздравляем, вы нашли сокровище!")
            print("Программа завершена.")
            exit()
        elif player_map[answer - 1] == "0":
            atempts += 1
            print(f"Пусто. Попробуйте снова. Попыток потрачено: {atempts}")
            if (atempts == 3):
                print("Программа завершена. Попытки закончились.")
                exit()
            continue
        elif answer == (-1):
            print("Ошибка! Число не должно быть отрицательныем.")
            continue
    except ValueError:
        print("Ошибка введенных данных. Введите число.")
    except IndexError:
        print("Ошибка введенных данных. Введеное число больше 10 или меньше 1.")
