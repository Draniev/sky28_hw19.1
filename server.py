from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer


class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open('index.html', 'rb') as file:
            self.wfile.write(file.read())


if __name__ == "__main__":
    host = '127.0.0.1'
    port = 8000
    server = TCPServer((host, port), MyHandler)

    print(f"Server started at http://{host}:{port}")
    server.serve_forever()
