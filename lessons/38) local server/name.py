# основные классы для создания и обработки запросов
from http.server import HTTPServer, SimpleHTTPRequestHandler, BaseHTTPRequestHandler

from sqlalchemy import PoolResetState


# зачем нам это:
# для проверок статусов кода
# формировать тело ответа
# обработка ответов
# обработка файлов
# для тестирования

class CustomHTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        html_content = '''
            <!DOCTYPE html>
            <html>
            <head>>/head>
            <body>
            <p>Пример работы сервера</p>
            <p>Текущий путь {path}</p>
            <p>Время на сервере: {time}</p>
            </body>
            </html>
        '''
        from datetime import datetime
        html_content = html_content.format(
            path=self.path,
            time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )
        # порядок действий
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset="utf-8"') # если указать другой форат то он не поймет
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))

server = HTTPServer(('', 8000), CustomHTTPHandler)
print('http://localhost:8000/')
server.serve_forever()

#MIME - типы # сообщения браузеру
#
# 1) text, image, application, audio, video
# 2) plain, html, json, css, javascript

обработка основных методов протокола
BaseHTTPRequestHandler:
    # запрос(request)
    self.requestline # строка запроса
    self.command = 'GET' POST
    self.header = 'заголовки запроса'
    self.rfile = 'оток для чтения запроса'
    #Ответ(response)
    self.wfile = 'поток для записи ответа'
    self.send_header()
    self.end_headers()
    log_message()
    send_error()

    class h(HTTPServer):
        server_address = (host, port)
        handler_class = 'класс обработчик'
        serve_forever = 'запускает бесконечный цикл обработки запросов'
        serve_close() = 'корректно закреот сервер'
        