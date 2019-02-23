choice = raw_input("Enter command you wish to enter: ")
print(choice)

def qotd():
    from random import randint
    randomQOTD = randint(0, 9)

    if randomQOTD == 0:
        print("'A yurt a day keeps the doctor away.' - Gav")

    elif randomQOTD == 1:
        print("'Change the world by being a Yurt.' - Amy Poehler")

    elif randomQOTD == 2:
        print("'Every Yurt is a fresh beginning.' - T.S Eliot")

    elif randomQOTD == 3:
        print("'Never regret anything that made you Yurt.' - Mark Twain")

    elif randomQOTD == 4:
        print("'Everything you can Yurt is real.' - Pablo Picasso")

    elif randomQOTD == 5:
        print("'Whatever you do, Yurt it well.' - Walt Disney")

    elif randomQOTD == 6:
        print("'Tough times never last but Yurts people do.' - Robert H. Schiuller")

    elif randomQOTD == 7:
        print("'Have enough courage to Yurt and enough heart to Yurt Harder.' - Jessica N. S. Yourko")

    elif randomQOTD == 8:
        print("'Be so good they cant Yurt you' - Steve Martin")

    elif randomQOTD == 9:
        print("Never let your emotions over power your Yurt.' - Drake")

def ytsearch():
    print("Enter what you wish to search on YouTube: ")
    print("")
    print("--------- Use + instead of space ---------")
    print("------- example = how+to+use+space -------")
    youtubeSearch = raw_input ("Search: ")
    print(youtubeSearch)

    import webbrowser
    webbrowser.open('https://www.youtube.com/results?search_query='+youtubeSearch)

def fax():
    print("No Printer")

def tictactoe():
    #Import
    import os
    import time
    import random

    #Define the board
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    #Print the header
    def print_header():
	print"""
 ___  _  __     ___  __  __     ___  __  ___
/__ _\/ \/   _\   /_ _\/  _ \/   _\   /_ __\/  _ \/  __/    1 | 2 | 3
  / \  | ||  / ___ / \  | / \||  / ___ / \  | / \||  \      4 | 5 | 6
  | |  | ||  \_\____\| |  | |-|||  \_\____\| |  | \_/||  /_     7 | 8 | 9
  \_/  \_/\____/     \_/  \_/ \|\____/     \_/  \____/\____\

 To play Tic-Tac-Toe, you need to get three in a row...
 Your choices are defined, they must be from 1 to 9...

"""

    #Define the print_board function
    def print_board():
	    print "   |   |   "
	    print " "+board[1]+" | "+board[2]+" | "+board[3]+"  "
	    print "   |   |   "
	    print "---|---|---"
	    print "   |   |   "
	    print " "+board[4]+" | "+board[5]+" | "+board[6]+"  "
	    print "   |   |   "
	    print "---|---|---"
	    print "   |   |   "
	    print " "+board[7]+" | "+board[8]+" | "+board[9]+"  "
	    print "   |   |   "

    XorO = raw_input("Please choose wheteher you wish to be 'x' or 'o' ")
    print("----------- player 1 is '"+XorO+"'-----------")
    if XorO == "x":
        print("----------- player 2 is 'o'-----------")
    elif XorO == "X":
        print("----------- player 2 is 'o'-----------")
    elif XorO == "o":
        print("----------- player 2 is 'x'-----------")
    elif XorO == "O":
        print("----------- player 2 is 'x'-----------")

    while True:

        print_header()
        print_board()

        placement = raw_input("Please choose an empty space. ")
        placement = int(placement)

		#Check to see if the space is empty first
        if board[placement] == " ":
            board[placement] = XorO
        else:
            print "Sorry, that space is not empty!"
            time.sleep(1)

        if os.name == "nt":
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")


def flip():
    from random import randint
    randomflip = randint(0, 1)

    if randomflip == 0:
        print("HEADS")
    elif randomflip == 1:
        print("TAILS")

def rockpaperscissors():
    p1 = raw_input("Person 1 ready yes/no? ")
    p2 = raw_input("Person 2 ready yes/no? ")
    print(p1,p2)




def choiceC():
    def hello():
        print ("Timer Done")

    time = float(input("Enter time: "))

    t = Timer(time, hello)
    t.start()

def choiceD():
    print("D")

def unknown_choice():
    print("Unknown choice")

if choice == "!qotd":
    qotd()
elif choice == "!ytsearch":
    ytsearch()
elif choice == "fax":
    fax()
elif choice == "!ttt":
    tictactoe()
elif choice == "!flip":
    flip()
elif choice == "!rps":
    rockpaperscissors()
elif choice == "C":
    choiceC()
elif choice == "D":
    choiceD()
else:
    unknown_choice()
