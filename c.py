import threading
import socket
import os
import webbrowser

HOST = '192.168.0.79'    # The remote host
PORT = 20010          # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Open youtube search
def google(data):
    print "Google function"
    googleStr = data.replace("!google","")
    googleStr = googleStr.split(':', 1)[-1]
    googleStr = googleStr.strip()
    googleStr = googleStr.replace(" ","+")
    url = "https://www.google.com/search?q=" + googleStr
    webbrowser.open_new_tab(url)

def parse(data):
    print str(data)
    # Check if functions are called
    if "!flip" in data:
      flip()
    if "!google" in data:
      google(data)

# when we send data to the server, we are using a colon
# at the end of a sentence to mark the end of the current sentence
# later when the input comes back, we will then be breaking the input
# into individual parts using the colon : to separate the lines
def readInputThreaded(so):
    print("Type your username:")
    username = raw_input()
    #if os.name == "nt":
    #    print("you run windows")
    #elif os.name == "posix":
    #    print("you run linux")

    while 1:
        text = raw_input()
        text = username + ": " + text
        so.sendall(str(text))

t = threading.Thread(target=readInputThreaded, args = (s,))
t.start()

def readFromServer(s):
    while 1:
        data = s.recv(100)
        print str(data)
        parse(data)

# Start listening
t = threading.Thread(target=readFromServer, args = (s,))
t.start()
