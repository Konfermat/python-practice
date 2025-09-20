# # n = 5
# # s = 'asdf'
# # l1 = [1, 2, 3]
# # def funct():
# #     pass
# # class Test:
# #     pass
# #
# # print(type(n))
# # print(type(s))
# # print(type(l1))
# # print(type(funct))
# # print(type(Test))
#
# # __init__ магический метод
# class Dog:
# # Есть обязательные аргументы есть не обязательные
# # breed_arg по умолчанию будет создавать породу такс
# # name_arg не обязательный аргумент
#
#     # обязательно присваивать
#     def __init__(self, name_arg, age_arg, breed_arg='taksa'):
#         self.name = name_arg
#         self.age = age_arg
#         self.breed = breed_arg
#
#     # name = 'Luna'
#     # age = 5
#
#     # self это указатель на объект
#     def wooff(self, owner):
#         print(f'Whoof! Says {self.name}. Owner: {owner}')
#
#     # магический метод __str__
#     # строковое представление объекта
#     # если вывести объект без этого магического метода то выведется ссылка объекта
#     def __str__(self):
#         return f'{self.name} {self.age} {self.breed}'
#
# dog1 = Dog('Vasiliy', 12)
# dog2 = Dog('Toma', 21)
# dog3 = Dog('Jimbo', 2)
#
#
# # print(dog1.name, dog1.age)
# # dog1.wooff()
#
# dog1.name = 'Boris'
# print(dog1.name, dog1.age)
#
# dog1.wooff('Grisha')
# print(dog1)
#

class Transport:
    def __init__(self, speed, color, brand):
        self.speed = speed
        self.color = color
        self.brand = brand

    def sound(self):
        print(f'Beeb beep')

class Car(Transport):
    def __init__(self, speed, color, brand, seats):
        super().__init__(speed, color, brand)
        self.seats = seats
    def sound(self):
        print('NYAM NYAM ELYA!')
    def beeep(self):
        print('beep')

car = Car(speed=1, color='red', brand='BMW', seats=2)
print(car.color)
car.sound()

