# # декораторы
#
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('До вызова')
#         result = func(*args, **kwargs)
#         print('Что-то после вызова')
#         return result
#     return wrapper
#
# @my_decorator
# def hello(name):
#     # print('Исходная функция')
#     return f'Hello {name}'
#
# print(hello('Katen'))

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def hi():
    print('hi')

hi()