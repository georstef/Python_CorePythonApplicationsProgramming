from socket import *

if __name__=='__main__':
    host = 'localhost'
    port = 5555
    buffer_size = 4096
    address = (host, port)


    while True:
        #create a socket (network oriented, connection oriented)
        client_socket = socket(AF_INET, SOCK_STREAM)
        
        #connect to the server that listens to this address
        client_socket.connect(address)
  
        command = input('give command:')
        if not command:
            break
        key = input('give key:')
        value = input('give value:')
        value_type = input('give value type:')

        client_socket.send(bytes('{0};{1};{2};{3}'.format(command, key, value, value_type), 'utf-8'))
        data = client_socket.recv(buffer_size)
        if not data:
            break
        print(data)
        #print(data[1].decode('utf-8'))

        client_socket.close()
