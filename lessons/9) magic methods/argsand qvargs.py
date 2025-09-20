def test(*args):
    print(*args) # распаковка

test(1, 2, 3)
# args - неименованные, не резервированное слово(преобразуются в кортеж)
# kwargs
# init - конструктор, не резервированное слово

def sum_num(*args):
    res = 0 
    for m in args:
        res += m
    return res
print(sum_num(1, 2, 3))

def user_info(**kwargs):
    for k, v in kwargs.items():
        print(f'{k}: {v}')

user_info(name='Sasha', age=20, city='NSK')

# def func(simple_args, *args, simple_kwargs, **kwargs):