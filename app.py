from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Hello from DevOps Project 🚀".encode())

with HTTPServer(("", PORT), Handler) as server:
    print(f"Server running on port {PORT}")
    server.serve_forever()
