# Пример:
# Всего экспериментов: 5
# Введите номера проведенных экспериментов: 1 3 4 4 5
# Пропавший эксперимент: 2
# Дублированный эксперимент: 4

n = int(input("Всего экспериментов: "))
experiments = input("Номера экспериментов: ").split()
experiments = [int(x) for x in experiments]
planned = set(range(1, n+1)) # все
done = set(experiments) # реально проведенные
missing = planned - done
duplicates = []
for i in experiments:
    if i in experiments.count(i) > 1:
        duplicates.append(i)
        break

print(f'Пропавший: {missing}')
print(f'Дублированный: {set(duplicates)}')