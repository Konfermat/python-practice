from sqlalchemy import create_engine, DateTime, select, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, sessionmaker
from datetime import datetime

DB_URL = 'sqlite:///capsules.db'

print('ayaya')
class Base(DeclarativeBase):
    pass

class Message(Base):
    __tablename__ = 'messages'
    id: Mapped[int] = mapped_column(primary_key=True)
    author: Mapped[str] = mapped_column(String(30), nullable=False)
    content: Mapped[str] = mapped_column(String(100), nullable=False)
    unlock_date: Mapped[DateTime] = mapped_column(DateTime(timezone=True), 
        nullable=False) 
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), 
        default=datetime.utcnow())


def spawn_db_extra():
    engine = create_engine(DB_URL)
    # creates engine
    Base.metadata.create_all(bind=engine)
    # creates session
    SessionLocal = sessionmaker(bind=engine)
    with SessionLocal() as session:
        messages = [
            Message(author='Semyon', content='My favorite quote is: "Bla bla bla you\'r wrong bla bla." by Marcus Aurelius', 
                unlock_date=datetime(2026, 2, 1)),
            Message(author='Kasane Teto', content='Tomorrow im locked in.', unlock_date=datetime(2026, 1, 28)),
        ]
        session.add_all(messages)
        session.commit()
    print('Database is created and updated')


def spawn_db():
    engine = create_engine(DB_URL)
    # creates engine
    Base.metadata.create_all(bind=engine)
    print('Database is created')

    