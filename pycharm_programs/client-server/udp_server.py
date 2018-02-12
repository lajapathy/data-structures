
import socket

server_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_ip = '127.0.0.1'
server_port = 60000
server_sock.bind((server_ip,server_port))

while True:
    # Wait for next client
    print 'Waiting for client data ...'
    data, address = server_sock.recvfrom(1024)
    print address
    server_sock.sendto(data, address)

