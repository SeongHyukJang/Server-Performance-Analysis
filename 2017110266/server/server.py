from http.server import HTTPServer, BaseHTTPRequestHandler
import os
from io import BytesIO
import posixpath
import urllib
import shutil
import cgi

class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        f = self.send_head()
        self.copyfile(f,self.wfile)
        f.close()

    def send_head(self):
        path = self.translate_path(self.path)
        
        f = None
        if os.path.isdir(path):
            if not self.path.endswith('/'):
                self.send_response(301)
                self.send_header("Location", self.path + "/")
                self.end_headers()
                return None
            for index in "index.html", "index.htm":
                index = os.path.join(path, index)
                if os.path.exists(index):
                    path = index
                    break
            else:
                return self.list_directory(path)
        
        f = open(path,'rb')

        self.send_response(200)
        self.end_headers()
        return f

    def copyfile(self, source, outputfile):
        shutil.copyfileobj(source, outputfile)

    def translate_path(self, path):
        path = path.split('?', 1)[0]
        path = path.split('#',1)[0]
        path = posixpath.normpath(urllib.parse.unquote(path))
        words = path.split('/')
        words = filter(None, words)
        path = os.getcwd()
        return path

    def list_directory(self,path):
        List = os.listdir(path)
        
        List.sort(key = lambda a : a.lower())
        f = BytesIO()
        displaypath = cgi.escape(urllib.parse.unquote(self.path))
        f.write(("<html>\n<title>Directory Listing</title>\n").encode())
        f.write(("<body>\n<h2>Directory : %s</h2>\n" % displaypath).encode())

        for name in List:
            fullname = os.path.join(path, name)
            displayname = linkname = name
            if os.path.isdir(fullname):
                displayname = name + "/"
                linkname = name + "/"
            if os.path.islink(fullname):
                displayname = name + "@"
            f.write(('<li><a href="%s">%s</a>\n' % (urllib.parse.quote(linkname), cgi.escape(displayname))).encode())
            f.write(b"</ul>\n<hr>\n</body>\n</html>\n")
            f.seek(0)
            self.send_response(200)
            self.end_headers()
            return f


def main():
    PORT = 8000
    server = HTTPServer(('', PORT), RequestHandler)
    print("Server on port ", PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()
