import sqlite3
from datetime import datetime, timedelta

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

DATABASE = 'users.db'
def create_table():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        create table if not exists users(
        CustomerID integer primary key autoincrement, 
        FirstName text,
        LastName text,
        email text,
        phone text,
        RegistrationDate text,
        IsActive INTEGER)
        ''')
        conn.commit()
        print('Талица users создалась')
def insert_user(data):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        insert into users(FirstName, LastName, email, phone, RegistrationDate)
        values(?, ?, ?, ?, ?)
        ''', data)
        conn.commit()
        print('данные успешно добавлены')

def get_not_active()->list[tuple]:
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        days_ago = datetime.now() - timedelta(days=30)
        cursor.execute('''
            select * from users
            where RegistrationDate < ? and
            isActive = 0
        ''', (days_ago.strftime('%Y-%m-%d'), ))
        return cursor.fetchall()

def update_user(customerId, status):
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            update users set isAlive = ?
            where CustomerID = ?
                
        ''', (status, customerId))
        conn.commit()

def delete_user():
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        days_ago = datetime.now() - timedelta(days=60)
        cursor.execute('''
        delete from users
        where RegisrationDate < ? and
        isActive = 0
        ''', (days_ago.strftime('%Y-%m-%d'),))
        # in database
        # datetime %Y-%m-%d %H:%M:%S
        # data %Y-%m-%d
        # time %H:%M:%S
        conn.commit()
