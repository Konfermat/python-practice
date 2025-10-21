from functools import wraps

# functools
# этот декоратор помогает сохранять метаданные
# __name__
# __doc__

def simple_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'вызов {func.__name__}')
        res = func(*args, **kwargs)
        print('end')
        return res
    return wrapper

@simple_decorator
def calc(a, b):
    '''сложение цисел'''
    return a + b

print(calc.__name__)

print(calc.__doc__)
print()

@simple_decorator
def hello(name):
    '''__doc__ вызывает этот коментарий'''
    return 'hello'

print(hello.__name__)
print(hello.__doc__)
