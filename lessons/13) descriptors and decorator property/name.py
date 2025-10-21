# descriptors
# @property - у этого декоратора тоже есть гетеры и сетеры
# __get__ __set__ __delete__
# class MyDescriptor:
#     # переопределять не обязательно
#     def __get__(self, instance, owner):
#         print('данный дескриптор')
#         return instance.__dict__.get('attr', None)
#
#     # должен принимать 2 параметра
#     def __set__(self, instance, value):
#         print(f'Установка значения {value}, {instance}')
#         instance.__dict__['attr'] = value
#
#     def __delete__(self, instance):
#         print('Удаление') # нужно указать вручную т к мы переопределили его
#         del instance.__dict__['attr']
#         # instance - obj, self - это attr
#
# class MyClass:
#     attr = MyDescriptor() #Non-data дескриптор они реализуют только метод get
# obj = MyClass()
# obj.attr = 'new value' # здесь метод set
# print(obj.attr) # здесь метод get
# del obj.attr # удаление значения

# @property превращает метод в свойство
class Circle:
    def __init__(self, radius):
        self._radius = radius # защищенный атрибут

    @property
    def perimeter(self):
        return 2 * self._radius * 3.14

    # геттер и сеттер декоратора
    @property # это геттер
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError('Radius must be a positive number')
        self._radius = value

circle = Circle(5)
print(circle.radius) #используется геттер
print(circle.perimeter) # вычесляемое свойство

circle.radius = 10 # используется сеттер
print(circle.radius)

try:
    circle.radius = -5
except ValueError as e:
    print('xdxdxdxdxd')

