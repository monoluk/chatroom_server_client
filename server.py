import socket
import select
from thread import *
import sys
import demo_mysql

# filename = "users.txt"
# file1 = open(filename, 'rb')
# allowedUsers = pickle.load(file1)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""
the first argument AF_INET is the address domain of the socket. This is used when we have an Internet Domain
with any two hosts
The second argument is the type of socket. SOCK_STREAM means that data or characters are read in a continuous flow
"""
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
if len(sys.argv) != 3:
    print "Correct usage: script, Server IP address, port number"
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.bind((IP_address, Port)) 
#binds the server to an entered IP address and at the specified port number. The client must be aware of these parameters
server.listen(100)
#listens for 100 active connections. This number can be increased as per convenience
print 'Listening for connections on ' + IP_address + ' on port: ' + str(Port)
list_of_clients=[]
#allowedUsers = {'ye':'1234','ke': '1234','justin':'1234','hayley':'1234'}


def clientthread(client, addr,clientUserID):
    #clientUserID = client.recv(10)
    client.send("Welcome to the COOL chatroom! " + clientUserID)
    #sends a message to the client whose user object is client
    while True:
            try:     
                message = client.recv(2048)    
                if message:
                    message_to_send = "<" + clientUserID + "> " + message
                    print message_to_send
                    broadcast(message_to_send,client)
                    #prints the message and address of the user who just sent the message on the server terminal
                else:
                    userLeft = clientUserID + ' left the chatroom'
                    print userLeft
                    # broadcast(userLeft,client)
                    remove(client)
            except:
                continue

def broadcast(message,connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
                clients.send(message)
            except:
                clients.close()
                remove(clients)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while True:
    client, addr = server.accept()
    clientUserInfo = client.recv(15)

    # filename = "users.txt"
    # file1 = open(filename, 'rb')
    # allowedUsers = pickle.load(file1)

    clientUserID, clientPwd = clientUserInfo.split()
    validUser = demo_mysql.verification(clientUserID,clientPwd)

    # if clientUserID not in allowedUsers:
    if not validUser:
        client.send('404')
        validUser = False
        print 'Unauthorised user: ' + clientUserID + ', tried to login'
        try:
            client.close()
        except Exception as e:
            continue
    
    # if clientPwd != allowedUsers[clientUserID]:
    #     client.send('405')
    #     validUser = False
    #     print 'Unauthorised user: ' + clientUserID + ', tried to login'
    #     client.close()

    # for userID in allowedUsers
    # #if clientPwd != allowedUsers[clientUserID]:
    # print userID[clientUserID]

    """
    Accepts a connection request and stores two parameters, conn which is a socket object for that user, and addr which contains
    the IP address of the client that just connected
    """
    if validUser:
        list_of_clients.append(client)
        #print addr[0] + " connected"
        connectionMessage = clientUserID + " is connected"
        print connectionMessage
        broadcast(connectionMessage,client)
        
        #maintains a list of clients for ease of broadcasting a message to all available people in the chatroom
        #Prints the address of the person who just connected
        start_new_thread(clientthread,(client,addr,clientUserID))
        #creates and individual thread for every user that connects

client.close()
server.close()
file1.close()