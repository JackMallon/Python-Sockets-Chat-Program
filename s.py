# Python modules
import socket
import threading, Queue
from time import gmtime, strftime
import time
from time import gmtime, strftime
import datetime

# IP address goes here
HOST = '172.20.10.3'    
PORT = 20070

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

# A list of all current connections
currentConnections = list()
# Log of the chat
bufferCounter = 0
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
		
def rpsls():
    from random import randint
    randomrpsls = randint(0, 4)
    rpsls = ""

    if randomrpsls == 0:
        rpsls = "rock"
    elif randomrpsls == 1:
        rpsls = "paper"
    elif randomrpsls == 2:
        rpsls = "scissors"
    elif randomrpsls == 3:
        rpsls = "lizard"
    elif randomrpsls == 4:
        rpsls = "spock"
				
    for singleClient in currentConnections:
        singleClient.send(str(rpsls, quote))
		
def qotd():
    from random import randint
    randomQOTD = randint(0, 9)
    qotd = ""

    if randomQOTD == 0:
        qotd=("'A yurt a day keeps the doctor away.' - Gav")

    elif randomQOTD == 1:
        qotd=("'Change the world by being a Yurt.' - Amy Poehler")

    elif randomQOTD == 2:
        qotd=("'Every Yurt is a fresh beginning.' - T.S Eliot")

    elif randomQOTD == 3:
        qotd=("'Never regret anything that made you Yurt.' - Mark Twain")

    elif randomQOTD == 4:
        qotd=("'Everything you can Yurt is real.' - Pablo Picasso")

    elif randomQOTD == 5:
        qotd=("'Whatever you do, Yurt it well.' - Walt Disney")

    elif randomQOTD == 6:
        qotd=("'Tough times never last but Yurts people do.' - Robert H. Schiuller")

    elif randomQOTD == 7:
        qotd=("'Have enough courage to Yurt and enough heart to Yurt Harder.' - Jessica N. S. Yourko")

    elif randomQOTD == 8:
        qotd=("'Be so good they cant Yurt you' - Steve Martin")

    elif randomQOTD == 9:
        qotd=("'Never let your emotions over power your Yurt.' - Drake")
		
    for singleClient in currentConnections:
        singleClient.send(str(qotd))
		
def date():
    date= ""
    date ="Todays date is "+ datetime.date.today().strftime("%d-%m-%Y")

    for singleClient in currentConnections:
        singleClient.send(str(date))
		
def day():
    day = ""
    day ="Today is "+ datetime.date.today().strftime("%A")
	
    for singleClient in currentConnections:
        singleClient.send(str(day))
		
		
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

def addToBuffer(data):
    global buffer
    global bufferCounter
    buffer = buffer + data + " : "
    bufferCounter += 1
    print(bufferCounter)
	
def total():
    for singleClient in currentConnections:
        singleClient.send(str(bufferCounter))
		
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
    if "!total"in data:
        total()
    if "!qotd" in data:
        qotd()
    if "!rpsls" in data:
        rpsls()
    if "!date" in data:
        date()
    if "!day" in data:
        day()



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
        addToBuffer(data)
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
