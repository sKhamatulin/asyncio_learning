import socket

# domain 5000

# create a socket  INET is IP4   SOCK_STREAM is TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# refresh the port used after end of script
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# link to the port
server_socket.bind(('localhost', 5000))
server_socket.listen()

# start to chanal communocate to client
while True:
    # get a input connection
    print('Before accept')
    client_socket, address = server_socket.accept()
    print('Connection from ', address)

    # try to get request by client
    while True:
        # value for cllient's request, buffer size is 4Kb
        print('Before recv')
        request = client_socket.recv(4096)

        if not request:
            break

        else:
            # value for server response, encode to bites
            response = 'Hello World!\n'.encode()
            # send response to client
            client_socket.send(response)

    print('End inner loop')
    client_socket.close()
