from wsgiref.simple_server import make_server#, demo_app 
from chapter10_wsgi_client import my_app, demo_app

if __name__=='__main__':
    httpd = make_server('', 8000, demo_app) #or my_app
    print("Started app serving on port 8000...")
    httpd.serve_forever()
