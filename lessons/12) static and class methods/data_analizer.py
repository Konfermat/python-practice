import pandas
import os

from abc import ABC, abstractmethod

class DataAnalyzer(ABC):
    def __init__(self, filepath):
        self.filepath =filepath
        self.data = None # Для хранения данных после чтения

    @abstractmethod
    def read_data(self):
        pass

    def get_summary(self):
        if self.data is None:
            return 'данные не загружены'
        num_rows, num_cols = self.data.shape
        columns = list(self.data.columns)

        print('------СВОДНЫЙ ОТЧЕТ------')
        print(f'Файл: {os.path.basename(self.filepath)}')
        print(f'Кол-во записей: {num_rows}')
        print(f'Кол-во колонок: {num_cols}')
        print(f'Название колонок: {columns}')
        print('-' * 30 + '\n')


    @staticmethod
    def validate_data(filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f'Файл не найден по пути {filepath}')
        return True

    @classmethod
    def create_analyzer(cls, filepath):
        cls.validate_data(filepath)
        _, ext = os.path.splitext(filepath)
        # print(os.path.splitext('repo.rts/report.pdf'))
        ext = ext.lower()
        if ext == '.csv':
            return CSVAnalyzer(filepath)
        elif ext =='.json':
            return JSONAnalyzer(filepath)
        else:
            raise ValueError(f'неподдерживаемый тип файла {ext}')

class CSVAnalyzer(DataAnalyzer):
    def read_data(self):
        print(f'reading {self.filepath}')
        self.data = pandas.read_csv(self.filepath)

class JSONAnalyzer(DataAnalyzer):
    def read_data(self):
        print(f'reading {self.filepath}')
        self.data = pandas.read_json(self.filepath)

'''print(type(pandas.read_json('data.json')))
print(pandas.read_json('data.json').shape)
print(pandas.read_json('data.json'))

print(pandas.read_csv('data.csv'))'''

if __name__ == '__main__':
    file_to_analyze = ['data.csv', 'data.json', 'not.txt']

    for file in file_to_analyze:
        try:
            analyzer = DataAnalyzer.create_analyzer(file)
            analyzer.read_data()
            analyzer.get_summary()
        except (FileNotFoundError, ValueError) as e:
            print(f'{file}: {e}\n')
