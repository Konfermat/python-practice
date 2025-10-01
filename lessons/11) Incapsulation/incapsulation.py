# модификаторы доступа
# public, - доступен везде
# protected, условно скрыты для внешнего использования
# private - доступен только внутри класса

class Car:
    def __init__(self, model, year, num = 'asdf134'):
        self.model = model
        self.year = year
        self._serial_number = num #protected
        self.__vin = None #private

    def drive(self):
        self.__vin = '16y76s'
        self._info_serial_number()
        print(f'Driving {self.model} car ')

    def _info_serial_number(self):
        print(f'Serial number: {self._serial_number}')
car = Car('Volkswagen', 1999)

print(car.model)
car.drive()
print()
car._info_serial_number()
print(car.__vin)
print(car._Car__vin)

