from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class RequestHandler(BaseHTTPRequestHandler):

    def _set_head(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length',4)
        self.end_headers

    def do_HEAD(self):
        self._set_head()

    def do_GET(self):
        self._set_head()
        self.wfile.write(json.dumps({'hello' : 'world', 'recieved' : 'ok'}).encode())

    def do_POST(self):
        ctype = self.headers['Content-Type']

        if ctype == 'application/json':
            length = int(self.headers['Content-Length'])
            message = json.loads(self.rfile.read(length))

            message['recieved'] = 'ok'

            self._set_head()
            self.wfile.write(json.dumps(message).encode())


def main():
    PORT = 8000
    url = ''
    server = HTTPServer((url,PORT), RequestHandler)
    print("Server on ", PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()