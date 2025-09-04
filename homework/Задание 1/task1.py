material_type = input("Введите тип учебного материала (книга/видео): ")
material_price = float(input("Введите стоимость материала: "))
category = input("Введите категорию материала: ")

if (material_price <= 0):
    print("Ошибка! Указанная стоимость не является положительным числом.")
else:
    print(f'Материал добавлен: Тип - {material_type}, Стоимость - {material_price}, Категория – {category}')
