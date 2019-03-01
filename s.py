# Python modules
import socket
import threading, Queue
from time import gmtime, strftime
import time

# IP address goes here
HOST = '172.20.10.5'
PORT = 20010
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

# A list of all current connections
currentConnections = list()
# Log of the chat
buffer = "Beginning of chat : "

# The functions we've added
# Coin flip
def flip():
    from random import randint
    randomflip = randint(0, 1)

    if randomflip == 0:
        flip = "heads"
    elif randomflip == 1:
        flip = "tails"

    for singleClient in currentConnections:
        singleClient.send(str(flip))

# Parse messages to see if functions are called
def parseInput(data, con):
    print str(data)
    # Check if functions are called
    if "!flip" in data:
        flip()

#manages each connection
def manageConnection(conn, addr):
    global buffer
    global currentConnections
    print 'Connected by', addr
    # add the new connection to the list of connections
    currentConnections.append(conn)
    # Continue to listen
    while 1:
        data = conn.recv(1024)
        print "rec:" + str(data)
        for singleClient in currentConnections:
            if singleClient != conn:
                singleClient.send(str(data))
        parseInput(data,conn)# Calling the parser

while 1:
    s.listen(1)
    conn, addr = s.accept()
    # Creates a thread for each connection
    t = threading.Thread(target=manageConnection, args = (conn,addr))
    t.start()
