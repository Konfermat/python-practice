import http.server
import socketserver

PORT = 8000

# Define a custom handler to process requests
class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"This is my test message")

# Start the server
with socketserver.TCPServer(("", PORT), MyRequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    print(f"Visit http://localhost:{PORT}")
    httpd.serve_forever()
