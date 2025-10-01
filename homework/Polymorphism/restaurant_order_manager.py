class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f'Название: "{self.name}", Цена: {self.price} рублей.'
        
class MainDish(Dish):
    def __init__(self, name, price, milk_free, meat_free):
        super().__init__(name, price)
        self.milk_free = milk_free
        self.meat_free = meat_free
    
    def __str__(self):
        tmp = super().__str__()[:-1]
        return tmp + f', Содержит молоко: {self.milk_free}, Содержит мясо: {self.meat_free}.'

class Dessert(Dish):
    def __init__(self, name, price, honey):
        super().__init__(name, price)
        self.honey = honey
    
    def __str__(self):
        tmp = super().__str__()[:-1]
        return tmp + f', Содержит мед: {self.honey}.'

class Drink(Dish):
    def __init__(self, name, price, alcohol):
        super().__init__(name, price)
        self.alcohol = alcohol
    
    def __str__(self):
        tmp = super().__str__()[:-1]
        return tmp + f', Содержит алкоголь: {self.alcohol}.'
    
class Order:
    def __init__(self):
        self.dishes = []
    
    def add_dish(self, dish):
        self.dishes.append(dish)
    
    def remove_dish(self, dish):
        if dish in self.dishes:
            self.dishes.remove(dish)
    
    def total_price(self):
        return sum(dish.price for dish in self.dishes)
    
    def __str__(self):
        return '\n'.join(str(dish) for dish in self.dishes)
    
    def __add__(self, other):
        new_order = Order()
        new_order.dishes = self.dishes + other.dishes
        return new_order
    
    def __gt__(self, other):
        return self.total_price() > other.total_price()


d1 = Dish('Яичница', 20)
md1 = MainDish('Шашлык по Грузински', 500, 'Нет', 'Да')
dr1 = Drink('Веселый велосипедист', 250, 'Да')

order1 = Order()
print('Заказ 1: ')
order1.add_dish(d1)
order1.add_dish(md1)
order1.add_dish(dr1)
order1.add_dish(dr1)
print(order1)
print()

print('Заказ 1 с коректировкой: ')
order1.remove_dish((d1))
print(order1)
print()

print('Заказ 2: ')
order2 = Order()
order2.add_dish(d1)
order2.add_dish(md1)
print(order2)

print('Сравнение двух заказов.')
print(f'Заказ 1 дороже Заказа 2?: {order1 > order2}')
print()

print('Сложение двух заказов.')
print('Заказ 3:')
order3 = Order()
order3 = order1 + order2
print(order3)

    