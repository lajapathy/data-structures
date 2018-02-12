
import socket

serv_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_ip = socket.gethostname()
print server_ip
server_port = 60000
serv_sock.bind(('127.0.0.1',server_port))
serv_sock.listen(5)

while True:
    conn,address = serv_sock.accept()
    print 'sss'
    print address
    print 'Received TCP connection from '+str(address)
    print conn.getpeername()
    print conn.getsockname()
    data = conn.recv(1024)
    print data
    conn.send('Got it')
    print 'Waiting for more data'