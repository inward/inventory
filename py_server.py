from http.server import BaseHTTPRequestHandler, HTTPServer
import gs
class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        if path == "/":
            path = "pages/index.html"
        if path.startswith('/'):
            path = path[1:]
        if path.startswith('part?'):
            gs.check_part(path.split('?')[1])
            path = "pages/self_close.html"
        try:
            path = "pages/self_close.html"
            file  = open(path, 'r', encoding='utf-8')
            print(path)
        except FileNotFoundError:
            file  = open("pages/404.html", 'r')

        message = file.read()
        file.close()
        self.wfile.write(bytes(message, "utf8"))
        return



server = HTTPServer(('192.168.27.30', 8083), myHandler)
server.serve_forever()