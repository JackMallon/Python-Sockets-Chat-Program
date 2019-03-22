import threading
import socket
import os
import webbrowser
import time

HOST = '127.0.0.1'
PORT = 3500
username = None

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def commandlist():
    commandlist = 	(
    "**************************************************************\n"
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
    print commandlist

# Open youtube search
def google(data):
    print("Google function")
    googleStr = data.replace("!google","")
    googleStr = googleStr.split(':', 1)[-1]
    googleStr = googleStr.strip()
    googleStr = googleStr.replace(" ","+")
    print(googleStr)
    url = "https://www.google.com/search?q=" + googleStr
    webbrowser.open_new_tab(url)

# Ping pong
def ping():
    global HOST, PORT
    pingSoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    pingSoc.connect((HOST, PORT))
    start = time.time()
    pingSoc.sendall(str("!ping"))
    data = pingSoc.recv(100)
    print(data)
    end = time.time()
    amount = (end - start)
    print("Ping took " + str(amount) + " seconds")
    pingSoc.shutdown(socket.SHUT_RDWR)
    pingSoc.close()

def processOutput(text):
    if "!ping" in text:
        ping()
        return False
    if "!commands" in text:
        commandlist()
        return False
    return True

def parse(data):
    # Check if functions are called
    if "!google" in data:
        google(data)

def readInputThreaded(so):
    global username
    print("Type your username:")
    username = raw_input()
    so.sendall(str("!setUsername" + username))
    while 1:
        text = raw_input()
        text = username + ": " + text
        if processOutput(text):
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
