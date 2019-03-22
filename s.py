# Python modules
import socket
import threading, Queue
from time import gmtime, strftime
import time
from time import gmtime, strftime

# IP address goes here
HOST = '127.0.0.1'
PORT = 20038
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

# A list of all current connections
currentConnections = list()
# Log of the chat
buffer = "Beginning of chat : "
# List of usernames
usernames = "Users in this chat: "

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

def checkData(data):
    if "!setUsername" in data:
        return False
    return True

def addUsername(data):
    global usernames
    userData = data.replace("!setUsername","")
    usernames = usernames + userData + " "
    for singleClient in currentConnections:
        singleClient.send(str(userData + " has joined the chat!"))

def getUsers():
    global usernames
    for singleClient in currentConnections:
        singleClient.send(str(usernames))

def sendTime():
    for singleClient in currentConnections:
        singleClient.send(strftime("%H:%M:%S", gmtime()))

# Parse messages to see if functions are called
def parseInput(data, con):
    print str(data)
    # Check if functions are called
    if "!flip" in data:
        flip()
    if "!setUsername" in data:
        addUsername(data)
    if "!users" in data:
        getUsers()
    if "!time" in data:
        sendTime()

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
        for singleClient in currentConnections:
            if singleClient != conn:
                if checkData(data):
                    singleClient.send(str(data))
        parseInput(data,conn)# Calling the parser

while 1:
    s.listen(1)
    conn, addr = s.accept()
    # Creates a thread for each connection
    t = threading.Thread(target=manageConnection, args = (conn,addr))
    t.start()
