# Контекстный менеджер это with
# Менеджеры контекста
# когда мы используем КМ вызывается мг метож __enter__()
# где есть вход там есть и выхож
# __exit__() вызвается при выходе
# может вызывать исключения
# нас интересует создание собственного менеджера котекста

# как он работает
# Мы пишем свой менеджер контекста
# смотрим ка работет with

# С одним enter или с несколькими
'''class FileWriter:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'w')
        # озвращает экземпляр класса
        return self

    def write(self, text):
        self.file.write(text)
                        #тип искл само искл, объект трассировки
    def __exit__(self, exc_type, exc_val, exc_tb):
        # if self.file:
        #     self.file.close()
        if exc_type:
            print(f'Ошибка {exc_val}')
        self.file.close()
        return True

# использование
with FileWriter('output.txt') as writer:
    writer.write('Hello Word')
    raise Exception('ошибка при записи')
'''


# контекстный менеджер с нескольким входами
# свой менеджер контекста
class FileWriter:
    # def __init__(self, filename):
    #     self.filename = filename
    #     self.file = None

    def __enter__(self):
        self.file = open('log.txt', 'w')
        return self

    # def abracadabra(self, text):
    #     self.file.write(text)
                        #тип  само исключение  объект трассировки(для диагностики)
    def __exit__(self, exc_type, exc_val, exc_tb):
        # if self.file:
        self.file.close()
        if exc_type:
            print(f'Ошибка {exc_val}')
        # self.file.close()
        return True

class DBConnection:
    def __enter__(self):
        print('открываем соединение с бд')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('закрываем соединение с БД')
        if exc_type:
            print(f'Ошибка {exc_val}')
        return True


#использование
with FileWriter() as writer, DBConnection() as db:
    writer.abracadabra('Hello World')
    # raise Exception('ошибка при записи')
    print('работа с БД')
