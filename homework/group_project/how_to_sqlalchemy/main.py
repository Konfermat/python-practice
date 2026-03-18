from typing import Optional
from sqlalchemy import Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

DB_URL = 'sqlite:///test1.db'
engine = create_engine(DB_URL, echo=True)

class Base(DeclarativeBase):
    pass

class BongBong(Base):
    __tablename__ = 'bongbongs':
    id: Mapped[int] = mapped_column(primary_key=True)
    bong_bong: Mapped[Optional[str]] = mapped_column(String())

bong_one = BongBong()
bong_two = BongBong(bong_bong='Бонг Бонг')

