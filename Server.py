import socket

socket_server = socket.socket()
print('Server Created')

socket_server.bind(('localhost', 9999))

socket_server.listen(3)
print('Waiting for connections')

while True:

    socket_client, address = socket_server.accept()
    ui_name = socket_client.recv(1024).decode()
    ui_age = socket_client.recv(1024).decode()
    ui_address = socket_client.recv(1024).decode()

    print("Connected with", address)
    print("Client:", ui_name)
    print("Client's Age:", ui_age)
    print("Client's Location:", ui_address)

    socket_client.send(bytes('Welcome to Allheaven!', 'utf-8'))

    socket_client.close()
