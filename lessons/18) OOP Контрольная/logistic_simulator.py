from abc import ABC, abstractmethod
import copy

class Resource(ABC):
    name = ''
    _amount = 0

    @property
    def amount(self):
        return self._amount
    def __str__(self):
        return f'Resource: {self.name}, Amount: {self._amount}'
    def __add__(self, other):
        if self.name == other.name:
            obj = copy.copy(other)
            obj._amount = self._amount + obj.amount
            return obj
        else:
            raise TypeError("objects not the same")

    @amount.setter
    def amount(self, num):
        if isinstance(round(num), int) and round(num) >= 0:
            self._amount = round(num)
        else:
            raise TypeError("amount must be >= 0 and be a number")

class Building(ABC):
    name = ''
    storage = {}
    @abstractmethod
    def produce(self):
        pass

class ResourceLimiter:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity


class Wood(Resource):
    def __init__(self, name='Wood', amount=0):
        self.name = name
        self._amount = amount

class Food(Resource):
    def __init__(self, name='Food', amount=0):
        self.name = name
        self._amount = amount

class Farm(Building):
    def __init__(self, name='Farm', max_food=0):
        self.name = name
        self.storage = {}
        self.max_food = ResourceLimiter(max_food)

    def produce(self):

        print(f'')

class LumberMill(Building):
    def __init__(self, name='LumberMill', max_wood=0):
        self.name = name
        self.storage = {}
        self.max_wood = ResourceLimiter(max_wood)

    def produce(self):
        print('May produce wood')

class OakProducer()

w1 = Wood(name='W1', amount=1)
w2 = Wood(name='W1', amount=2)
f1 = Food(name='F1', amount=1)

'''
print(w1 + w2)
print(w1.amount)
w1.amount = 2.9
print(w1.amount)
'''

