from __future__ import annotations
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


# relationship in relation database:
# One on One


# One to Many (one object to many objects)
# Many to Many (two tables with one supporter table)
# one to manu or
# many to many (one table to suppoerter table) 


print('Hello World')

# in sqlalchemy there is two types of ORM configuration styles:

# Declarative(old but gold?) vs. Imperative(modern?, acoridng to PEP 484) Forms 
# Declarative example:
def demo1():
    class Parent(Base):
        __tablename__ = 'parent_table'
        id = mapped_column(Integer, primary_key=True)
        children = relationship('Child', backpopulates='parent')

    class Child(Base):
        __tablename__ = 'child_table'
        id = mapped_column(Integer, primary_key=True)
        parent_id = mapped_column(ForeignKey('parent_table.id'))
        # in relationship you tell what class then you tell what column
        parent = relationship('Parent', backpopulates='children')
  
# Declarative example(with anotations):
def demo2():    
    class Parent(Base):
        __tablename__ = 'parent_table'
        id: Mapped[int] = mapped_column(primary_key=True)
        children: Mapped[List['Child']] = relationship(backpopulates='parent')
        
    class Child(Base):
        __tablename__ = 'child_table'
        id: Mapped[int] = mapped_column(primary_key=True)
        parent_id: Mapped[int] = mapped_column(ForeignKey('parent_table.id'))
        parent: Mappend[List['Parent']] = relationship(backpopulates='children')

# Imperative example:
def demo3():        
    registry.map_imperatively(
        Parent,
        parent_table,
        properties = {'children': relationship('Child', back_populates='parent')},
    )    
    registry.map_imperatively(
        Child,
        child_table,
        properties = {'parent': relationship('Parent', back_populates='children')},
    )

# One to Many relationship
class Parent(Base):
    __tablename__ = 'parent_table'
    children: Mapped[List['Child']] = relationship()
class Child(Base):
    __tablename__ = 'child_table'
    parent_id: Mapped[int] = mapped_column(ForeignKey('parent_table.id'))
# To establish a bidirectional relationship in one-to-many, 
#where the “reverse” side is a many to one, specify an additional relationship() 
#and connect the two using the relationship.back_populates parameter, 
#using the attribute name of each relationship() 
#as the value for relationship.back_populates on the other:

class Parent(Base):
    __tablename__ = 'parent_table'
    id: Mapped[int] = mapped_column(primary_key=True)
    children: Mapped[List['Child']] = relationship(back_populates='parent')
class Child(Base):
    __tablename__ = 'child_table'
    parent_id: Mapped[int] = mapped_column(ForeignKey('parent_table.id'))