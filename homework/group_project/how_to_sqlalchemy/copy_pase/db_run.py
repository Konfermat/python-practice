from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db_declare import User, Address, Base

engine = create_engine("sqlite:///copy_paste.db")

def spawn_db():
    Base.metadata.create_all(engine)
    print('db was spawned')
# spawn_db()

def seed_db():
    with Session(engine) as session:
        spongebob = User(
            name="spongebob",
            fullname="Spongebob Squarepants",
            addresses=[Address(email_address="spongebob@sqlalchemy.org")],
        )
        sandy = User(
            name="sandy",
            fullname="Sandy Cheeks",
            addresses=[
                Address(email_address="sandy@sqlalchemy.org"),
                Address(email_address="sandy@squirrelpower.org"),
            ],
        )
        patrick = User(name="patrick", fullname="Patrick Star")
        session.add_all([spongebob, sandy, patrick])
        session.commit()
# seed_db()

from sqlalchemy import select

def simple_select():
    session = Session(engine)
    stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))
    for user in session.scalars(stmt):
        print(user.id)
        print(user.name)
        print(user.fullname)
        print()
# simple_select()

def select_with_join():
    session = Session(engine)    
    stmt = (
        select(Address)
        .join(Address.user)
        .where(User.name=='sandy')
        .where(Address.email_address=='sandy@sqlalchemy.org')
    )
    sandy_address = session.scalars(stmt).one()
    print(sandy_address.id)
    print(sandy_address.email_address)
# select_with_join()

