import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print "Correct usage: script, Server IP address, port number"
    exit()
UserID = raw_input("Username: ")
Password = raw_input("Password: ")
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
#UserID = str(sys.argv[3])
server.connect((IP_address, Port))
server.send(UserID + ' ' + Password)

while True:
    sockets_list = [sys.stdin, server]
    read_sockets,write_socket, error_socket = select.select(sockets_list, [], [])
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            if message == '404':
                print 'User not exist, connection lost!'
                server.close()
                sys.exit()
            if message == '405':
                print 'Invalid Password, connection lost!'
                server.close()
                sys.exit()
            print message
        else:
            message = sys.stdin.readline()
            server.send(message)
            sys.stdout.write("<You>")
            sys.stdout.write("Message Sent: " + message)
            #sys.stdout.write(message)
            sys.stdout.flush()
server.close()