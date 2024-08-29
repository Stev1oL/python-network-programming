import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('socket successfully created')
except socket.error as err:
    print(f'socket creation failed with error {err}')

port = 80

try:
    ip = socket.gethostbyname('www.google.com')
except socket.gaierror:
    print('error resolving the host')
    sys.exit()

s.connect((ip, port))
print(f'Socket has successfully connected to Host {ip} on Port {port}')