import socket
import selectors

selector = selectors.DefaultSelector()


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    # registor connection
    selector.register(fileobj=server_socket,
                      events=selectors.EVENT_READ,
                      data=accept_connection)


# function for get connection
def accept_connection(server_socket):
    client_socket, address = server_socket.accept()
    print('Connection from ', address)

    # registor clients
    selector.register(fileobj=client_socket,
                      events=selectors.EVENT_READ,
                      data=send_message)


# function for sending messege to client
def send_message(client_socket):
    request = client_socket.recv(4096)

    if request:
        response = 'Hello World!\n'.encode()
        client_socket.send(response)
    else:
        selector.unregister(client_socket)
        client_socket.close()


def event_loop():
    while True:

        events = selector.select()  # return a tuple (key, events)
        for key, _ in events:
            callback = key.data
            callback(key.fileobj)


if __name__ == '__main__':
    # start server
    server()
    event_loop()
