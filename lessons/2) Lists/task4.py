products = ["яблоко", "банан", "хлеб", "молоко", "сыр"]
print("Игра про список продуктов")
cart = []
user_action = 0
actions = '''
    1) Показать список товаров
    2) Добавить товар в корзину
    3) Удалить товар из корзины
    4) Показать содержимое корзины
    5) Выйти из программы
'''
while True:
    print(actions)

    try:
        user_action = int(input("Выберите действие: "))
    except ValueError:
        print("Неправильный ввод!")
        continue

    if user_action == 1:
        print(*products)

    elif user_action == 2:
        try:
            user_action = int(input("Введите номер товара для добавления: "))
            cart.append(products[user_action-1])
            print(f"Товар {products[user_action-1]} добавлен")
            products.remove(products[user_action-1])
        except ValueError:
            print("Неправильный ввод!")

    elif user_action == 3:
        try:
            user_action = int(input("Введите номер товара для удаления: "))
            products.append(cart[user_action-1])
            print(f"Товар {cart[user_action-1]} удален")
            cart.remove(cart[user_action-1])
        except ValueError:
            print("Неправильный ввод!")

    elif user_action == 4:
        if len(cart) > 0:
            print('В вашей корзине:', *cart)
        else:
            print("Ваша корзина пустая.")

    elif user_action == 5:
        print("Пока! Пока!")
        exit()

    else:
        print("Неправильный ввод!")
        continue
