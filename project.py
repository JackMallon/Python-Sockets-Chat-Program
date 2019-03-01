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
    board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    #Print the header
    def print_header():
	print"""
 _____  _  ____     _____  ____  ____     _____  ____  _____
/__ __\/ \/   _\   /__ __\/  _ \/   _\   /__ __\/  _ \/  __/    1 | 2 | 3
  / \  | ||  / _____ / \  | / \||  / _____ / \  | / \||  \      4 | 5 | 6
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
	
    def is_winner(board, player):
        if (board[1] == player and board[2] == player and board[3] == player) or \
            (board[4] == player and board[5] == player and board[6] == player) or \
            (board[7] == player and board[8] == player and board[9] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[3] == player and board[6] == player and board[9] == player) or \
            (board[1] == player and board[5] == player and board[9] == player) or \
            (board[3] == player and board[5] == player and board[7] == player):
            return True
        else:
            return False
		
    def is_board_full(board):
        if " " in board:
            return False
        else:
            return True
	
    while True:
        os.system("cls")
        print_header()
        print_board()
	
        #Get Player X Input
        choice = raw_input("Please choose an empty space for X. ")
        choice = int(choice)
	
        #Check to see if the space is empty first
        if board[choice] == " ":
            board[choice] = "X"
        else:
            print "Sorry, that space is not empty!"
        time.sleep(1)
		
        #Check for X win
        if is_winner(board, "X"):
            os.system("cls")
            print_header()
            print_board()
            print "X wins! Congratulations"
            break
		
        os.system("cls")
        print_header()
        print_board()
	
        #Check for a tie (is the board full)
        #If the board is full, do something
        if is_board_full(board):
            print "Tie!"
            break
	
        #Get Player O Input
        choice = raw_input("Please choose an empty space for O. ")
        choice = int(choice)
	
        #Check to see if the space is empty first
        if board[choice] == " ":
            board[choice] = "O"
        else:
            print "Sorry, that space is not empty!"
            time.sleep(1)
		
        #Check for O win
        if is_winner(board, "O"):
            os.system("cls")
            print_header()
            print_board()
            print "O wins! Congratulations"
            break
		
        #Check for a tie (is the board full)
        #If the board is full, do something
        if is_board_full(board):
            print "Tie!"
            break
		


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
    if (p1 == "yes" and p2 == "yes"):
            from random import randint
            randomrpsP1 = randint(0, 2)
            randomrpsP2 = randint(0, 2)
	
            if randomrpsP1 == 0:
                print("Player1:ROCK")
            elif randomrpsP1 == 1:
                print("Player1:PAPER")            
            elif randomrpsP1 == 2:
                print("Player1:SCISSORS")            
            if randomrpsP2 == 0:
                print("Player2:ROCK")
            elif randomrpsP2 == 1:
                print("Player2:PAPER")            
            elif randomrpsP2 == 2:
                print("Player2:SCISSORS")
				
			#player1win
            if (randomrpsP1 == 1 and randomrpsP2 == 0) or \
                (randomrpsP1 == 0 and randomrpsP2 == 2) or \
                (randomrpsP1 == 2 and randomrpsP2 == 1):
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~      Player 1 Wins!!!       ~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

			#player2win
            if (randomrpsP2 == 1 and randomrpsP1 == 0) or \
                (randomrpsP2 == 0 and randomrpsP1 == 2) or \
                (randomrpsP2 == 2 and randomrpsP1 == 1):
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~      Player 2 Wins!!!       ~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
				
			#draw
            if (randomrpsP1 == 0 and randomrpsP2 == 0) or \
                (randomrpsP1 == 1 and randomrpsP2 == 1) or \
                (randomrpsP1 == 2 and randomrpsP2 == 2):
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print("~            Tie!!!           ~")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    else:
        print("Players arent ready, Enter command again to try again!")
	
	
	
    
def commands():
    print("*********************************************************************")
    print("***                          Command List                         ***")
    print("*********************************************************************")
    print("***                                                               ***")
    print("***                  !qotd - gives quote of the day               ***")
    print("***                   !ytsearch - searchss youtube                ***")
    print("***                  fax - auto responds with reply               ***")
    print("***     !ttt - play x's and o's against another chat member       ***")
    print("***                      !flip - flips a coin                     ***")
    print("***  !rps - playrock paper scissors against another chat member   ***")
    print("***                 !commands - gives command list                ***")
    print("***                     !blah - blah blah blah                    ***")
    print("***                     !blah - blah blah blah                    ***")
    print("***                     !blah - blah blah blah                    ***")
    print("***                                                               ***")
    print("*********************************************************************")


	
def choiceD():
    print("D")
	
def choiceE():
    print("E")


def unknown_choice():
    print("Unknown choice")

if choice == "!qotd": #works
    qotd()
elif choice == "!ytsearch": #works
    ytsearch()
elif choice == "fax": #works
    fax()
elif choice == "!ttt": #works
    tictactoe()
elif choice == "!flip": #works
    flip()
elif choice == "!rps": #works
    rockpaperscissors()
elif choice == "!commands": #works
    commands()
elif choice == "D":
    choiceD()
elif choice == "E":
    choiceE()
else:
    unknown_choice()
