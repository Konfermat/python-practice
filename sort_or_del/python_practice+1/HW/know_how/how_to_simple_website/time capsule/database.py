import sys
sys.path.append('')
from sqlalchemy import create_engine, String, DateTime, select
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, sessionmaker
from datetime import datetime
from urllib.parse import parse_qs
from jinja2 import Environment, FileSystemLoader
from http.server import HTTPServer, BaseHTTPRequestHandler

# SERVER ===========================================================================================
template_env = Environment(
    loader=FileSystemLoader('templates'),
)

HOST = 'localhost'
PORT = 8080
DB_URL = 'sqlite:///capsules.db'

class HTTPHandler(BaseHTTPRequestHandler):
    def get_db_session(self):
        engine = create_engine(DB_URL)
        SessionLocal = sessionmaker(bind=engine)
        return SessionLocal()

    def do_GET(self):
        if self.path == '/':
            session = self.get_db_session()
            stmt = select(Message)
            messages = session.execute(stmt).scalars().all()
            session.close()
            now = datetime.now()
            context = {'messages': messages, 'now': now}
            html_content = self.render_template('index.html', context)
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html_content)

        elif self.path == '/create':
            html_content = self.render_template('create.html')
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(html_content)

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(safe_bytes('<h1>404 Not Found</h1>'))

    def do_POST(self):
        if self.path == '/create':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            form_data = parse_qs(post_data)
            author = form_data.get('author', [''])[0].strip()
            content = form_data.get('content', [''])[0].strip()
            unlock_str = form_data.get('unlock_date', [''])[0].strip()

            if not (author and content and unlock_str):
                self.send_response(400)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(safe_bytes('<h1>Все поля обязательны!</h1>'))
                return

            try:
                unlock_date = datetime.strptime(unlock_str, '%Y-%m-%d')
            except ValueError:
                self.send_response(400)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(safe_bytes('<h1>Неверный формат даты (YYYY-MM-DD)!</h1>'))
                return

            session = self.get_db_session()
            new_message = Message(author=author, content=content, unlock_date=unlock_date)
            session.add(new_message)
            session.commit()
            session.close()

            self.send_response(302)
            self.send_header('Location', '/')
            self.end_headers()
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(safe_bytes('<h1>404 Not Found</h1>'))

    def render_template(self, template_name, context={}):
        template = template_env.get_template(template_name)
        return template.render(context).encode('utf-8')

def safe_bytes(text):
    return text.encode('utf-8')

def start_server():
    server_address = (HOST, PORT)
    server = HTTPServer(server_address, HTTPHandler)
    print(f'Server: http://{HOST}:{PORT}/')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()

# DB ===========================================================================================
class Base(DeclarativeBase):
    pass

class Message(Base):
    __tablename__ = 'messages'
    id: Mapped[int] = mapped_column(primary_key=True)
    author: Mapped[str] = mapped_column(String(30), nullable=False)
    content: Mapped[str] = mapped_column(String(100), nullable=False)
    unlock_date: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

def create_db():
    engine = create_engine(DB_URL)
    Base.metadata.create_all(engine)

def spawn_db():
    create_db()
    engine = create_engine(DB_URL)
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()
    messages = [
        Message(author='Semyon', content='My favorite quote is: "Bla bla bla you\'r wrong bla bla." by Marcus Aurelius', unlock_date=datetime(2026, 2, 1)),
        Message(author='Kasane Teto', content='Tomorrow im locked in.', unlock_date=datetime(2026, 1, 28)),
    ]
    session.add_all(messages)
    session.commit()
    session.close()
    print('База данных инициализирована тестовыми данными')

if __name__ == '__main__':
    #spawn_db()  # Раскомментируй для инициализации БД
    start_server()
