from http.server import HTTPServer, BaseHTTPRequestHandler
import os
from io import BytesIO
import posixpath
import urllib
import shutil
import cgi
import re

class RequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        f = self.send_head()
        if f:
            self.copyfile(f,self.wfile)
            f.close()

    def do_POST(self):
        r, info = self.deal_post_data()
        print((r, info, "by: ", self.client_address))

        f = BytesIO()
        f.write(b'<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">')
        f.write(b"<html>\n<title>Upload Result Page</title>\n")
        f.write(b"<body>\n<h2>Upload Result Page</h2>\n")
        f.write(b"<hr>\n")

        if r:
            f.write(b'<strong>Success:</strong>')
        else:
            f.write(b'<strong>Failed:</strong>')
        
        f.write(info.encode())
        f.write(("<br><a href=\"%s\">back</a>" % self.headers['referer']).encode())
        f.write(b"</body>\n</html>\n")

        length = f.tell()
        f.seek(0)
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Type", str(length))
        self.end_headers()
        if f:
            self.copyfile(f, self.wfile)
            f.close()

    def deal_post_data(self):
        content_type = self.headers['Content-Type']
        if not content_type:
            return (False, "Content-Type header doesn't contain boundary")

        boundary = content_type.split('=')[1].encode()
        remainbytes = int(self.headers['content-length'])
        line = self.rfile.readline()
        remainbytes -= len(line)

        if not boundary in line:
            return (False, "Content NOT begin with boundary")

        line = self.rfile.readline()
        remainbytes -= len(line)
        
        fn = re.findall(r'Content-Disposition.*name="file"; filename="(.*)"', line.decode())
        if not fn:
            return (False, "Can't find out file name...")

        path = self.translate_path(self.path)
        fn = os.path.join(path, fn[0])

        line = self.rfile.readline()
        remainbytes -= len(line)

        try:
            out = open(fn,'wb')
        except IOError:
            return (False, "Can't create file to write, do you have permission to write?")
        
        preline = self.rfile.readline()
        remainbytes -= len(preline)
        
        while remainbytes > 0:
            line = self.rfile.readline()
            remainbytes -= len(line)
            if boundary in line:
                preline = preline[0:-1]
                if preline.endswith(b'\r'):
                    preline = preline[0:-1]
                out.write(preline)
                out.close()
                return (True, "File '%s' upload success!" % fn)
            else:
                out.write(preline)
                preline = line
        
        return (False, "Unexpect Ends of data...")

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
        self.send_header("Content-Type", "text/html")
        fs = os.fstat(f.fileno())
        self.send_header("Content-length", str(fs[6]))
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
        for word in words:
            _, word = os.path.splitdrive(word)
            _, word = os.path.split(word)
            if word in (os.curdir, os.pardir): continue
            path = os.path.join(path, word)
        return path

    def list_directory(self,path):
        List = os.listdir(path)
        
        List.sort(key = lambda a : a.lower())
        f = BytesIO()
        displaypath = cgi.escape(urllib.parse.unquote(self.path))
        f.write(("<html>\n<title>Directory Listing</title>\n").encode())
        f.write(("<body>\n<h2>Directory : %s</h2>\n" % displaypath).encode())
        f.write(b'<hr>\n')
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
            length = f.tell()
            f.seek(0)
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.send_header("Content-Length", str(length))
            self.end_headers()
            return f


def main():
    PORT = 8000
    server = HTTPServer(('', PORT), RequestHandler)
    print("Server on port ", PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()
