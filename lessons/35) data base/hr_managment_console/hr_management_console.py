import sqlite3
from contextlib import contextmanager

DB_FILE = 'hr_management.db'

class DBManagerSingleton:
    _instance = None
    _connection = None
    _db_path = None

    def __new__(cls, db_path=DB_FILE):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._db_path = db_path
        return cls._instance

    #метод для получения единственного экземпляра
    @staticmethod
    def get_instance():
        if DBManagerSingleton._instance is None:
            DBManagerSingleton._instance = DBManagerSingleton()
        return DBManagerSingleton._instance

    @contextmanager
    def connection(self):
        if DBManagerSingleton._connection is None:
            try:
                DBManagerSingleton._connection = sqlite3.connect(self._db_path)
            except sqlite3.Error as e:
                print(f'Ошибка подключения к БД: {e}')
        conn = DBManagerSingleton._connection
        conn.commit() # фиксируем изменения # возможно rollback

class HRConsole:
    pass


