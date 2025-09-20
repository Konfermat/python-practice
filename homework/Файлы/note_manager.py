import os

while True:
    print('Доступные команды: add, list, read, delete, exit.')
    user_case = input('Введите команду: ')  
    
    if user_case == 'add':
        header = input('Введите заголовок заметки: ')
        text = input('Введите текст заметки: ')
        
        try:
            if not os.path.isdir('notes'):
                os.mkdir('notes')
        except Exception:
            print('Невозможно создать директорию для заметок.')
            continue

        with open(f'notes/{header}.txt', 'w', encoding='utf-8') as file:  
            file.write(text)
        print(f'Заметка "{header}" создана.')
        continue
        
    elif user_case == 'list':
        if not os.path.exists('notes'):  
            print('Нет доступных заметок.')
            continue
        elif os.listdir('notes') == []:
            print('Нет доступных заметок.')            
            continue
        for i in os.listdir('notes'):
            print(i[:-4])
        print('Список выведен.')
        continue
        
    elif user_case == 'read':
        user_case = input('Введите имя заметки для прочтения: ')
        try:
            with open(f'notes/{user_case}.txt', 'r', encoding='utf-8') as file:
                content = file.read()
            print(f'Содержимое заметки:\n{content}')  
        except FileNotFoundError:
            print(f'Заметка "{user_case}" не найдена.')
        continue
        
    elif user_case == 'delete':
        file_to_delete = input('Введите имя заметки для удаления: ')
        file_path = f'notes/{file_to_delete}.txt'  
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f'Заметка "{file_to_delete}" успешно удалена.')
            continue
        else:
            print(f"Заметки '{file_to_delete}' не существует.")
            continue
            
    elif user_case == 'exit':
        print('Программа выключена. До встречи!')
        exit()
    else:
        print('Ошибка ввода.')
        continue
