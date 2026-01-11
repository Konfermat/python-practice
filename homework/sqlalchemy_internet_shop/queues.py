# queries.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_creator import Order, Product, User  # предполагаем models.py

engine = create_engine('sqlite:///electronics.db')
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# 1. Товары в категории "Смартфон" дешевле 50_000
smartphones = session.query(Product).filter(
    Product.category == 'Смартфон',
    Product.price < 50000
).all()

print("Товары 'Смартфон' < 50k:")
for p in smartphones:
    print(f"- {p.name}: {p.price} руб.")

# 2. Заказы пользователя customer@example.com
customer_orders = session.query(Order).join(Order.user).filter(
    User.email == 'customer@example.com'
).all()

print("\nЗаказы customer@example.com:")
for order in customer_orders:
    print(f"- Заказ #{order.id}: {order.order_date}, статус: {order.status}")

session.close()
