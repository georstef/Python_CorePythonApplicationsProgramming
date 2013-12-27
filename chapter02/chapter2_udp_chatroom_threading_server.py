
# for client use -> chapter2_tcp_chatroom_threading_client

from socketserver import (UDPServer, DatagramRequestHandler, ThreadingMixIn)
from time import ctime
import threading

host = ''
port = 21000
address = (host, port)
attendees = {}

class ThreadedUDPRequestHandler(DatagramRequestHandler):
    def handle(self):
        data = self.rfile.readline().strip()
        data = data.decode('utf-8')

        if data[0:5] == 'name:':
            #first contact
            if self.client_address not in attendees:
                attendees[self.client_address] = data[5:]
                print("+++ [{0} just entered the room]".format(attendees[self.client_address]))
        else:
            if not data:
                #if empty data send then remove user from room
                print("--- [{0} left the room]".format(attendees[self.client_address]))
                del(attendees[self.client_address])
                self.socket.sendto(bytes("", 'utf-8'), self.client_address)
                return
            else:
                #else tell to everyone in the room
                self.socket.sendto(bytes("OK", 'utf-8'), self.client_address)
                print("[{0}] says: {1}".format(attendees[self.client_address], data))

        #respond ok
        self.socket.sendto(bytes("OK", 'utf-8'), self.client_address)
                

class ThreadedMixInUDPServer(ThreadingMixIn, UDPServer):
    pass

if __name__=='__main__':
    server_socket = ThreadedMixInUDPServer(address, ThreadedUDPRequestHandler)

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
