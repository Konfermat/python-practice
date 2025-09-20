from code import interact


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Депозит: {amount}, Новый баланс: {self.balance}')
        else:
            print('Сумма должна быть положительной.')

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f'Снятие: {amount}, Новый баланс: {self.balance}')
            else:
                print("Недостаточно средств")
        else:
            print("Сумма должна быть положительной")


class SavingsAccount(Account):
    def __init__(self, owner, balance, intrest_rate=15):
        super().__init__(owner, balance)
        self.intrest_rate = intrest_rate

    def add_interest(self):
        interest = self.balance * self.intrest_rate / 100
        self.deposit(interest)
        print(f'Начислен процент на остаток{interest}')

    def __str__(self):
        return f'Сберегательный счет {self.owner}. Баланс: {self.balance}'


class CreditAccount(Account):
    def __init__(self, owner, balance, credit_limit=20000):
        super().__init__(owner, balance)
        self.credit_limit = credit_limit

    def withdraw(self, amount):
        if amount > 0:
            if self.balance + self.credit_limit >= amount:
                self.balance -= amount
                print(f'Снятие: {amount}, Новый баланс: {self.balance}')
        else:
            print('Сумма должна быть полжительной.')

# это другой метод хз как

class PremiumAccount(SavingsAccount, CreditAccount):
    def __init__(self, owner, balance, intrest_rate=20, credit_limit=100_000):
        Account.__init__(self, owner, balance)
        self.intrest_rate = intrest_rate
        self.credit_limit = credit_limit

premium = PremiumAccount("Kate", 20_000)
premium.deposit(10_000)
premium.withdraw(8_000)
premium.add_interest()
print(premium.balance)
premium.withdraw(300_000_000)
