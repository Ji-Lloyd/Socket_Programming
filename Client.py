import socket

socket_client = socket.socket()

socket_client.connect(('localhost', 9999))

ui_name = input("Enter name:")
ui_age = input("Enter age:")

socket_client.send(bytes(ui_name, 'utf-8'))
socket_client.send(bytes(ui_age, 'utf-8'))

print(socket_client.recv(1024).decode())

