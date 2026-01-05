import http.server
import socketserver
from http import HTTPStatus
from urllib.parse import parse_qs, urlparse
import json

PORT = 8000

class SearchHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Парсим path и query параметры
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        
        if 'q' not in query_params:
            self.send_error(HTTPStatus.BAD_REQUEST.value, "Missing 'q' parameter")
            return
        
        query = query_params['q'][0]
        # Имитируем результаты поиска
        results = [
            f"Результат 1 для '{query}'",
            f"Результат 2 для '{query}'",
            f"Результат 3 для '{query}'"
        ]
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.end_headers()
        
        response_data = json.dumps({'query': query, 'results': results}, ensure_ascii=False).encode('utf-8')
        self.send_header('Content-Length', str(len(response_data)))
        self.end_headers()
        self.wfile.write(response_data)

# Запуск сервера
with socketserver.TCPServer(("", PORT), SearchHandler) as httpd:
    print(f"Сервер запущен на http://localhost:{PORT}")
    print("Тестируйте: http://localhost:8000/search?q=python")
    httpd.serve_forever()
