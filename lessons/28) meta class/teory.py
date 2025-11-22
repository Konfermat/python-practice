# # синглтон
# class Singleton(type):
#     _instances = {} #словарь экземпляров
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             #создаем новый экземпляр
#             instance = super().__call__(*args, **kwargs)
#             cls._instances[cls] = instance
#         return cls._instances[cls]
#
# class App(metaclass=Singleton):
#     def __init__(self, debug_mode=False):
#         if not hasattr(self, '_initialized'):
#             self.debug_mode = debug_mode
#             self._initialized = False
#             print('инициализация конфигурации')
#         else:
#             print('вторая попытка проигнорирована')
#
#     def set_db(self, path):
#         self.db_path = path
#         print('путь к бд установлен')
#
# config1 = App(debug_mode=True)
# config1.set_db('data/db')
# print(config1.debug_mode)
#
# config2 = App(debug_mode=False)
# print(config2.debug_mode)
# print(config2.db_path)
# print(config1.db_path)
#
# print(config1 is config2)
# print(id(config1), id(config2))
# # синглтон
# # можно также сделать с помощью декоратора
# # синглтоны усложняют тестирование
#
# # SRP (принцип единственной ответветственности)

#вариант с декоратором
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Logger:
    def __init__(self):
        print('инициализирован')

log1 = Logger()
log2 = Logger()
print(log1 is log2)
print(id(log1), id(log2))


