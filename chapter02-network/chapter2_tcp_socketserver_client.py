from socket import *

host = 'localhost'
port = 21000
buffer_size = 1024
address = (host, port)

if __name__=='__main__':

    while True:
        answer = input('write something:')
        if not answer:
            break

        #create a socket (network oriented, connection oriented)
        client_socket = socket(AF_INET, SOCK_STREAM)
        #connect to the server that listens to this address
        client_socket.connect(address)

        #send data (with a '\n')   <- needs NEWLINE
        client_socket.send(bytes(answer+'\n', 'utf-8'))
        #get response
        data = client_socket.recv(buffer_size)
        if not data:
            break

        print(data.decode('utf-8'))

        # since socketserver always closes the connection
        # the client needs to close it too
        # and reopen it everytime it needs to send something
        client_socket.close()
