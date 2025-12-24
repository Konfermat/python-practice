import time
import threading

users = [('Diana', 4), ('Agent 47', 3), ('That red guy', 2), ('Triad boss', 5)]

def send_notification(name, delay):
    print(f'Начинаю отправку уведомления для {name}...')
    time.sleep(delay)
    print(f'Уведомление для {name} отправлено!')
    
def thread_maker():
    threads = [threading.Thread(target=send_notification, args=(name, delay,)) for name, delay in users]
    
    for i in threads:
        i.start()
    for i in threads:
        i.join()

thread_maker()
#red agent diana triad