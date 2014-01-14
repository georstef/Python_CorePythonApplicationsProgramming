#!/usr/bin/env python

import ctypes
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_error(404, 'File Not Found - POST: %s' % self.path)

    def do_GET(self):
        try:
            f = open('readme.md', 'r') #current dir
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f.read().encode('utf-8'))# must be bytes type
            f.close()
        except IOError:
            self.send_error(404, 'File Not Found - GET: %s' % self.path)
            
def main():
    try:
        if ctypes.windll.shell32.IsUserAnAdmin():
            print('admin')
        else:
            print('not admin')

        server = HTTPServer(('127.0.0.1', 8000), MyHandler)
        print('Welcome to the machine...')
        print('Press ^C once or twice to quit')
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down server')
        server.socket.close()

if __name__ == '__main__':
    main()
