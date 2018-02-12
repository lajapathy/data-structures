
import socket

client_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_ip = '127.0.0.1'
server_port = 60000
server_addr = (server_ip,server_port)
client_sock.sendto('lajju',server_addr)
x = client_sock.recvfrom(1024)
print x
print x[0]
client_sock.close()