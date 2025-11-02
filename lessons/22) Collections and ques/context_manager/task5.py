import random
import time
class ConnectionError(Exception):
    pass

class ApiConnectionRetry:
    def __init__(self, max_attempts=3):
        self.max_attempts = max_attempts
        self.connection = None #объект соединение если установленно

    # с вероятностью 70% выдает ошибку
    # random.random() float [0.0, 1.0])
    def attempt_connection(self):
        if random.random() < 0.7:
            raise ConnectionError('сбой соединениея с API')
        return 'API connected successfully'

    def __enter__(self):
        attempts = 0
        while attempts < self.max_attempts:
            attempts += 1
            print(f'попытка соединения: {attempts}...')
            try:
                self.connection = self.attempt_connection()
                print('соединение успешно установлено')
                return self.connection
            except ConnectionError as e:
                print(f'не удалось соединиться: {e}')
                if attempts < self.max_attempts:
                    wait_time = random.uniform(0.5, 1.5)#случайное значение
                    print(f'ожидание {wait_time:.2f} сек')
                    time.sleep(wait_time)
                else:
                    print('попытки исчерпаны')
                    raise #повторно выбросит последнее исключение
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            print('соединение закрыто')
            self.connection = None
        return False

print('Сценарий 1')
try:
    with ApiConnectionRetry(max_attempts=5) as api:
        print(f'внутри {api}')
except ConnectionError as e:
    print(f'{e} (ожидаемый сбой перехвачен)')



