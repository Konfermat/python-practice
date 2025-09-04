bad_words = ["дурак", "глупый", "тупой"]
# Ты такой Дурак, но не тупой.

text = input("Введите текст: ")
words = text.split()
print(words)

for i in range(len(words)):
    word_clear = words[i].lower().strip(".,!@#$%^&?")
    if word_clear in bad_words:
        if word_clear in bad_words:
            words[i] = "*"*len(word_clear)

res = ''
for w in words:
    res += w + ' '
print(res.strip())



