# # @staticMethod
# # @classmethod
#
# class Converter:
#     ed_iz = ''#атрибут класса
#     def __init__(self, value):
#         self.value = value
#
#     @staticmethod
#     def cel_to_fah(celsius):
#         return(celsius * 9 / 5) + 32
#
# print(Converter.cel_to_fah(9))
# converter = Converter(25)
# print(converter.cel_to_fah(25))

class Worker:
    percent = 1.05

    def __init__(self, name, lastname, salary):
        self.name = name
        self.lastname = lastname
        self.salary = salary

    def get_full_name(self):
        return f'{self.name} {self.lastname}'

    @classmethod #декоратор
    def set_percent(cls, new_percent):
        if new_percent > 1.0:
            cls.percent = new_percent
        else:
            print('должен быть больше 1')

    @classmethod
    def from_str(cls, str_worker):
        name, lastname, salary = str_worker.split('-')
        return cls(name, lastname, salary)

worker_str = 'Вася-Пупкин-50000'
worker = Worker.from_str(worker_str)
print(worker.get_full_name())
print(worker.percent)
worker.set_percent(2.5)
print(Worker.percent)
