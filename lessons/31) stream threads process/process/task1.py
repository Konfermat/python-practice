# Cоздать 3 процесса. Каждый из них будет вычислять квадрат
# числа от 1 до 3,
# передавать результаты в очередь,
# а затем главный процесс будет выводить
# эти результаты по мере их поступления.

from multiprocessing import Process, Queue
import time

def square(n, queue):
    res = n ** 2
    queue.put(res)
    time.sleep(1)

if __name__ == '__main__':
    queue = Queue()
    processes = []
    for i in range(1, 4):
        process = Process(target=square, args=(i, queue))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()

    while not queue.empty():
        res = queue.get()
        print(f'res = {res}')
    print(f'done')