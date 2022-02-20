import random
import os
board=[" " for x in range(10)]

def printBoard():
    print("     |     |     ")
    print("  " + board[1] + "  |  " + board[2] + "  |  " + board[3] + "  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  " + board[4] + "  |  " + board[5] + "  |  " + board[6] + "  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  " + board[7] + "  |  " + board[8] + "  |  " + board[9] + "  ")
    print("     |     |     ")

def insert(letter,pos):
    board[pos]=letter

def boardIsFull():
    if board.count(" ") > 1:
        return False
    else:
        return True

def freeSpace(pos):
    return board[pos]==" "

def isWinner(board,l):
    return ((board[1]==l and board[2]==l and board[3]==l) or
    (board[4]==l and board[5]==l and board[6]==l) or
    (board[7]==l and board[8]==l and board[9]==l) or
    (board[1]==l and board[4]==l and board[7]==l) or
    (board[2]==l and board[5]==l and board[8]==l) or
    (board[3]==l and board[6]==l and board[9]==l) or
    (board[1]==l and board[5]==l and board[9]==l) or
    (board[7]==l and board[5]==l and board[3]==l))

def playerMove():
    run=True
    while(run):
        pos=input("Please! select a position to enter 'X' in range(1,9)..")
        try:
            pos = int(pos)
            if pos in range(1,10):
                if freeSpace(pos):
                    insert('X',pos)
                    run=False
                else:
                    print("Sorry! this place is Occupied. Choose another..")
            else:
                print("Please! enter a number between (1-9)..")
        except:
            print("Please enter a valid number..")

def computerMove():
    emptySpaces=[x for x in range(1,10) if board[x]==' ']
    move=0
    for letter in ['O','X']:
        for i in emptySpaces:
            boardCopy=board[:]
            boardCopy[i]=letter
            if isWinner(boardCopy,letter):
                move=i
                return move

    if 5 in emptySpaces:
        move=5
        return move

    corners=[]
    for i in emptySpaces:
        if i in [1,3,7,9]:
            corners.append(i)
    if len(corners)>0:
        move=random.choice(corners)
        return move
    
    edges=[]
    for i in emptySpaces:
        if i in [2,4,6,8]:
            edges.append(i)
    if len(edges)>0:
        move=random.choice(edges)
        return move
    return move

def play():
    print("Welcome to the game : TIC-TAC-TOE")
    printBoard()
    while not(boardIsFull()):
        if not(isWinner(board,'O')):
            playerMove()
            os.system('cls')
            printBoard()
        else:
            print("Oops! you loose..")
            break

        if not(isWinner(board,'X')):
            move=computerMove()
            if move !=0:
                insert('O',move)
                print("Computer placed 'O' at position %s." %move)
                printBoard()
        else:
            print("Hurrey! you win!")
            break
    if boardIsFull():
        print("Tie game! well played..")

while True:
    x= input("Do you wanna play the game? (y/n) ")
    if x.lower()=='y':
        board=[" " for x in range(10)]
        print("-----------------------------------")
        play()
    else:
        break