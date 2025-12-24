import uuid
import time
import random
from threading import Thread
from multiprocessing import Process
import os
import asyncio

# strateges:
# for sync(regular) and threading
def busy_normal_task(ID):
    print(f'Обычная задача {ID} запущена.')
    time.sleep(random.uniform(0.5, 2.0))
    print(f'Обычная задача {ID} завершена.')    
    
async def busy_io_task(ID):
    print(f'Обычная задача {ID} запущена.')
    await asyncio.sleep(random.uniform(0.5, 2.0))
    print(f'Обычная задача {ID} завершена.')    

def fibonachi_normal_sum(ID):
    print(f'Программа подсчета суммы 30-ти чисел Фибоначи {ID} запущена.')
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    result = fibonacci(30)
    print(result)
    print(f'Программа подсчета суммы 30-ти чисел Фибоначи завершена.')
    
async def fibonachi_io_sum(ID):
    print(f'Программа подсчета суммы 30-ти чисел Фибоначи {ID} запущена.')
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    result = fibonacci(30)
    print(result)
    print(f'Программа подсчета суммы 30-ти чисел Фибоначи завершена.')

# perfomance   
def log_busy_regular_task(func, arg1, repeats):
    func_name = 'последовательное'
    
    start = time.perf_counter()
    print('='*70)
    print('РАБОТА НАБОРА ЗАДАЧ')
    for _ in range(repeats):
        func(arg1)
    end = time.perf_counter()
    print('='*70)
    
    return f'Метод исполнения: {func_name}, количество задач: {repeats}, затраченно времени: {end - start:.2f} сек.'
    
def log_busy_threading_task(func, arg1, repeats):
    func_name = 'паралельный тред стрим'
    start = time.perf_counter()
    print('='*70)
    print('РАБОТА НАБОРА ЗАДАЧ')
    threads = [Thread(target=func, args=(arg1, )) for _ in range(repeats)]
    for i in threads: i.start()
    for i in threads: i.join()
    
    end = time.perf_counter()
    print('='*70)
    
    return f'Метод исполнения: {func_name}, количество задач: {repeats}, затраченно времени: {end - start:.2f} сек.'

def log_busy_multiprocessing_task(func, arg1, repeats):
    func_name = 'паралельный процессорный стрим'
    
    start = time.perf_counter()
    print('='*70)
    print('РАБОТА НАБОРА ЗАДАЧ')
    processes = [Process(target=func, args=(arg1, )) for _ in range(repeats)]
    for i in processes: i.start()
    for i in processes: i.join()
    
    end = time.perf_counter()
    print('='*70)
    
    return f'Метод исполнения: {func_name}, количество задач: {repeats}, затраченно времени: {end - start:.2f} сек.'

async def log_busy_asyncio_task(func, arg1, repeats):
    func_name = 'асинхроный стрим'
    
    start = time.perf_counter()
    print('='*70)
    print('РАБОТА НАБОРА ЗАДАЧ')
    coorutine = [func(arg1) for _ in range(repeats)]
    await asyncio.gather(*coorutine)
    print('='*70)
    end = time.perf_counter()
    
    return f'Метод исполнения: {func_name}, количество задач: {repeats}, затраченно времени: {end - start:.2f} сек.'

if __name__ == '__main__':
    result = []
    result.append('\n')
    result.append('Результат вычесления симуляции:')
    result.append(log_busy_regular_task(busy_normal_task, os.getpid(), 10))
    result.append(log_busy_threading_task(busy_normal_task, os.getpid(), 10))
    result.append(log_busy_multiprocessing_task(busy_normal_task, os.getpid(), 10))
    result.append(asyncio.run(log_busy_asyncio_task(busy_io_task, os.getpid(), 10)))    
    result.append('\n')
    result.append('Результат вычесления счета суммы чисел Фибоначи:')
    result.append(log_busy_regular_task(fibonachi_normal_sum, os.getpid(), 10))
    result.append(log_busy_threading_task(fibonachi_normal_sum, os.getpid(), 10))
    result.append(log_busy_multiprocessing_task(fibonachi_normal_sum, os.getpid(), 10))
    result.append(asyncio.run(log_busy_asyncio_task(fibonachi_io_sum, os.getpid(), 10)))  
    
    for i in result:
        print(i)