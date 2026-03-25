from sqlalchemy import create_engine
from models import Base

def spawn_db(engine_type, name):
    engine = create_engine(f'{engine_type}:///{name}')
    Base.metadata.create_all(engine)
    print(f'db {name} was created')

if __name__ == '__main__':
    spawn_db('sqlite', 'models_instance.db')
