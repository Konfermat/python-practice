import random
l1 = ["python", "list", "number", "orange"]
# c = random.choice(l1).split()
# s2 = 'asdf, fdas, mmds, asqwer'.split(', ')
# print(s2)
c = random.choice(l1) # рандомное слово
letters = [] # для ьукв слова
for i in c:
    letters.append(i)
random.shuffle(letters)
test = "".join(letters)

user_check = input(f" Слово: {test} Введите слово правильно: ")
print(test)
if user_check == c:
    print(f'Верно! это слово {c}')
else:
    print(f"Неправильно! Это слово {test}")
