# Python modules
import socket
import threading, Queue
from time import gmtime, strftime
import time
from time import gmtime, strftime
import time
import datetime

# IP address goes here
HOST = '127.0.0.1'
PORT = 3500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

# A list of all current connections
currentConnections = list()
# Log of the chat
buffer = "Beginning of chat | "
# Number of messages in buffer
bufferCounter = 0
# List of usernames
usernames = "Users in this chat: "
#Key value pair of users and their connection object
userConnectionsDict = dict()
#Kicked users
kickedUsers = list()

# The functions we've added
def qotd():
    from random import randint
    randomQOTD = randint(0, 9)
    quotes = ["'A yurt a day keeps the doctor away.' - Gav", "'Change the world by being a Yurt.' - Amy Poehler", "'Every Yurt is a fresh beginning.' - T.S Eliot",
    "'Never regret anything that made you Yurt.' - Mark Twain", "'Everything you can Yurt is real.' - Pablo Picasso", "'Whatever you do, Yurt it well.' - Walt Disney",
    "'Tough times never last but Yurts people do.' - Robert H. Schiuller", "'Have enough courage to Yurt and enough heart to Yurt Harder.' - Jessica N. S. Yourko",
    "'Be so good they cant Yurt you' - Steve Martin", "'Never let your emotions over power your Yurt.' - Drake"]
    for singleClient in currentConnections:
        singleClient.send(str(quotes[randomQOTD]))

def addToBuffer(data):
    global buffer
    global bufferCounter
    bufferCounter += 1
    buffer = buffer + data + " | "

def total():
    global bufferCounter
    for singleClient in currentConnections:
        singleClient.send(str(bufferCounter))

def day():
    day = ""
    day ="Today is "+ datetime.date.today().strftime("%A")
    for singleClient in currentConnections:
        singleClient.send(str(day))

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

def checkData(data, conn):
    global kickedUsers
    if "!setUsername" in data:
        return False
    if "!ping" in data:
        return False
    if conn in kickedUsers:
        return False
    return True

def addUsername(data, con):
    global usernames
    global userConnectionsDict
    userData = data.replace("!setUsername","")
    usernames = usernames + userData + " "
    userConnectionsDict[userData] = con
    con.send(str(buffer + "\n"))
    if "!ping" not in userData:
        for singleClient in currentConnections:
            singleClient.send(str(userData + " has joined the chat!"))

def getUsers():
    global usernames
    for singleClient in currentConnections:
        singleClient.send(str(usernames))

def sendTime():
    for singleClient in currentConnections:
        singleClient.send(strftime("%H:%M:%S", gmtime()))

def kick(data):
    global kickedUsers
    global userConnectionsDict
    user = data.split(':', 1)[-1]
    user = user.replace("!kick","")
    user = user.strip()
    for singleClient in currentConnections:
        singleClient.send(str(user + " has been kicked from the chat! They well no longer be able to send or recieve messages!"))
    object = userConnectionsDict[user]
    currentConnections.remove(object)
    kickedUsers.append(object)

def ping(con):
    global currentConnections
    con.send(str("pong"))
    currentConnections.remove(conn)

def date():
    date= ""
    date ="Todays date is "+ datetime.date.today().strftime("%d-%m-%Y")
    for singleClient in currentConnections:
        singleClient.send(str(date))

# Parse messages to see if functions are called
def parseInput(data, con):
    # Check if functions are called
    if "!flip" in data:
        flip()
    if "!setUsername" in data:
        addUsername(data, con)
    if "!users" in data:
        getUsers()
    if "!time" in data:
        sendTime()
    if "!ping" in data:
        ping(con)
    if "!kick" in data:
        kick(data)
    if "!qotd" in data:
        qotd()
    if "!total"in data:
        total()
    if "!day" in data:
        day()
    if "!date" in data:
        date()

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
        if "!" not in data:
            addToBuffer(data)
        for singleClient in currentConnections:
            if singleClient != conn :
                if checkData(data, conn):
                    singleClient.send(str(data))
        parseInput(data,conn)# Calling the parser

while 1:
    s.listen(1)
    conn, addr = s.accept()
    # Creates a thread for each connection
    t = threading.Thread(target=manageConnection, args = (conn,addr))
    t.start()
