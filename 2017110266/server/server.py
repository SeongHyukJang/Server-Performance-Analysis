from http.server import HTTPServer, BaseHTTPRequestHandler
import shutil
import os

class RequestHandler(BaseHTTPRequestHandler):

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-Type', 'multipart/form-data')
        self._set_head()
        self.end_headers()

    # def _html(self, message):
    #     content = f'<html><body>{message}</body></html>'
    #     return content.encode()

    def _set_head(self):
        try:
            f = open(self.path,'rb')
            fileSize = os.fstat(f.fileno())
            self.send_header("Content-Length", str(fileSize[6]))
        except:
            pass

    def do_GET(self):
        self._set_response()
        if self.path.endswith('comic.png'):
            shutil.copyfileobj(open(self.path[1:],'rb'), self.wfile)

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        data = self.rfile.read(length)

        self._set_response()
        self.wfile.write(b"POST SUCCESS")



def main():
    PORT = 8000
    url = ''
    server = HTTPServer((url,PORT), RequestHandler)
    print("Server on ", PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()