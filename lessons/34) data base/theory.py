# sql lite создает db локально
# мы будем прописывать sql запросы в python
import sqlite3


conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('''
    create table if not exists users(
        id integer primary key autoincrement, 
        user_name text not null,
        password text not null,
        email text )
''')
# data = {'username': 'Kate',
#         'password': '1234',
#         'email': 'k@g.com'}

# cursor.execute('''-
#     insert into users(username, password, email)
#     values(?, ?, ?)
# ''', (data['username'], data['password'], data['email']))


# другой способ
data = [('Alice', '1234', 'a@g.com'),
        ('Bob', '234', 'b@.com')]

cursor.executemany('''
    insert into users(user_name, password, email)
    values (?, ?, ?)
''', data)
# is_active 0/1
cursor.execute('''
delete from users where is_active = 0
''')

# executescript()
conn.commit()

users = cursor.execute('select * from users')
# для получения
print(users.fetchall())
# fetchall() fetchone()
cursor.close()
conn.close()
