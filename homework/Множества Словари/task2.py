print('Добро пожаловать в реестр участников.')
print('Доступные команды: add, remove, list, exit.')

participants = {}

while True:
    user_input = input('Введите команду: ')

    if user_input == 'add':
        user_name = input('Введите через пробел имя и фамилию участника: ').strip().lower().title().split()
        hobbies_list = input('Введите через запятую список интересов: ').strip().split(', ')
        participants[tuple(user_name)] = hobbies_list
        print('Участник добавлен.')
        continue

    elif user_input == 'remove':
        user_input = input('Введите пользователя на удаление: ').split()
        print('Пользователь удален.')
        participants.pop(participants[tuple(user_input)])

    elif user_input == 'list':
        for names in participants:
            print(f'Участник {" ".join(names)}. Интересы: ", ".join(participants[names]).')
        print('Список участников выведен.')
        continue

    elif user_input == 'exit':
        print('Программа завершила работу')
        exit()
    break
