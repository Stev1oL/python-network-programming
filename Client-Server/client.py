import socket

s = socket.socket()

localhost = '127.0.0.1'
port = 56789

s.connect((localhost, port))
print(s.recv(1024))

s.close()