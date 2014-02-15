from http.server import CGIHTTPRequestHandler,test

if __name__=='__main__':
    test(CGIHTTPRequestHandler)

'''
run this script and then in the browser open 127.0.0.1:8000/chapter10-cgibin.html
and the Submit button calls the script in the /cgi-bin folder
'''
