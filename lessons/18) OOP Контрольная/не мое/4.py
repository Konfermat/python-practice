import time
from functools import wraps


class LimitCalls:

    def __init__(self, max_calls, time_win=None):
        self.max_calls = max_calls
        self.time_win = time_win
        self.call_count = 0
        self.first_call_time = None
        self.window_start_time = None  # время начала текущего окна

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            cur_time = time.time()

            if self.time_win is not None:
                # если это первый вызов или окно истекло
                if (self.window_start_time is None or
                    cur_time - self.window_start_time > self.time_win):
                    self.call_count = 0
                    self.window_start_time = cur_time

            if self.call_count >= self.max_calls:
                if self.time_win:
                    err_msg = (f'превышено {self.max_calls} '
                               f'в течении {self.time_win} '
                               f'для {func.__name__}')
                else:
                    err_msg = (f'превышено {self.max_calls} '
                               f'для {func.__name__}')
                raise RuntimeError(err_msg)

            self.call_count += 1
            return func(*args, **kwargs)

        wrapper.reset_counter = self.reset_counter
        return wrapper

    def reset_counter(self):
        self.call_count = 0
        self.first_call_time = None
        self.window_start_time = None



@LimitCalls(3)
def greet(name):
    """просто функция приветствия"""
    return f'Hello, {name}!'


print("без временного окн")
for i in range(4):
    try:
        res = greet(i+1)
        print(f'вызов {i+1}: {res}')
    except RuntimeError as e:
        print(f'вызов {i+1}. ошибка {e}')

greet.reset_counter()
print("счетчик сброшен")

print("\nс временным окном")
@LimitCalls(max_calls=2, time_win=5)
def process(data):
    return f'обработка {data}'


for i in range(3):
    try:
        res = process(i+1)
        print(f'вызов {i+1}: {res}')
    except RuntimeError as e:
        print(f'вызов {i+1}. ошибка {e}')

print("ожидание 6 секунд")
time.sleep(6)

try:
    res = process('после ожидания')
    print(f'успех: {res}')
except RuntimeError as e:
    print(f'ошибка после ожидания: {e}')