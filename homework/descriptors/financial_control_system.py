from datetime import datetime

class FinancialDescriptor:
    def __init__(self, name = None, min_value = 0, max_value = 0):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value
        self.history = []

    def add_history(self, action):
        time_stamp = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        self.history.append(f'Действие: {action} выполнено: {time_stamp}')



class FinancialAccount:
    # 2 to rub 160
    exchange_rate = 1.0

    currency = {
        'USD': 80.8861,
        'EUR': 93.3848,
        'CNY': 11.2449,
        'AED': 22.0248,
        'RUB': 1.0,
    }

    # по заданию непонятно как правильно исполнить.
    # через декоратор @property или через встроенный класс property()
    # сделаю для начала через декоратор

    def __init__(self, age_days = 0, total_commission_paid = 0, monthly_statistics = 0):
        self._age_days = age_days
        self._total_commission_paid = total_commission_paid
        self._monthly_statistics = monthly_statistics

    @property
    def age_days(self):
        return self._age_days
    @age_days.setter
    def age_days(self, value):
        self._age_days = value

    @property
    def total_commission_paid(self):
        return self._total_commission_paid
    @total_commission_paid.setter
    def total_commission_paid(self, value):
        self._total_commission_paid = value

    @property
    def monthly_statistics(self):
        return self._monthly_statistics
    @monthly_statistics.setter
    def monthly_statistics(self, value):
        self._monthly_statistics = value

    @classmethod
    def convert_currency(cls):
        pass

    @classmethod
    def set_exchange_rate(cls):
        pass





print(datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
a = FinancialAccount()
print(a.age_days)
a.age_days = 2
print(a.age_days)

exchange_rate = 1
currency = {
    'USD': 80.8861,
    'EUR': 93.3848,
    'CNY': 11.2449,
    'AED': 22.0248,
}
print('Курс вылюты относительно рубля')
print('конвертирую 2 доллара в рубли')
print()

for key, value in currency.items():
    print(key, value)

