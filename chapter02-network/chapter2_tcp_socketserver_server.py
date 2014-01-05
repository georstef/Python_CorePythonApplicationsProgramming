from socketserver import (TCPServer, StreamRequestHandler)
from time import ctime

host = ''
port = 21000
address = (host, port)

class MyRequestHandler(StreamRequestHandler):
    # the StreamRequestHandler class treats input and output sockets 
    # as file-like objects, so we will use
    # readline() to get the client message  and
    # write() to send a string back to the client
    def handle(self):
        print("connected from:", self.client_address)
        #if the received data have no NEWLINE character next line halts
        data = self.rfile.readline().strip()
        #self.wfile.write(data)
        self.wfile.write(bytes('[{0}] {1}'.format(ctime(), data.decode("utf-8")), 'utf-8'))

if __name__=='__main__':
    #create a tcp socket and pass all the receives to a handler class
    server_socket = TCPServer(address, MyRequestHandler)

    print('waiting...just waiting')
    server_socket.serve_forever()

# SocketServer receives a client connection, responds and then closes it
# this means TCP server acts more like a UDP
# this can be changed by overriding the appropriate methods 
# in our request handler classes
