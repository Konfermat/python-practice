# seed.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_creator import Base, User, Product, Order, OrderItem  # предполагаем models.py с моделями

engine = create_engine('sqlite:///electronics.db', echo=True)
SessionLocal = sessionmaker(bind=engine)

# Создание таблиц
Base.metadata.create_all(engine)

session = SessionLocal()

# 5 пользователей
users = [
    User(username='user1', email='user1@example.com'),
    User(username='customer', email='customer@example.com'),
    User(username='buyer2', email='buyer2@example.com'),
    User(username='shopper', email='shopper@example.com'),
    User(username='client3', email='client3@example.com'),
]
session.add_all(users)
session.flush()  # для получения ID

# 10 товаров
products = [
    Product(name='iPhone 15', category='Смартфон', price=45000.00, quantity_in_stock=10),
    Product(name='Samsung Galaxy', category='Смартфон', price=35000.00, quantity_in_stock=15),
    Product(name='Xiaomi 14', category='Смартфон', price=28000.00, quantity_in_stock=20),
    Product(name='MacBook Pro', category='Ноутбук', price=120000.00, quantity_in_stock=5),
    Product(name='Dell XPS', category='Ноутбук', price=85000.00, quantity_in_stock=8),
    Product(name='AirPods Pro', category='Наушники', price=25000.00, quantity_in_stock=12),
    Product(name='Sony WH-1000', category='Наушники', price=32000.00, quantity_in_stock=7),
    Product(name='iPhone 14', category='Смартфон', price=40000.00, quantity_in_stock=10),
    Product(name='Asus Zenbook', category='Ноутбук', price=95000.00, quantity_in_stock=6),
    Product(name='JBL Tune', category='Наушники', price=8000.00, quantity_in_stock=25),
]
session.add_all(products)
session.flush()

# 5 заказов
orders_data = [
    (users[0], [('iPhone 15', 1), ('AirPods Pro', 2)]),
    (users[1], [('Samsung Galaxy', 1), ('Dell XPS', 1), ('Sony WH-1000', 1)]),
    (users[2], [('Xiaomi 14', 2)]),
    (users[3], [('MacBook Pro', 1)]),
    (users[4], [('iPhone 14', 1), ('JBL Tune', 3), ('Asus Zenbook', 1)]),
]

for user, items_data in orders_data:
    order = Order(user=user, status='оплачен')
    session.add(order)
    session.flush()
    
    for prod_name, qty in items_data:
        product = session.query(Product).filter(Product.name == prod_name).one()
        order_item = OrderItem(
            order=order,
            product=product,
            quantity=qty,
            price_at_order=product.price
        )
        session.add(order_item)

session.commit()
session.close()
print("База данных заполнена тестовыми данными!")
