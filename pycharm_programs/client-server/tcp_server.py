
import socket

server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_ip = '127.0.0.1'
server_port = 60000
server_sock.bind((server_ip,server_port))
server_sock.listen(5)

while True:
    # Wait for next client
    print 'Waiting for client connection ...'
    conn_obj, addr = server_sock.accept()
    print 'client IP : ' + str(conn_obj.getpeername())
    print 'Server IP : ' + str(conn_obj.getsockname())
    #Inform client that server has accepted the connection.i.e, TCP connection formed
    conn_obj.send('TCP formed successfuly. Send request\n')

    #Wait for client to send a request
    conn_obj.recv(1024)

    #Send data to client
    for line in open('mytext.txt','r'):
        conn_obj.send(line)


