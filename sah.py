import socket

#socket.SOCK_STREAM indicates TCP
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(("localhost", 12345))

msg = b"Hello World from client"

print(b"client sending: "+msg)
clientsocket.send(msg)

msg = clientsocket.recv(1024)
print(msg.decode("utf-8"))