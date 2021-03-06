from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import lauda

class RequestHandler(BaseHTTPRequestHandler):

    def __init__(self, request, client_address, server):
        self.stopWatch = lauda.StopWatch()
        super().__init__(request,client_address,server)

    def writeResults(self,newData,resource,method):
        with open('ServerSpeedResult.json','r') as file:
            data = json.load(file)

        data['ServerLanguage']['python'][resource][method].append(newData)

        with open('ServerSpeedResult.json','w') as file:
            json.dump(data,file,ensure_ascii=False,indent=4)

    def do_GET(self):
            
        if self.path.endswith('server-speed/json'):
            self.stopWatch.start()

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            with open('GETdata.json', 'r') as file:
                data = json.load(file)
            self.end_headers()
            self.wfile.write(str(data).encode())
        
            self.stopWatch.stop()
            self.writeResults(self.stopWatch.elapsed_time * 1000,'json','GET')
            
        
        elif self.path.endswith('json'):
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            with open('GETdata.json', 'r') as file:
                data = json.load(file)
            self.end_headers()
            self.wfile.write(str(data).encode())

        if self.path.endswith('server-speed/calc'):
            self.stopWatch.start()

            self.send_response(200)
            self.end_headers()
            x = 1.0
            pi = 1.0
            i = 2
            while i != 100000:
                x *= -1
                pi += x / (2*i - 1)
                i +=1
            pi *= 4
            self.wfile.write(str(pi).encode())

            self.stopWatch.stop()
            self.writeResults(self.stopWatch.elapsed_time*1000,'calc','GET')

        elif self.path.endswith('calc'):
            self.send_response(200)
            self.end_headers()
            x = 1.0
            pi = 1.0
            i = 2
            while i != 10000:
                x *= -1
                pi += x / (2*i - 1)
                i +=1
            pi *= 4
            self.wfile.write(str(pi).encode())

        if self.path.endswith('server-speed/html'):
            self.stopWatch.start()

            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            with open('index.html','rb') as f:
                self.wfile.write(f.read())
            
            self.stopWatch.stop()
            self.writeResults(self.stopWatch.elapsed_time*1000,'html','GET')
        
        elif self.path.endswith('html'):

            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            with open('index.html','rb') as f:
                self.wfile.write(f.read())

    def do_POST(self):
        ctype = self.headers['Content-Type']
        if self.path.endswith('server-speed/post'):
            if ctype == 'application/json':
                self.stopWatch.start()

                length = int(self.headers['Content-Length'])
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()

                try:
                    with open('POSTdataPY.json', 'r') as file:
                        data = json.load(file)
                except:
                    data = []

                newData = json.loads(self.rfile.read(length))
                data.append(newData)

                with open('POSTdataPY.json', 'w') as file:
                    json.dump(data, file, ensure_ascii=False, indent = 4)

                self.stopWatch.stop()
                self.writeResults(self.stopWatch.elapsed_time * 1000,'json','POST')


        else:
            if ctype == 'application/json':
                length = int(self.headers['Content-Length'])
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()

                try:
                    with open('POSTdataPY.json', 'r') as file:
                        data = json.load(file)
                except:
                    data = []

                newData = json.loads(self.rfile.read(length))
                data.append(newData)

                with open('POSTdataPY.json', 'w') as file:
                    json.dump(data, file, ensure_ascii=False, indent = 4)

def main():
    PORT = 8000
    url = ''
    server = HTTPServer((url,PORT), RequestHandler)
    print("Server on PORT", PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()