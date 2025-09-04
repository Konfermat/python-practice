# 5 2 8 2 5 9 1 8 8
ids = input("Введите ID через пробел: ").split()
ids = [int(x) for x in ids]

# уникальные
unique_ids = set(ids)
# .count() считает элементы
sus = [] # дубликаты
noSus = [] # уникальные

for x in unique_ids:
    count = ids.count(x)
    if count > 1:
        sus.append(x)
    else:
        noSus.append(x)
sus.sort()
noSus.sort(reverse=True)
print(f'Подозрительные: {sus}')
print(f'Надежные: {noSus}')
