def even_numbers(start, end):
    cnt = start
    while cnt <= end:
        if cnt % 2 == 0:
            yield cnt
        cnt += 1

for i in even_numbers(1, 15):
    print(i, end=' ')
print('')

for i in even_numbers(5, 12):
    print(i, end=' ')
print('')
