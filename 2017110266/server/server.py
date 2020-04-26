from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path.endswith('data'):
            try:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                with open('GETdata.json', 'r') as file:
                    data = json.load(file)
                    length = len(data)
            except:
                data = []
                length = 0
            self.send_header('Content-Length',str(length))
            self.wfile.write(str(data).encode())
            self.end_headers()
        
        if self.path.endswith('calc'):
            self.send_response(200)
            try:
                a_0 = 1
                a_n = a_0
                count = 0
                while(count != 10000):
                    a_n1 = (a_n/2) + (1/a_n)
                    a_n = a_n1
                    count += 1
                #print("{:.20f}".format(a_n))
                self.wfile.write(str(a_n).encode())
                self.end_headers()
            except:
                pass

        if self.path.endswith('html'):
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            with open('GEThtml.html','r') as f:
                self.wfile.write(f.read().encode())
            
            

    def do_POST(self):
        ctype = self.headers['Content-Type']

        if ctype == 'application/json':
            length = int(self.headers['Content-Length'])
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            try:
                with open('POSTdata.json', 'r') as file:
                    data = json.load(file)
            except:
                data = []

            newData = json.loads(self.rfile.read(length))
            data.append(newData)

            with open('POSTdata.json', 'w') as file:
                json.dump(data, file, ensure_ascii=False, indent = 4)

def main():
    PORT = 8000
    url = ''
    server = HTTPServer((url,PORT), RequestHandler)
    print("Server on ", PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()