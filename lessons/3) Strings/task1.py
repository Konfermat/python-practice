
password = input("Введите пароль: ")
errors = []

# длинна
if len(password) < 8:
    errors.append("пароль слишком короткий")
elif password == "exit":
    exit()

# Заглавная ли буква
has_upper = False
for char in password:
    if char.isupper():
        has_upper = True
        break
if not has_upper:
    errors.append("нет заглавной буквы")

# есть ли число
has_digit = False
for char in password:
    if char.isdigit():
        has_digit = True
        break
if not has_digit:
    errors.append("нет числа")

if " " in password:
    errors.append("недолжно быть пробелов")

if len(errors) > 0:
    for err in errors:
        print(f"Ошибка: {err}")
else:
    print("Пароль подходит")