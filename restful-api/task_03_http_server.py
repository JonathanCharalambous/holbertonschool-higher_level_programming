import http.server
import socketserver
import json

PORT = 8000
class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        
        if self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {

                "name" : "John",
                "age" : 30,
                "city" : "New York"

            }

            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {
                "status": "OK",
            }

            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {

                "version" : "1.0",
                "description" : "A simple API built with http.server",

            }

            self.wfile.write(json.dumps(data).encode('utf-8'))

        elif self.path == '/':

            self.send_response(200)

            self.send_header("Content-type", "text/html")
            self.end_headers()

            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {
                "error": "Not Found",
                "message": "The requested resource was not found."
            }

            self.wfile.write(json.dumps(data).encode('utf-8'))

def run_server():
    with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
        print(f"Serving on port {PORT}")
        httpd.serve_forever()

if __name__ == '__main__':
    run_server()