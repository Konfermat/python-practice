# Создайте программу, которая будет принимать на вход
# строку и выводить на экран все подстроки этой строки.

text = input("Введите текст: ").strip()

if len(text) == 0:
    print('Текст небыл введен.')
    exit()
elif len(text) == 1:
    for i in range(len(text)):
        print(text[i:len(text)])
    exit()

for i in range(len(text)):
    print(text[0:i])
for i in range(len(text)):
    print(text[i:len(text)])
