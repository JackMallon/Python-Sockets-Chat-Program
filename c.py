import threading
import socket
import os
import webbrowser

HOST = '127.0.0.1'    # The remote host
PORT = 20040          # The same port as used by the server

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


def parse(data):
    # Check if functions are called
    if "!flip" in data:
        flip()
    if "!google" in data:
        google(data)
    if "!ping" in data:
        ping()


def readInputThreaded(so):
    global username
    print("Type your username:")
    username = raw_input()
    so.sendall(str("!setUsername" + username))

    while 1:
        text = raw_input()
        text = username + ": " + text
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
