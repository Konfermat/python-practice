print("Добро пожаловать в программу списка задач")
task_list = []
while True:
    print("Список доступных команд: add, remove, list, exit")
    user_input = input("Введите команду: ")
    if user_input == "add":
        task_list.append(input("Введите задачу: "))
        continue
    elif user_input == "remove":
        try:
            if task_list == []:
                print("Удаление невозможно. Список пуст.")
                continue
            else:
                task_list.pop(int(input("Введите индекс элемента списка на удаление: ")) - 1)
                continue
        except ValueError:
            print("Ошибка ввода. Нужно ввести числовой индекс.")
            continue
        except IndexError:
            print("Ошибка ввода. Индекс не найден.")
            continue
    elif user_input == "list":
        if task_list == []:
            print("Ваш список пуст.")
            continue
        else:
            for i in range(len(task_list)):
                print(f'{i + 1}. {task_list[i]}')
            continue
    elif user_input == "exit":
        exit()
    else:
        print("Ошибка ввода. Команда введена неправильно.")
        continue
    break