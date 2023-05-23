import socket
from select import select

# .fileno() is method for select lib, so this method can return file descriptor (num of file, int num)

# value for list of sockets that need to monitoring
to_monitor = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5000))
server_socket.listen()


# function for get connection
def accept_connection(server_socket):
    client_socket, address = server_socket.accept()
    print('Connection from ', address)
    to_monitor.append(client_socket)


# function for sending messege to client
def send_message(client_socket):
    request = client_socket.recv(4096)

    if request:
        response = 'Hello World!\n'.encode()
        client_socket.send(response)
    else:
        client_socket.close()


def event_loop():
    while True:
        # unpack the select's object. It has tree lists: for_read, for_write and for_errors
        ready_to_read, _, _ = select(to_monitor, [], [])
        for sock in ready_to_read:
            if sock is server_socket:
                accept_connection(sock)
            else:
                send_message(sock)


if __name__ == '__main__':
    # add to value the list of sockets
    to_monitor.append(server_socket)
    event_loop()
