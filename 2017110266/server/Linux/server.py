from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import lauda

class RequestHandler(BaseHTTPRequestHandler):

    def __init__(self, request, client_address, server):
        self.stopWatch = lauda.StopWatch()
        super().__init__(request,client_address,server)

    def writeResults(self,newData,resource,method):
        with open('ServerResult.json','r') as file:
            data = json.load(file)

        data['ServerLanguage']['python'][resource][method].append(newData)

        with open('ServerResult.json','w') as file:
            json.dump(data,file,ensure_ascii=False,indent=4)

    def do_GET(self):

        if self.path.endswith('os'):
            self.send_response(200)
            self.end_headers()
            self.wfile.write('Linux'.encode())
            
        if self.path.endswith('json'):
            self.stopWatch.start()

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            with open('GETdata.json', 'r') as file:
                data = json.load(file)
            self.end_headers()
            self.wfile.write(str(data).encode())
        
            self.stopWatch.stop()
            self.writeResults(self.stopWatch.elapsed_time * 1000,'json','GET')

        if self.path.endswith('calc'):
            self.stopWatch.start()

            self.send_response(200)
            self.end_headers()
            x = 1.0
            pi = 1.0
            i = 2
            while i != 1000000:
                x *= -1
                pi += x / (2*i - 1)
                i +=1
            pi *= 4
            self.wfile.write(str(pi).encode())

            self.stopWatch.stop()
            self.writeResults(self.stopWatch.elapsed_time*1000,'calc','GET')
        
        if self.path.endswith('html'):
            self.stopWatch.start()

            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()

            with open('index.html','rb') as f:
                self.wfile.write(f.read())
            
            self.stopWatch.stop()
            self.writeResults(self.stopWatch.elapsed_time * 1000,'html','GET')

    def do_POST(self):
        ctype = self.headers['Content-Type']

        if ctype == 'application/json':
            self.stopWatch.start()

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

            self.stopWatch.stop()
            self.writeResults(self.stopWatch.elapsed_time * 1000,'json','POST')

def main():
    PORT = 8000
    url = ''
    server = HTTPServer((url,PORT), RequestHandler)
    print("Server on PORT", PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()