# Пример: Привет, мир! Мир прекрасен, привет всем.
# Введите текст: $$
# Результат:
# привет: 2
# мир: 2
# прекрасен: 1
# всем: 1

text = input('Введите текст: ').lower()

for char in '!@#$%^&*()?>,.{}[]':
    text = text.replace(char, '')
words = text.split()
count_words = {}

for word in words:
    if word in count_words:
        count_words[word] += 1
    else:
        count_words[word] = 1
print(count_words)
items = list(count_words.items())
n = len(items)
# [('a', 2), ('b', 1), ('c', 3)]
for i in range(n):
    for j in range(0, n-i-1):
        if items[j][1] < items[j+1][1]:
            # сравниваем соседние по количеству
            # меняем местами
            items[j], items[j+1] = items[j+1], items[j]

for word, count in items[:5]:
    print(f'{word}: {count}')
# print(items[0][1])
