maze = [
    ["#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#"],
    ["#", " ", "#", "#", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", "#"],
    ["#", "#", "0", "#", "#", "#", "#"]
]

def print_maze(maze):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            print(maze[i][j], end=' ')
        print()

def find_exit(maze_in, x, y):
    maze_in[x][y] = 'E'
    cnt_moves = 0
        
    print('Добро пожаловать в игру "Лабиринт".')
    print('Игрок на карте обозначен буквой "Е".')
    print('Ваша цель покинуть лабиринт, зайдя на клетку "0".')
    print('Управление игроком производится путем ввода буквенных команд: ')
    print('"W" - перемещает игрока наверх.')
    print('"A" - перемещает игрока налево.')
    print('"S" - перемещает игрока вниз.')
    print('"D" - перемещает игрока вправо.')
    print('Если вы захотели выйти напишите "exit".')
    print('Программа не чувствительна к регистру')
    
    while True:
        print()
        print_maze(maze_in)
        player_move = input('Введите команду: ').lower()
        tmp = [x, y]
        
        # Обновление координат в зависимости от команды
        if player_move == 'w':
            tmp[0] -= 1
        elif player_move == 'a':
            tmp[1] -= 1
        elif player_move == 's':
            tmp[0] += 1
        elif player_move == 'd':
            tmp[1] += 1
        elif player_move == 'exit':
            print('Выключение программы. До встречи!')
            exit()
        else:
            print('Ошибка ввода. Несуществующая команда.')
            continue
        
        # Проверка на допустимость движения
        if maze_in[tmp[0]][tmp[1]] == ' ':
            cnt_moves += 1
            maze_in[x][y] = '-'
            x, y = tmp[0], tmp[1]
            maze_in[x][y] = 'E'
            print('Ход выполнен.')
            continue
        elif maze_in[tmp[0]][tmp[1]] == '-':
            cnt_moves += 1
            maze_in[x][y] = '-'
            x, y = tmp[0], tmp[1]
            maze_in[x][y] = 'E'
            print('Ход выполнен.')
            continue
        elif maze_in[tmp[0]][tmp[1]] == '#':
            print('Ход невозможен. Игрок уперся в стену.')
            continue
        elif maze_in[tmp[0]][tmp[1]] == '0':
            cnt_moves += 1
            print(f'Победа! Вы прошли лабиринт! Шагов сделано: {cnt_moves}.')
            exit()
        break

find_exit(maze, 3, 3)
