import string

# Введите текст
text = input('Введите текст: ').split()
# Введите зарезервированные слова через пробел
reserved = input('Введите зарезервированные слова через пробел: ').lower().split()

for i in range(len(reserved)):
    for j in range(len(text)):
        tmp = text[j]
        if tmp[-1] in string.punctuation:
            if tmp[:-1].lower() == reserved[i].lower():
                text[j] = text[j].upper()
                # print(text[j])
        if text[j].lower() == reserved[i]:
            text[j] = text[j].upper()

# print(' '.join(text))

cnt = 0
for i in range(len(text)):
   if cnt <= 8:
       print(text[i], end=' ')
       cnt += 1
   else:
       print()
       cnt = 0
       print(text[i], end=' ')
