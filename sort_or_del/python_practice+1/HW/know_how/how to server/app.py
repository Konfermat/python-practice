from http.server import BaseHTTPRequestHandler, HTTPServer


# SERVER ==============================================================
HOST = 'localhost'
PORT = 8080

class HTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write('<!doctype html><html lang="en"><body><h2>SSSDF</h2></body></html>'.encode('utf-8'))

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

    
