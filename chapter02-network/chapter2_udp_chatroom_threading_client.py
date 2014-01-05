from socket import *

host = 'localhost'
port = 21000
buffer_size = 1024
address = (host, port)

if __name__=='__main__':

    name = input('Give name:')
    if not name:
        print('No name, no chat!!!')
    
    #create a socket (network oriented, connectionless)
    client_socket = socket(AF_INET, SOCK_DGRAM)

    #send [name] to the server that listens to this address
    client_socket.sendto(bytes("name:"+name+'\n', 'utf-8'), address)
    data, server_address = client_socket.recvfrom(buffer_size)
    #print(data.decode('utf-8'))

    while name:

        mydata = input('say something:')
        if not mydata:
            name = ""

        #send [data] (with a '\n')   <- needs NEWLINE
        client_socket.sendto(bytes(mydata+'\n', 'utf-8'), address)
        data, server_address = client_socket.recvfrom(buffer_size)
    
    client_socket.close()
