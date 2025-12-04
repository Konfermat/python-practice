# # Process
# # GIL (global interpreter lock)
# from multiprocessing import Process
# import time
#
# def hey():
#     print('hello from process')
#     time.sleep(5)
#     print('process end')
#
# if __name__ == '__main__':
#     process = Process(target=hey)
#     process.start()
#     time.sleep(2)
#     if process.is_alive():
#         print('все еще работает, прерываем')
#         process.terminate()
#
#     process.join()
#     print('process *end*')
#
# # is_alive() - роверяет работает ли процесс в данный момент
# # terminate() - принудительно завешает
#
# # Queue FIFO (first in ,first out)
#
# from multiprocessing import Process, Queue
# import time
#
# def procedure(queue):
#     for i in range(5):
#         print(i)
#         queue.put(i)
#         time.sleep(1)
# def consumer(queue):
#     while True:
#         item = queue.get()
#         if item == 'DONE':
#             break
#         print(f'consumer {item}')
#
# if __name__ == '__main__':
#     queue = Queue()
#     p_process = Process(target=procedure, args=(queue,))
#     c_process = Process(target=consumer, args=(queue,))
#     p_process.start()
#     c_process.start()
#     p_process.join()
#     queue.put('DONE')
#     c_process.join()
#     print('done')
#
# # Pipe на основе связи между двумя процессами

from multiprocessing import Process, Pipe
import time

def sender(conn):
    for i in range(5):
        conn.send(i) # отправляем данные через канад
        time.sleep(1)

def receiver(conn):
    while True:
        data = conn.recv()
        if data == 'done':
            break
        print(f'получатель получил {data}')

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()

    s_p = Process(target=sender, args=(parent_conn,))
    r_p = Process(target=receiver, args=(child_conn,))
    s_p.start()
    r_p.start()
    s_p.join()
    parent_conn.send('done')
    r_p.join()
    print('end')
    