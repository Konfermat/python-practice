import time
from functools import wraps

class Timing:
    def __init__(self, log_file='time_log.txt', duration=0.5):
        self.log_file = log_file
        self.duration = duration

# args список **kwargs словарь # сначало обычные аргументы args потом **kwargs)
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            res = func(*args, **kwargs)
            end_time = time.time()
            dur = end_time - start_time
            warning_message = ''
            if dur > self.duration:
                warning_message = f'ВНИМАНИЕ! слишком долго; {dur}'

            print(f'Функция {func.__name__} выполнилась за {dur} секунд.')

            if warning_message:
                print(warning_message)
            print('-'*30)

            log_str = [
                f'Func: {func.__name__}',
                f'Duration: {dur}',
                # f'Warning message: {warning_message}.\n',
            ]
            if warning_message:
                log_str.append(warning_message)
            try:
                with open(self.log_file, 'a', encoding='utf-8') as f:
                    f.writelines(log_str)
            except IOError as e:
                f'Ошибка записи: {e}'

            return res
        return wrapper

@Timing()
def fast(n):
    print('начало')
    time.sleep(0.01)
    return n*2

@Timing(duration=0.2)
def slow(n):
    print('начало')
    time.sleep(n)
    return 'готово'

res1 = fast(10)
print(res1)

res2 = slow(1.5)
print(res2)

print(fast.__name__)
print(slow.__doc__)


# print(time.time())
# print(time.perf_counter())
# print(time.localtime(time.time()))

