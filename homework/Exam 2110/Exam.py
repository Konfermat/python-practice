from abc import ABC, abstractmethod

# Часть 1 и 3: Абстрактный класс Resource с геттером и сеттером для amount,
# магическими методами __str__ и __add__
class Resource(ABC):
    def __init__(self, name, amount):
        self.name = name
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if not isinstance(value, int):
            raise TypeError("Amount must be an integer")
        if value < 0:
            raise ValueError("Amount cannot be negative")
        self._amount = value

    def __str__(self):
        return f"Ресурс: {self.name}, количество: {self.amount}"

    def __add__(self, other):
        if not isinstance(other, Resource):
            return NotImplemented
        if type(self) != type(other):
            raise TypeError("Нельзя сложить разные ресурсы")
        return type(self)(self.amount + other.amount)

# Конкретные классы ресурсов Wood и Food
class Wood(Resource):
    def __init__(self, amount):
        super().__init__("Дерево", amount)

class Food(Resource):
    def __init__(self, amount):
        super().__init__("Еда", amount)

# Часть 4: Дескриптор ResourceLimiter для ограничения максимального запаса ресурса
class ResourceLimiter:
    def __init__(self, max_value):
        self.max_value = max_value
        self._values = {}

    def __get__(self, instance, owner):
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if value > self.max_value:
            raise ValueError(f"Достигнут максимальный лимит {self.max_value}")
        self._values[instance] = value

# Часть 6: Декоратор log_production для логирования процесса производства
def log_production(method):
    def wrapper(self, *args, **kwargs):
        print(f"--- НАЧАЛО ПРОИЗВОДСТВА: {self.__class__.__name__} [{self.name}] ---")
        result = method(self, *args, **kwargs)
        print(f"--- ПРОИЗВОДСТВО ЗАВЕРШЕНО: {self.__class__.__name__} ---")
        return result
    return wrapper

# Абстрактный класс Building с хранилищем ресурсов и абстрактным методом produce
class Building(ABC):
    max_wood = None  # Для LumberMill
    max_food = None  # Для Farm

    def __init__(self, name):
        self.name = name
        self.storage = {}

    @abstractmethod
    def produce(self):
        pass

    # Часть 5: Статический метод для вычисления стоимости производства ресурса
    @staticmethod
    def calculate_production_cost(resource_type):
        if resource_type == Food:
            return 10
        elif resource_type == Wood:
            return 5
        return 0

    # Часть 5: Метод класса для создания здания с начальными запасами
    @classmethod
    def create_initial_setup(cls, name):
        instance = cls(name)
        if cls.__name__ == 'Ферма':
            instance.storage[Food.__name__] = Food(50)
        elif cls.__name__ == 'Лесопилка':
            instance.storage[Wood.__name__] = Wood(50)
        return instance

# Конкретный класс Farm с дескриптором max_food и декорированным produce
class Farm(Building):
    max_food = ResourceLimiter(100)

    @log_production
    def produce(self):
        food = self.storage.get(Food.__name__, Food(0))
        new_amount = food.amount + 10
        if new_amount > self.max_food:
            print("Лимит по еде достигнут, производство остановлено.")
            return
        self.storage[Food.__name__] = Food(new_amount)
        self.max_food = new_amount

# Конкретный класс LumberMill с дескриптором max_wood и декорированным produce
class LumberMill(Building):
    max_wood = ResourceLimiter(100)

    @log_production
    def produce(self):
        wood = self.storage.get(Wood.__name__, Wood(0))
        new_amount = wood.amount + 10
        if new_amount > self.max_wood:
            print("Лимит по древесине достигнут, производство остановлено.")
            return
        self.storage[Wood.__name__] = Wood(new_amount)
        self.max_wood = new_amount


# --- Тестирование работы системы ---

if __name__ == "__main__":
    # Создание зданий через метод класса
    farm = Farm.create_initial_setup("Ферма дяди Вовы")
    lumber_mill = LumberMill.create_initial_setup("Лесопилка Гампа")

    # Демонстрация сложения ресурсов одного типа
    wood1 = Wood(30)
    wood2 = Wood(20)
    wood_sum = wood1 + wood2
    print(wood_sum)  # Resource: Wood, amount: 50
    print()

    # Попытка сложения ресурсов разных типов вызывает ошибку
    food1 = Food(50)
    try:
        invalid_sum = wood1 + food1
    except TypeError as e:
        print(e)  # Cannot add different types of resources
    print()

    # Попытка установить отрицательное значение amount вызывает ValueError
    try:
        food1.amount = -10
    except ValueError as e:
        print(e)  # Amount cannot be negative
    print()

    # Производство с проверкой лимитов и логированием
    for _ in range(6):
        farm.produce()
    for _ in range(6):
        lumber_mill.produce()
    print()

    # Проверка стоимости производства
    print("Стоимость производства Food:", Farm.calculate_production_cost(Food))  # 10
    print("Стоимость производства Wood:", LumberMill.calculate_production_cost(Wood))  # 5
