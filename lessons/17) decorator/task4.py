import time
from functools import wraps

class LimitCalls:
    def __init__(self, max_calls=5, time_win=None):
        self.max_calls = max_calls
        self.time_win = time_win
        self.call_count = 0
        self.first_call_time = None


    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            cur_time = time.time()

            if (self.first_call_time is None and
            self.time_win is not None):
                self.first_call_time = cur_time

            if (self.time_win is not None and
            self.first_call_time is not None and
            cur_time - self.first_call_time > self.time_win):
                self.call_count = 0
                cur_time = self.first_call_time
                self.first_call_time = None

            if self.call_count >= self.max_calls:
                if self.time_win:
                    err_msg = f'превышено {self.max_calls} в течении {self.time_win} для {func.__name__}'
                else:
                    err_msg = f'превышено {self.max_calls} для {func.__name__}'
                raise RuntimeError(err_msg)

            self.call_count += 1
            return func(*args, **kwargs)
        wrapper.reset_counter = self.reset_counter
        return wrapper

    def reset_counter(self):
        self.call_count = 0
        self.first_call_time = None

@LimitCalls(3)
def greet(name):
    '''Простая функция'''
    return f'Hello {name}!'

for i in range(4):
    try:
        res = greet(i+1)
        print(f'вызов {i+1}')
    except RuntimeError as e:
        print(f'вызов {i+1}. ошибка {e}')

greet.reset_counter()

@LimitCalls(max_calls=2, time_win=5)
def process(data):
    return f'обработка {data}'

for i in range(3):
    try:
        res = process(i+1)
        print(f'вызов {i+1}')
    except RuntimeError as e:
        print(f'вызов {i+1}. ошибка {e}')

time.sleep(6)
try:
    res = process('после ожидания')
    print(f'{res}')
except RuntimeError as e:
    print(f'ошибка {e}')

