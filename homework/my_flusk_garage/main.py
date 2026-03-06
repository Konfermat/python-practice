
def decorator(func):
    def wrapper():
        print('hello before function call')
        func()
        print('hello after function call')
    return wrapper

@decorator
def intro():
    print('my name is Pedro')

# intro()

def decorator_name(func):
    def wrapper(*args, **kwargs):
        print('Before')
        result = func(*args, **kwargs)
        print('After')
        return result
    return wrapper

@decorator_name
def math_addition(a, b):
    print(a + b)

# math_addition(60, 7)


