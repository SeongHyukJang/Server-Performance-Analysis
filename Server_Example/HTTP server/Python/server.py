from http.server import HTTPServer, BaseHTTPRequestHandler

tasklist = ['Task 1', 'Task 2', 'Task 3']


# Handler는 http method들을 관리
class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/tasklist'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            output = ''
            output += '<html><body>'
            output += '<h1>Task List</h1>'

            for task in tasklist:
                output += task
                output += '</br>'

            output += '<h3><a href = "/tasklist/new"> Add New Task List</a></h3>'
            output += '</body></html>' 
            self.wfile.write(output.encode())

        elif self.path.endswith('/new'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            output = ''
            output += '<html><body>'
            output += '<h1>Add New Task</h1>'

            output += '<form method="POST" enctype="multipart/form-data" action="/tasklist/new">'
            output += '<input name="task" type="text" placeholder="Add new task">'
            output += '<input type="submit" value="Add">'
            output += '</form>'
            output += '</body></html>'

            self.wfile.write(output.encode())

        else:
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            
            output = ''
            output += '<html><body>'
            output += '<h1>Welcome!</h1>'
            output += '<h3><a href = "/tasklist">Task List</a></h3>'
            output += '</body></html>'
            self.wfile.write(output.encode())





def main():
    PORT = 8080
    server = HTTPServer(('', PORT), requestHandler)
    print("Server running on port %s" %PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()