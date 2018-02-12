
import socket

client_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_ip  = '127.0.0.1'
server_port = 60000
x = client_sock.connect((server_ip,server_port))
print type(x)
print x
client_sock.send('Please send file data')
received_data = client_sock.recv(1024)
print received_data
