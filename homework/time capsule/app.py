from http.server import BaseHTTPRequestHandler, HTTPServer
from jinja2 import Environment, FileSystemLoader

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from database import Message
from datetime import datetime
from urllib.parse import parse_qs


# SERVER ==============================================================
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
            self.send_response(302)
            self.send_header('Location', '/index')
            self.end_headers()
        elif self.path == '/index':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            session = self.get_db_session()
            stmt = select(Message)
            messages = session.execute(stmt).scalars().all()
            session.close()    
            
            now = datetime.now()
            
            env = Environment(
            loader=FileSystemLoader('templates')
            )
            context = {
                'messages': messages,
                'now': now,
            }
            
            template = env.get_template('index.html')
            html_content = template.render(context)
            self.wfile.write(html_content.encode())
            
        elif self.path == '/create':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            env = Environment(loader=FileSystemLoader('templates'))
            context = {}
            template = env.get_template('create.html')
            html_content = template.render(context)
            
            self.wfile.write(html_content.encode())
        
        elif self.path == '/':
            self.response(200)
            self.send_header('Location', '/index')
            self.end_headers()
            
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write('<h1>404 Not Found</h1>'.encode('utf-8'))
         
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
            self.send_header('Location', '/index')
            self.end_headers()
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(safe_bytes('<h1>404 Not Found</h1>'))        


def run_server():
    server_address = (HOST, PORT)
    server = HTTPServer(server_address, HTTPHandler)
    print(f'http://{HOST}:{PORT}/')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()

if __name__ == '__main__':
    run_server()

    
