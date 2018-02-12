import socket

client_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_name = socket.gethostname()
print server_name
server_port = 60000
client_sock.connect(('127.0.0.1',server_port))
client_sock.send('test ')
client_sock.recv(1024)