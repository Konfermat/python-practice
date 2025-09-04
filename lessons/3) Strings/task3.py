# Привет мир, привет Python, привет код!
from enum import unique

user_input = input("Введите текст: ")
for ch in ".,!?":
    user_input = user_input.replace(ch, '')
user_input = user_input.lower().split()
words = user_input

unique_words = list(set(words))
unique_words_cnt = len(unique_words)
print(f'Разных слов: {unique_words_cnt}')
print(f'Уникальные слова: {sorted(unique_words)}')
