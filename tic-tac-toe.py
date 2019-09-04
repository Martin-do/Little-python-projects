import sys, random

''' my tic-tac-toe game of two players'''

def printBoard(b):
    print(board[7] + "|" + board[8] + "|" + board[9]) 
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[1] + "|" + board[2] + "|" + board[3])
secondPlayerLetter = " "
board = ["occu", " ", " ", " ", " ", " ", " ", " ", " ", " "]
name1 = input("Enter name of first player: ").title()
name2 = input("Enter name of second player: ").title()
firstPlayerLetter = input(name1 + " should pick either 'X' or 'O': ").upper()
if  firstPlayerLetter == "X":
    secondPlayerLetter = "O"
else:
    secondPlayerLetter = "X"
print("Okay " + name1 + ", you are " + firstPlayerLetter) 
print(name2 + ", you are " + secondPlayerLetter)

def checkMate(player, userName):
    if player == board[7] and player == board[8] and player == board[9]:
        print(userName + ", YOU WIN!!!")
        printBoard(board)
        sys.exit()
    elif player == board[4] and player == board[5] and player == board[6]:
        print(userName + ", YOU WIN!!!")
        printBoard(board)
        sys.exit()
    elif player == board[1] and player == board[2] and player == board[3]:
        print(userName + ", YOU WIN!!!")
        printBoard(board)
        sys.exit()
    elif player == board[1] and player == board[4] and player == board[7]:
        print(userName + ", YOU WIN!!!")
        printBoard(board)
        sys.exit()
    elif player == board[2] and player == board[5] and player == board[8]:
        print(userName + ", YOU WIN!!!")
        printBoard(board)
        sys.exit()
    elif player == board[3] and player == board[6] and player == board[9]:
        print(userName + ", YOU WIN!!!")
        printBoard(board)
        sys.exit()
    elif player == board[3] and player == board[5] and player == board[7]:
        print(userName + ", YOU WIN!!!")
        printBoard(board)
        sys.exit()
    elif player == board[1] and player == board[5] and player == board[9]:
        print(userName + ", YOU WIN!!!")
        printBoard(board)
        sys.exit()
    else:
        print("==================")


def playerMove(width):
    print((" Make your move " + name1 + " ").center(width, '='))
    move = int(input("Pick between numbers 1 - 9 to play: "))
    board[move] = str(firstPlayerLetter)
    printBoard(board)
    checkMate(firstPlayerLetter, name1)

def Player2Move(width):
    print((" Make your move " + name2 + " ").center(width, '='))
    Cmove = int(input("Pick between numbers 1 - 9 to play: "))
    board[Cmove] = str(secondPlayerLetter)
    printBoard(board)
    checkMate(secondPlayerLetter, name2)

printBoard(board)
for i in range(4):
    playerMove(30)
    Player2Move(30)
playerMove(30)
print("This is a tie")
sys.exit()