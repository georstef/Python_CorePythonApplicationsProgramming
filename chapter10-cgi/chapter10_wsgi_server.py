from wsgiref.simple_server import make_server#, demo_app 
from chapter10_wsgi_client import my_app, demo_app

if __name__=='__main__':
    httpd = make_server('', 8000, demo_app) #or my_app
    print("Started app serving on port 8000...")
    httpd.serve_forever()

'''
starts listening in 127.0.0.1:8000 and when a connection is made
it calls the [demo_app] function inside "chapter10_wsgi_client"
'''
