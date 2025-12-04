# Threads (потоки)

# I/O-bound tasks
# CPU-bound tasks (численные расчеты)
import threading
import time

def print_num():
    for i in range(10):
        print(f'num {i}')
        time.sleep(0.5)

# thread = threading.Thread(target=print_num)
# thread.start()
# print('поток запущен')
# thread.join() # дожидается завершения
# print('поток завершен')

# Гонка данных condition()
counter = 0
def increment():
    lock = threading.Lock() # для синхронизации
    global counter
    for i in range(100000):
        with lock: # блокируем доступ к переменной контекстный менеджер?
            counter += 1
        # что происходит
        # чтение значения
        # увеличение значения на 1
        # запись нового значения
        # может где то друг с другом пересечься и результат будет не предсказуемым
        # спастись можно синхронизацией

# threads = [threading.Thread(target=increment) for _ in range(5)]
# for thread in threads:
#     thread.start()
# for thread in threads:
#     thread.join()
# результат может быть другим
# print(f'counter: {counter}') # 500000

# Синхронизация Lock

import queue
# класс Queue потокобезопасный
def worker(q):
    while not q.empty(): # пока в очереди есть задача
        task = q.get() # извлекаем задачу из очереди
        print(f'processing {task}')
        time.sleep(1) # митация выполнения задачи
        q.task_done() # сообщаем о выполнении задачи

q = queue.Queue()
for i in range(5):
    q.put(f'task {i}') # добавление в очередь

threads = [threading.Thread(target=worker, args=(q,)) for _ in range(3)]
for thread in threads:
    thread.start()
q.join() # блокируем основной поток пока очередь не опустеет
print('all done')

# GIL Global Interpretator Log

