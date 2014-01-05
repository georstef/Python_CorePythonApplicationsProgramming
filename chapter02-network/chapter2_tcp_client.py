from socket import *

if __name__=='__main__':
    host = 'localhost'
    port = 21000
    buffer_size = 1024
    address = (host, port)

    #create a socket (network oriented, connection oriented)
    client_socket = socket(AF_INET, SOCK_STREAM)
    #connect to the server that listens to this address
    client_socket.connect(address)

    while True:
        answer = input('write something:')
        if not answer:
            break
        client_socket.send(bytes(answer, 'utf-8'))
        data = client_socket.recv(buffer_size)
        if not data:
            break
        #print(data)
        print(data.decode('utf-8'))

    client_socket.close()
