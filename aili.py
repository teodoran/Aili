currentPiece = 'O'
board = ['_' for i in range(9)]
done = 0

def aiMove(player, board):
    maxMove = -1
    maximum = -2

    children = getAllLegalMoves(board)

    for move in children:
        temp = minimax(-1*player, expandChild(board, move, player))
        if temp > maximum:
            maximum = temp
            maxMove = move
    return maxMove

def minimax(player, board):
    if hasWon(board):
        return player*-1
    if isFull(board):
        return 0

    children = getAllLegalMoves(board)

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

def getAllLegalMoves(board):
    moves = []
    for i in range(9):
        if isVacant(board, i):
            moves.append(i)
    return moves
        
def expandChild(board, move, player):
    piece = 'X'
    newBoard = board[:]

    if player == -1:
        piece = 'O'

    newBoard[move] = piece
    return newBoard

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

def isVacant(board, i):
    if board[i] != '_':
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

def userPlacePiece(board, currentPiece):
    userInput = raw_input("{0}'s turn: ".format(currentPiece))
    x = int(userInput.split(' ')[0])%3
    y = int(userInput.split(' ')[1])%3
    
    if isVacant(board, xyi(x, y)):
        board[xyi(x, y)] = currentPiece
        printBoard(board)
        swapCurrentPiece()
    else:
        print "Place is not vacant."

def aiPlacePiece(board):
    move = aiMove(1, board)
    board[move] = currentPiece
    printBoard(board)
    swapCurrentPiece()
    

def checkGameEnded():
    if hasWon(board):
        done = 1
        swapCurrentPiece()
        print "Player {0} has won!".format(currentPiece)
    if isFull(board):
        done = 1
        print "Game ended with a tie."

def printBoard(board):
    print "   0 1 2 "
    print "   _____ "
    print "0 |{0} {1} {2}|".format(board[0], board[1], board[2])
    print "1 |{0} {1} {2}|".format(board[3], board[4], board[5])
    print "2 |{0} {1} {2}|".format(board[6], board[7], board[8])

printBoard(board)

while not done:
    userPlacePiece(board, currentPiece)
    checkGameEnded()
    aiPlacePiece(board)
    checkGameEnded()
    
 
    
