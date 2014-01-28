from time import ctime
from wsgiref.simple_server import make_server#, demo_app 
from chapter10_wsgi_client import my_app, demo_app

def middleware_app(environ, start_response):
    data = demo_app(environ, start_response)
    new_data = []
    for d in data:
        new_data.append('[{0}] {1}'.format(ctime(), d).encode('utf-8')) 
    return new_data

class middleware_app_class():
    def __init__(self, app):
        self.orig_app = app

    def __call__(self, *stuff):
        data = self.orig_app(*stuff)
        new_data = []
        for d in data:
            new_data.append('[{0}] {1}'.format(ctime(), d).encode('utf-8')) 
        return new_data

if __name__=='__main__':
    #example with function
    httpd = make_server('', 8000, middleware_app)
    #example with class
    #httpd = make_server('', 8000, middleware_app_class(demo_app))
    print("Started app serving on port 8000...")
    httpd.serve_forever()
