# def озночает define

# Функция без возвращаемого значения
def test_function():
    a = 1
    b = 2
    print(a + b)
test_function()

# Функция возвращаемого значения
def test_function1():
    a = 3
    b = 5
    return a + b
print(test_function1())

# Функция с обязательным аргументом
def test_function2(a, b = 9):
    return a + b
print(test_function2(1))

# Функция с переопределением
def test_function3(a):
    return a
def test_function3(a, b):
    return a + b

print(test_function3(1))
print(test_function3(2, 2))