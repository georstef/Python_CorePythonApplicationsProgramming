from socket import *

if __name__=='__main__':
    host = 'localhost'
    port = 21000
    buffer_size = 1024
    address = (host, port)

    #create a socket (network oriented, connectionless)
    client_socket = socket(AF_INET, SOCK_DGRAM)

    while True:
        answer = input('write something:')
        if not answer:
            break
        #send to the server that listens to this address
        client_socket.sendto(bytes(answer, 'utf-8'), address)
        data, server_address = client_socket.recvfrom(buffer_size)
        if not data:
            break
        print("received {0} from {1}".format(data.decode('utf-8'), server_address))

    client_socket.close()
