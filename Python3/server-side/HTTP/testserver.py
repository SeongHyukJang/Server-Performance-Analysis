from http.server import HTTPServer, BaseHTTPRequestHandler
import shutil
import os

class RequestHandler(BaseHTTPRequestHandler):

    # def _set_response(self):
    #     self.send_response(200)
    #     self.send_header('Content-Type', 'text/html')
    #     #self.send_header('Content-Type', 'multipart/form-data')
    #     self._set_head()
    #     self.end_headers()

    def _set_head(self):
        try:
            f = open(self.path,'rb')
            fileSize = os.fstat(f.fileno())
            self.send_header("Content-Length", str(fileSize[6]))
        except:
            pass

    def do_GET(self):
        #self._set_response()
        self.send_response(200)
        #self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Type', 'application/json')
        self._set_head()
        self.end_headers()
        if self.path.endswith('comic.png'):
            shutil.copyfileobj(open(self.path[1:],'rb'), self.wfile)
        if self.path.endswith('db.sqlite3'):
            print(self.path)
            

    def do_POST(self):
        try:
            length = int(self.headers['Content-Length'])
            data = self.rfile.read(length)

            self.send_response(200)
            self.send_header('Content-Type', 'multipart/form-data')
            self._set_head()
            self.end_headers()
            self.wfile.write(b"=======POST======")
        except:
            print("Error")
            pass



def main():
    PORT = 8000
    url = ''
    server = HTTPServer((url,PORT), RequestHandler)
    print("Server on ", PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()