import threading
import socket
import os
import webbrowser

HOST = '172.20.10.3'
PORT = 20070   

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

username = None

# Open youtube search
def google(data):
    print("Google function")
    googleStr = data.replace("!google","")
    googleStr = googleStr.split(':', 1)[-1] = googleStr.strip()
    googleStr = googleStr.replace(" ","+")
    url = "https://www.google.com/search?q=" + googleStr
    webbrowser.open_new_tab(url)

# Open youtube search
def ping():
    pingSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    pingSock.connect((HOST, PORT))
	
def commandlist():
    commandlist = 	("**************************************************************\n"
    "***                      Commands                          ***\n"
    "**************************************************************\n"
    "***              !time - displays current time             ***\n"
    "***     !total - displays total messages in buffer         ***\n"
    "***             !users - displays current users            ***\n"
    "***                  !flip - flips a coin                  ***\n"
    "***             !qotd - print quote of the day             ***\n"
    "***    !google - opens browser on other users machines     ***\n"
    "***            !day - displays current day of week         ***\n"
    "***              !date - displays current date             ***\n"
    "***         !ping - prints pong and latency time           ***\n"
    "***        !commands - displays current commands           ***\n"
    "**************************************************************")
	
    print(commandlist)


def parse(data):
    # Check if functions are called
    if "!flip" in data:
        flip()
    if "!google" in data:
        google(data)
    if "!ping" in data:
        ping()
    if "!commands" in data:
        commandlist()



def readInputThreaded(so):
    global username
    print("Type your username:")
    username = raw_input()
    so.sendall(str("!setUsername" + username))

    while 1:
        text = raw_input()
        text = username + ": " + text
        if "!commands" in text:
            commandlist()
        else:
            so.sendall(str(text))

t = threading.Thread(target=readInputThreaded, args = (s,))
t.start()

def readFromServer(s):
    global username
    while 1:
        data = s.recv(100)
        if username != None:
            print(data)
        parse(data)

# Start listening
t = threading.Thread(target=readFromServer, args = (s,))
t.start()
