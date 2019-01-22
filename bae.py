import socket

#socket.SOCK_STREAM indicates TCP
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("localhost", 12345))
serversocket.listen(1)

(clientsocket, address) = serversocket.accept()
msg = clientsocket.recv(1024)
print("server recieved "+msg.decode("utf-8"))

msg = b"""
HTTP/1.1
Content-Type: text/html

<html>
<body>
<b>Hello World</b>
</body>
</html>

"""


print(b"server sending reply")
clientsocket.send(msg)