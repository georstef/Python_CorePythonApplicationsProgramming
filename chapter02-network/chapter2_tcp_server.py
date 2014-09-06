from socket import *
from time import ctime

if __name__=='__main__':
    host = ''
    port = 21000
    buffer_size = 1024
    address = (host, port)

    #create a socket (network oriented, connection oriented)
    server_socket = socket(AF_INET, SOCK_STREAM)
    #bind the socket to an address
    server_socket.bind(address)
    server_socket.listen(5)

    while True:
        print('waiting...just waiting')
        client_socket, client_address = server_socket.accept()
        #next line is reached only when a client connects
        print('connected from ->', client_address)
        while True:
            #this continues until client sends nothing
            data = client_socket.recv(buffer_size)
            if not data:
                break
            #client_socket.send('[{0}] {1}'.format(ctime(), data))
            client_socket.send(bytes('[{0}] {1}'.format(ctime(), data.decode('utf-8')), 'utf-8'))
            client_socket.close()
    
    server_socket.close()
