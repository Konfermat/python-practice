# lambda functions
# lambda параметр: выражение
# Пригодится при фугк сортировки, вычисления, в степень напиример

# sq = lambda x: x ** 2
# print(sq(9))

wrds = ['banana', 'apple', 'orange', 'lefruit']
sorted_wrds = sorted(wrds, key=lambda word: len(word))
print(sorted_wrds)

sorted_wrds = sorted(wrds, key=lambda word: word[-1])
print(sorted_wrds)

# спроси гпт
# индекс указывает какой соритровать элемент
touple1 = [(1, 5), (2, 3), (4, 1)]
print(touple1)
sort_touple1 = sorted(touple1, key=lambda tup: tup[1])
print(sort_touple1)

mul = lambda x, y: x * y
print(mul(2, 3))

