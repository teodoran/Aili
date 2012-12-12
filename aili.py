currentPiece = 'X'
board = ['_' for i in range(9)]
done = 0

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

def isVacant(board, x, y):
    if board[xyi(x, y)] != '_':
        return 0
    return 1

def swapCurrentPiece():
    global currentPiece
    if currentPiece == 'X':
        currentPiece = 'O'
    else:
        currentPiece = 'X'

def xyi(x, y):
    return y*3 + x

def placePiece(board, piece, x, y):
    board[xyi(x, y)] = piece

def userPlacePiece(board, currentPiece):
    userInput = raw_input("{0}'s turn: ".format(currentPiece))
    x = int(userInput.split(' ')[0])%3
    y = int(userInput.split(' ')[1])%3
    
    if isVacant(board, x, y):
        placePiece(board, currentPiece, x, y)
        printBoard(board)
        swapCurrentPiece()
    else:
        print "Place is not vacant."

def printBoard(board):
    print "   0 1 2 "
    print "   _____ "
    print "0 |{0} {1} {2}|".format(board[0], board[1], board[2])
    print "1 |{0} {1} {2}|".format(board[3], board[4], board[5])
    print "2 |{0} {1} {2}|".format(board[6], board[7], board[8])

printBoard(board)

while not done:
    userPlacePiece(board, currentPiece)
    if hasWon(board):
        done = 1
        swapCurrentPiece()
        print "Player {0} has won!".format(currentPiece)
    
