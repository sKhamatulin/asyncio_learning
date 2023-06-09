import socket
from select import select


tasks = []

to_read = {}

to_write = {}


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
        # read
        yield ('read', server_socket)
        client_socket, address = server_socket.accept()
        print('Connection from ', address)
        tasks.append(client(client_socket))


def client(client_socket):
    while True:
        yield ('read', client_socket)
        print('Before recv')
        # read
        request = client_socket.recv(4096)

        if not request:
            break

        else:
            # write
            response = 'Hello World!\n'.encode()
            yield ('write', client_socket)
            client_socket.send(response)

    print('End inner loop')
    client_socket.close()


def event_loop():

    while any([tasks, to_read, to_write]):

        while not tasks:
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])

            for sock in ready_to_read: 
                tasks.append(to_read.pop(sock))

            for sock in ready_to_write: 
                tasks.append(to_write.pop(sock))

        try:
            task = tasks.pop(0)
            reason, sock = next(task)

            if reason == 'read':
                to_read[sock] = task
            if reason == 'write':
                to_write[sock] = task

        except StopIteration:
            print('Done')


tasks.append(server())
event_loop()
