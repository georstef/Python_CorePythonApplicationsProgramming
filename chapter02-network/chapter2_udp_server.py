from socket import *
from time import ctime

if __name__=='__main__':
    host = ''
    port = 21000
    buffer_size = 1024
    address = (host, port)

    #create a socket (network oriented, connectionless)
    server_socket = socket(AF_INET, SOCK_DGRAM)
    #bind the socket to an address
    server_socket.bind(address)

    while True:
        print('udp waiting...just waiting')
        #receive data and sender address
        data, client_address = server_socket.recvfrom(buffer_size)
        #respond
        server_socket.sendto(bytes('[{0}] {1}'.format(ctime(), data.decode('utf-8')), 'utf-8'), client_address)

        print("...received something and returned to:", client_address)
    
    server_socket.close()
