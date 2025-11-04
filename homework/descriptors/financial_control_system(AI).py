from datetime import datetime

# Базовый класс для всех финансовых дескрипторов
class FinancialDescriptor:
    def __init__(self, name, min_value, max_value):
        self.name = name
        self.min_value = min_value
        self.max_value = max_value
        self.history = []
        self._add_to_history('Created')

    def _add_to_history(self, action):
        timestamp = self._get_current_timestamp()
        self.history.append({'action': action, 'timestamp': timestamp})

    def _get_current_timestamp(self):
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def validate_value(self, value):
        if value < self.min_value or value > self.max_value:
            raise ValueError(f"Value must be between {self.min_value} and {self.max_value}")


# Класс для баланса (наследуется от FinancialDescriptor)
class BalanceDescriptor(FinancialDescriptor):
    def __init__(self, name, min_value, max_value, is_credit_account=False):
        super().__init__(name, min_value, max_value)
        self.is_credit_account = is_credit_account
        self.balance = 0.0

    def set_balance(self, value):
        if not self.is_credit_account and value < 0:
            raise ValueError("Debit accounts cannot have a negative balance.")
        self.validate_value(value)
        self.balance = value
        self._add_to_history(f"Balance set to {value}")

    def check_sufficiency(self, amount):
        if self.is_credit_account:
            return self.balance + self.max_value >= amount  # Allow balance to go below 0 if it's a credit account
        return self.balance >= amount


# Класс для суммы транзакции (наследуется от FinancialDescriptor)
class TransactionAmountDescriptor(FinancialDescriptor):
    def __init__(self, name, min_value, max_value):
        super().__init__(name, min_value, max_value)

    def calculate_fee(self, amount):
        return amount * 0.01  # 1% fee

    def check_transaction(self, amount, balance):
        fee = self.calculate_fee(amount)
        total_amount = amount + fee
        if not balance.check_sufficiency(total_amount):
            raise ValueError("Insufficient funds for this transaction.")
        return fee


# Класс для категории расходов (наследуется от FinancialDescriptor)
class CategoryDescriptor(FinancialDescriptor):
    def __init__(self, name, min_value, max_value, categories):
        super().__init__(name, min_value, max_value)
        self.categories = categories
        self.limits = {}

    def set_category_limit(self, category, limit):
        if category not in self.categories:
            raise ValueError(f"Category {category} is not valid.")
        self.limits[category] = limit

    def check_category_limit(self, category, amount):
        if category not in self.limits:
            raise ValueError(f"Limit for category {category} is not set.")
        if amount > self.limits[category]:
            raise ValueError(f"Amount exceeds the limit for category {category}.")
        return True


# Основной класс для финансового счета
class FinancialAccount:
    exchange_rates = {}

    def __init__(self, account_name, currency, initial_balance=0.0):
        self.account_name = account_name
        self.currency = currency
        self.balance = BalanceDescriptor('Balance', 0.0, 1000000.0)
        self.balance.set_balance(initial_balance)
        self.age_days = 0
        self.total_commission_paid = 0.0
        self.monthly_statistics = {}
        self._add_to_history('Account Created')

    @classmethod
    def set_exchange_rate(cls, from_currency, to_currency, rate):
        if from_currency not in cls.exchange_rates:
            cls.exchange_rates[from_currency] = {}
        cls.exchange_rates[from_currency][to_currency] = rate

    @classmethod
    def convert_currency(cls, amount, from_currency, to_currency):
        if from_currency == to_currency:
            return amount
        if from_currency in cls.exchange_rates and to_currency in cls.exchange_rates[from_currency]:
            return amount * cls.exchange_rates[from_currency][to_currency]
        raise ValueError(f"Exchange rate from {from_currency} to {to_currency} not available.")

    def _add_to_history(self, action):
        timestamp = self._get_current_timestamp()
        if timestamp not in self.monthly_statistics:
            self.monthly_statistics[timestamp] = []
        self.monthly_statistics[timestamp].append(action)

    def _get_current_timestamp(self):
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def make_transaction(self, amount, category, descriptor, fee_calculator):
        fee = fee_calculator.check_transaction(amount, self.balance)
        self.balance.set_balance(self.balance.balance - (amount + fee))
        self.total_commission_paid += fee
        self._add_to_history(f"Transaction of {amount} in category {category} made with fee {fee}")

    def deposit(self, amount):
        self.balance.set_balance(self.balance.balance + amount)
        self._add_to_history(f"Deposit of {amount}")

    def __str__(self):
        return f"Account: {self.account_name}, Balance: {self.balance.balance}, Currency: {self.currency}"


# Пример использования:
account = FinancialAccount('MyAccount', 'USD', 500.0)
category_descriptor = CategoryDescriptor('Expense Category', 0, 100000, ['Food', 'Entertainment', 'Bills'])

# Установим лимит по категории
category_descriptor.set_category_limit('Food', 200.0)

# Попробуем выполнить транзакцию
try:
    transaction_descriptor = TransactionAmountDescriptor('Transaction', 0.01, 10000)
    account.make_transaction(100.0, 'Food', category_descriptor, transaction_descriptor)
except ValueError as e:
    print(f"Error: {e}")

# Пополнение счета
account.deposit(50.0)

# Вывод счета
print(account)
