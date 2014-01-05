
# for client use -> chapter2_tcp_socketserver_client

from socketserver import (TCPServer, StreamRequestHandler, ThreadingMixIn)
from time import ctime
import threading

host = ''
port = 21000
address = (host, port)

class ThreadedTCPRequestHandler(StreamRequestHandler):
    def handle(self):
        print("connected from:", self.client_address)
        data = self.rfile.readline().strip()
        self.wfile.write(bytes('[{0}] {1}'.format(ctime(), data.decode("utf-8")), 'utf-8'))    

class ThreadedMixInTCPServer(ThreadingMixIn, TCPServer):
    pass

if __name__=='__main__':
    server_socket = ThreadedMixInTCPServer(address, ThreadedTCPRequestHandler)

    # Start a thread with the server
    # a new thread will then start for each request
    server_thread = threading.Thread(target=server_socket.serve_forever, daemon=True)

    # Exit the server thread when the main thread terminates
    # server_thread.daemon = True <- ???

    server_thread.start()

    print("Server loop in thread: ", server_thread.name)

'''
A thread can be flagged as a “daemon thread”.
The significance of this flag is that the entire Python program exits
when only daemon threads are left.
The initial value is inherited from the creating thread.
The flag can be set through the daemon property.
'''
