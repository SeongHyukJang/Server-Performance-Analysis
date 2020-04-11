from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class RequestHandler(BaseHTTPRequestHandler):

    def _set_head(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_head()

    def do_GET(self):
        self._set_head()

        if self.path.endswith('data'):
            try:
                with open('data.json', 'r') as file:
                    data = json.load(file)
                    length = len(data)
            except:
                data = []
                length = 0
            self.send_header('Content-Length',str(length))
            self.wfile.write(str(data).encode())

    def do_POST(self):
        ctype = self.headers['Content-Type']

        if ctype == 'application/json':
            length = int(self.headers['Content-Length'])
            self._set_head()
            try:
                with open('data.json', 'r') as file:
                    data = json.load(file)
            except:
                data = []

            newData = json.loads(self.rfile.read(length))
            data.append(newData)

            with open('data.json', 'w') as file:
                json.dump(data, file, ensure_ascii=False, indent = 4)

def main():
    PORT = 8000
    url = ''
    server = HTTPServer((url,PORT), RequestHandler)
    print("Server on ", PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()