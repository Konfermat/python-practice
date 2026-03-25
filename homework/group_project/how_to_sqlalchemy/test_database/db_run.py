from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from db_declare import User, Address

engine = create_engine('sqlite:///test_database.db')

def seed_db():
    with Session(engine) as session:
        chicken = User(
            name='Chicken',
            fullname='Chicken Eggfish',
            addresses=[Address(email_address='chicken@sql.org')],
        )
        fish = User(
            name='Bubble',
            fullname='Bubble Bass',
            addresses=[
                Address(email_address='BubbleBase@sql.org'),
                Address(email_address='Bubble@sql.org')
            ],
        )
        deer = User(
            name='Buck',
            fullname='Buck Deer'
        )

        session.add_all([chicken, fish, deer])
        session.commit()

seed_db()
    
