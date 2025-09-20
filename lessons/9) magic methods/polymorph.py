# полиморфизм реализация через наследование
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return 'Woof!'

class Cat(Animal):
    def speak(self):
        return 'Meow!'

# Пример полиморфизма
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.speak())

# DuckTyping
class Human:
    def speak(self):
        return 'Hello!'
class Duck:
    def speak(self):
        return 'Krya!'

def make_sound(object):
    print(object.speak())

human = Human()
duck = Duck()

# Экземпляр класса
make_sound(Human())
make_sound(Duck())
#
# полиморфизм через перегрузку операторов
class Vector:
    # перегрузка
    # переопределили '-'
    # непонял зачем это надо
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f'{self.x}, {self.y}'
# переопределили оператор "+"
v1 = Vector(2, 3)
v2 = Vector(2, 7)
v3 = v2 + v1
# print(v3)
# print(5 + 2)

