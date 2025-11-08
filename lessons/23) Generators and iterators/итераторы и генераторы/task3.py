def multiples(limit, divisior):
    for n in range(1, limit+1):
        if n % divisior == 0:
            yield n
limit = int(input('верхний предел: '))
divisor = int(input('делитель: '))
for m in multiples(limit, divisor):
    print(m)


