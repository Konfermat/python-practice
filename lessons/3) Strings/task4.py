# ivan@mail.ru, petr123@gmail, test@yandex.com
emails = input("Введите через запятую список email адресов через запятую: ")
print(emails)

try:
    email_list = [em.strip() for em in emails.split(", ")]
    valid = []
    invalid = []

    for e in email_list:
        if "@" in e:
            parts = e.split("@")
            if len(parts) == 2 and '.' in parts[1]:
                valid.append(e)
            else:
                invalid.append(e)
        else:
            invalid.append(e)
    print(f'Корректные e-mail адреса: {valid}')
    print(f'Некорректные e-mail адреса: {invalid}')
except Exception as e:
    print(e)