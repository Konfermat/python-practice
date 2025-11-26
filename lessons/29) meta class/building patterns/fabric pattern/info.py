from abc import ABC, abstractmethod

#Product
class Car:
    def __init__(self):
        self.parts = {}

    def add_part(self, name, value):
        self.parts[name] = value

    # строкове представление
    def __str__(self):
        parts_list = '\n'.join(f'{name}: {value}' for name, value in self.parts.items())
        return f'готовый автомобиль: {parts_list}'

# Builder
class CarBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_engine(self, type_engine):
        pass
        return self

    @abstractmethod
    def set_wheels(self, number):
        pass
        return self

    @abstractmethod
    def get_result(self):
        pass

# Concrete Builder
class SportCarBuilder(CarBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._car = Car()

    def set_engine(self, type_engine='diesel'):
        self._car.add_part('engine', type_engine)
        return self

    def set_wheels(self, number=4):
        self._car.add_part('wheel', number)
        return self

    def get_result(self):
        car = self._car
        self.reset()
        return car

class Director:
    def __init__(self, builder: CarBuilder):
        self._builder = builder

    def build_full_featured(self):
        # продолжаем цепочку вызовов
        # изображение цепочек вызовов с переносом
        return self._builder.set_engine('diesel Turbo').set_wheels(4).get_result()

builder = SportCarBuilder()
director = Director(builder)
sport_car = director.build_full_featured()
print(sport_car)


