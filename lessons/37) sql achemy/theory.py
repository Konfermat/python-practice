# pip install sqlalchemy
# объектно ориентированная база данных
# json не реляционный это формат данных
from calendar import TextCalendar

#import sqlalchemy
from sqlalchemy import create_engine, String, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, Mapped, mapped_column, relationship

# int - Integer
# str - String(length)
# str - Text
# bool - Boolean (true/false)
# float - Float() Numeric()
# datetime.datetime - DateTime()
# datetime.date - Date()
# Enum()
# Mapped[int] Integer

class Base(DeclarativeBase):
    pass

class Author(Base):
    __tablename__ = 'authors'
    id: Mapped[int] = mapped_column(primary_key=True)
    # id = Column(Integer(), )
    books: Mapped[list['Book']] = relationship(back_populates='author')
    name: Mapped[str] = mapped_column(String(30), nullable=False)

class Book(Base):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    author_id:Mapped[int] = mapped_column(ForeignKey('authors.id'))
    author: Mapped['Author'] = relationship(back_populates='books')
