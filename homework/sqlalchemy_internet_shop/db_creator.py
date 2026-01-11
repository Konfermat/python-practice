from sqlalchemy import create_engine, String, Numeric, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from datetime import datetime
from typing import List

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    registration_date: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now())
    
    orders: Mapped[List['Order']] = relationship(back_populates='user', cascade='all, delete-orphan')

class Product(Base):
    __tablename__ = 'products'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    category: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[Numeric] = mapped_column(Numeric(10, 2), nullable=False)
    quantity_in_stock: Mapped[int] = mapped_column(default=0)
    
    order_items: Mapped[List['OrderItem']] = relationship(back_populates='product')

class Order(Base):
    __tablename__ = 'orders'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    order_date: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now())
    status: Mapped[str] = mapped_column(String(20), default='в обработке')
    
    user: Mapped['User'] = relationship(back_populates='orders')
    items: Mapped[List['OrderItem']] = relationship(back_populates='order', cascade='all, delete-orphan')

class OrderItem(Base):
    __tablename__ = 'order_items'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey('orders.id'), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False)
    price_at_order: Mapped[Numeric] = mapped_column(Numeric(10, 2), nullable=False)
    
    order: Mapped['Order'] = relationship(back_populates='items')
    product: Mapped['Product'] = relationship(back_populates='order_items')

if __name__ == '__main__':
    # создание таблиц
    engine = create_engine('sqlite:///electronics.db')
    Base.metadata.create_all(engine)