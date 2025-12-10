class Vehicle:
    def __init__(self):
        self.vehicle = 1

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.car = 2

v = Vehicle()
c = Car()
print(c.__repr__())