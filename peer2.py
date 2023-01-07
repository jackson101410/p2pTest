import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8080))

client.send(bytes('I am CLIENT\n', 'utf-8'))

from_server = client.recv(4096)

client.close()

print (str(from_server))