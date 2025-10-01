# Абстрактные классы
# raise NotImplementedError
from abc import ABC, abstractmethod
class PayProcess(ABC): # абстрактный класс
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def pay(self, amount):
        pass

    def info(self):
        print('lorem ipsum')


class CreditPayProcess(PayProcess):
    def pay(self, amount):
        self.amount += amount
        return f'Credit pay: {self.amount}'

# pp = PayProcess(100)
cpp = CreditPayProcess(200)
print(cpp.pay(112))
cpp.info()

