from abc import ABC, abstractmethod

class DataManager(ABC):
    '''Абстрактный класс для управления данными'''
    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def write_data(self, data):
        pass

class FileDataManager(DataManager):
    def __init__(self, filename):
        self.filename = filename

    def read_data(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return 'файл не найден'

    def write_data(self, data):
        with open(self.filename, 'w', encoding='utf-8') as f:
            f.write(data)
        return 'данные записаны'

class DatabaseDataManager(DataManager):
    def __init__(self):
        self.database = {}

    def read_data(self):
        return self.database

    def write_data(self, data):
        if isinstance(data, dict):
            self.database.update(data)
            return 'база данных объединена'
        return 'Ошибка! ожидается словарь'

if __name__ == '__main__':
    file_manager = FileDataManager('data.txt')
    db_manager = DatabaseDataManager()

    print(file_manager.write_data('Пример данных'))
    print('Содержимое файла: ', file_manager.read_data())

    print(db_manager.write_data({'user': 'admin', 'password': 1234}))
    print('содержимое БД', db_manager.read_data())
    print('содержимое БД', db_manager.read_data())



