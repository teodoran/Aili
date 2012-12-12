##########################################################
# Global variables and functions directly related to them.

currentPlayer = 'X'
board = ['_' for i in range(9)]
done = 0

def i(x, y):
    return y*3 + x

def printBoard(board):
    print ""
    print "   0 1 2 "
    print "   _____ "
    for i in range(3):
        print "{0} |{1} {2} {3}|".format(i, board[i*3], board[i*3+1], board[i*3+2])
    print ""

def swapCurrentPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
    else:
        currentPlayer = 'X'


#######################################################
# Ai related functions. Includes Minimax implementation

def minimax(player, board):
    if hasWon(board):
        return player*-1
    if isFull(board):
        return 0

    children = allLegalMoves(board)

    if player == 1:
        maximum = -2
        for move in children:
            temp = minimax(-1*player, expandChild(board, move, player))
            if temp > maximum:
                maximum = temp
        return maximum

    else:
        minimum = 2
        for move in children:
            temp = minimax(-1*player, expandChild(board, move, player))
            if temp < minimum:
                minimum = temp
        return minimum

def allLegalMoves(board):
    moves = []
    for i in range(9):
        if isVacant(board, i):
            moves.append(i)
    return moves

def isVacant(board, i):
    if board[i] != '_':
        return 0
    return 1
        
def expandChild(board, move, player):
    piece = 'O'
    newBoard = board[:]

    if player == -1:
        piece = 'X'

    newBoard[move] = piece
    return newBoard


########################################
# Functions to determine if game is over

def checkGameEnded(player, board):
    global done
    if hasWon(board):
        done = 1
        if player == 'O':
            print "Aili has won!"
        else:
            print "You hvae won!"
    if isFull(board):
        done = 1
        print "Game ended with a tie."

def isFull(board):
    n = 0
    
    for i in range(9):
        n += not isVacant(board, i)

    return n >= 9

def hasWon(board):
    returnVal = 0
    returnVal += threeInRow(board, 0, 4, 8)
    returnVal += threeInRow(board, 2, 4, 6)

    for i in range(3):
        n = i*3
        returnVal += threeInRow(board, n, n+1, n+2)
        returnVal +=  threeInRow(board, i, i+3, i+6)
    return returnVal

def threeInRow(board, i, j, k):
    if board[i] != '_' and board[j] != '_' and board[k] != '_' and board[i] == board[j] and board[i] == board[k]:
        return 1
    return 0


#############################################
# Piece placement functions for player and Ai

def aiMove(board):
    print "Aili makes her move."
    maxMove = -1
    maximum = -2
    children = allLegalMoves(board)

    for move in children:
        temp = minimax(-1, expandChild(board, move, 1))
        if temp > maximum:
            maximum = temp
            maxMove = move
    return maxMove

def userMove(board):
    while 1:
        userInput = raw_input("{0}'s turn: ".format('X'))
        x = int(userInput.split(' ')[0])%3
        y = int(userInput.split(' ')[1])%3
    
        if i(x, y) in allLegalMoves(board):
            return i(x, y)
        else:
            print "Place is not vacant."

def placePiece(player, board):
    move = 0
    if player == 'O':
        move = aiMove(board)
    else:
        move = userMove(board)
    board[move] = player
    printBoard(board)


##################################
# Game loop and intro print-screen

print " __________________________"
print "|                          |"
print "|       /\  |  |   |       |"
print "|      /  \ |  |__ |       |"
print "|                          |"
print "|The tic tac toe playing AI|"

printBoard(board)

while not done:
    placePiece(currentPlayer, board)
    checkGameEnded(currentPlayer, board)
    swapCurrentPlayer()
    
 
    
