import copy
import time


class Board:
    def __init__(self, board, pegCount):
        self.board = board
        self.pegCount = pegCount
        self.visited = False
        self.children = []
        self.parent = None
        self.path = []


#East Hop Functions
def validateNorthEastHop(board, hopperIndex):
    #checks if valid hopperIndex (hopper to hop exists at said lcoation)
    if board[hopperIndex[0]][hopperIndex[1]] != 1:
        return False
    #if hopper won't jump to invalid area of the board from a NorthEast Hop (right side), then continue (has a place to land)
    if hopperIndex[1] <= len(board[hopperIndex[0]]) - 3:
        #if there is indeed a peg to hop and no peg in the way of the landing, output true
        if board[hopperIndex[0] - 1][hopperIndex[1]] == 1 and board[hopperIndex[0] - 2][hopperIndex[1]] == 0:
            return True
        else:
            return False
    else:
        return False
def hopNorthEast(board, hopperIndex, pathPiece):
    board[hopperIndex[0]][hopperIndex[1]] = 0
    board[hopperIndex[0] - 1][hopperIndex[1]] = 0
    board[hopperIndex[0] - 2][hopperIndex[1]] = 1
    landedIndex = [hopperIndex[0] - 2, hopperIndex[1]]
    pathPiece.append(convertIndex(landedIndex))
def validateEastHop(board, hopperIndex):
    #checks if valid hopperIndex (hopper to hop exists at said lcoation)
    if board[hopperIndex[0]][hopperIndex[1]] != 1:
        return False
    #if hopper won't jump to invalid area of the board from an East Hop (right side), then continue (has a place to land)
    if hopperIndex[1] <= len(board[hopperIndex[0]]) - 3:
        #if there is indeed a peg to hop and no peg in the way of the landing, output true
        if board[hopperIndex[0]][hopperIndex[1] + 1] == 1 and board[hopperIndex[0]][hopperIndex[1] + 2] == 0:
            return True
        else:
            return False
    else:
        return False
def hopEast(board, hopperIndex, pathPiece):
    board[hopperIndex[0]][hopperIndex[1]] = 0
    board[hopperIndex[0]][hopperIndex[1] + 1] = 0
    board[hopperIndex[0]][hopperIndex[1] + 2] = 1
    landedIndex = [hopperIndex[0], hopperIndex[1] + 2]
    pathPiece.append(convertIndex(landedIndex))
def validateSouthEastHop(board, hopperIndex):
    #checks if valid hopperIndex (hopper to hop exists at said lcoation)
    if board[hopperIndex[0]][hopperIndex[1]] != 1:
        return False
    #if hopper won't jump to invalid area of the board from a SouthEast Hop (bottom side), then continue (has a place to land)
    if hopperIndex[0] <= 2:
        #if there is indeed a peg to hop and no peg in the way of the landing, output true
        if board[hopperIndex[0] + 1][hopperIndex[1] + 1] == 1 and board[hopperIndex[0] + 2][hopperIndex[1] + 2] == 0:
            return True
        else:
            return False
    else:
        return False
def hopSouthEast(board, hopperIndex, pathPiece):
    board[hopperIndex[0]][hopperIndex[1]] = 0
    board[hopperIndex[0] + 1][hopperIndex[1] + 1] = 0
    board[hopperIndex[0] + 2][hopperIndex[1] + 2] = 1
    landedIndex = [hopperIndex[0] + 2, hopperIndex[1] + 2]
    pathPiece.append(convertIndex(landedIndex))

#West Hop Functions
def validateNorthWestHop(board, hopperIndex):
    #checks if valid hopperIndex (hopper to hop exists at said lcoation)
    if board[hopperIndex[0]][hopperIndex[1]] != 1:
        return False
    #if hopper won't jump to invalid area of the board from a NorthWest Hop (left side), then continue (has a place to land)
    if hopperIndex[1] >= 2:
        #if there is indeed a peg to hop and no peg in the way of the landing, output true
        if board[hopperIndex[0] - 1][hopperIndex[1] - 1] == 1 and board[hopperIndex[0] - 2][hopperIndex[1] - 2] == 0:
            return True
        else:
            return False
    else:
        return False
def hopNorthWest(board, hopperIndex, pathPiece):
    board[hopperIndex[0]][hopperIndex[1]] = 0
    board[hopperIndex[0] - 1][hopperIndex[1] - 1] = 0
    board[hopperIndex[0] - 2][hopperIndex[1] - 2] = 1
    landedIndex = [hopperIndex[0] - 2, hopperIndex[1] - 2]
    pathPiece.append(convertIndex(landedIndex))
def validateWestHop(board, hopperIndex):
    #checks if valid hopperIndex (hopper to hop exists at said lcoation)
    if board[hopperIndex[0]][hopperIndex[1]] != 1:
        return False
    #if hopper won't jump to invalid area of the board from a West Hop (left side), then continue (has a place to land)
    if hopperIndex[1] >= 2:
        #if there is indeed a peg to hop and no peg in the way of the landing, output true
        if board[hopperIndex[0]][hopperIndex[1] - 1] == 1 and board[hopperIndex[0]][hopperIndex[1] - 2] == 0:
            return True
        else:
            return False
    else:
        return False
def hopWest(board, hopperIndex, pathPiece):
    board[hopperIndex[0]][hopperIndex[1]] = 0
    board[hopperIndex[0]][hopperIndex[1] - 1] = 0
    board[hopperIndex[0]][hopperIndex[1] - 2] = 1
    landedIndex = [hopperIndex[0], hopperIndex[1] - 2]
    pathPiece.append(convertIndex(landedIndex))
def validateSouthWestHop(board, hopperIndex):
    #checks if valid hopperIndex (hopper to hop exists at said lcoation)
    if board[hopperIndex[0]][hopperIndex[1]] != 1:
        return False
    #if hopper won't jump to invalid area of the board from a SouthWest Hop (bottom side), then continue (has a place to land)
    if hopperIndex[0] <= 2:
        #if there is indeed a peg to hop and no peg in the way of the landing, output true
        if board[hopperIndex[0] + 1][hopperIndex[1]] == 1 and board[hopperIndex[0] + 2][hopperIndex[1]] == 0:
            return True
        else:
            return False
    else:
        return False
def hopSouthWest(board, hopperIndex, pathPiece):
    board[hopperIndex[0]][hopperIndex[1]] = 0
    board[hopperIndex[0] + 1][hopperIndex[1]] = 0
    board[hopperIndex[0] + 2][hopperIndex[1]] = 1
    landedIndex = [hopperIndex[0] + 2, hopperIndex[1]]
    pathPiece.append(convertIndex(landedIndex))


#solves the game board and stores the path and moves by using findPath()
def solveBoard(board, path, moves):
    global run
    global startTime
    move = False
    p = 0
    currentTime = time.time()
    #force time out after 20 seconds of not finding a solution (not needed but saves time not waiting for no solution)
    if currentTime - startTime >= 20:
        run = False
    if run == True:
        #base case
        if board.pegCount == 1:
            print "Solution Found"
            run = False
            findPath(board, path, moves)
        else:
            for i in range(len(board.board)):
                for j in range(len(board.board[i])):
                    p = p + 1
                    hopperIndex = [i, j]
                    #checks which hops are possible for current board, makes the hop on a copy and saves the copy
                    if validateNorthEastHop(board.board, hopperIndex) == True:
                        pathPiece = [p]
                        #creates copy from root board
                        newBoard1 = copy.deepcopy(board)
                        #makes the hop on the copied board
                        hopNorthEast(newBoard1.board, hopperIndex, pathPiece)
                        #reduces the pegCount on the copy by 1
                        newBoard1.pegCount = newBoard1.pegCount - 1
                        #stores where the jump came from and where landed in 1-15 format
                        newBoard1.path = pathPiece
                        #stores current board as newBoard's parent (for path finding)
                        newBoard1.parent = board
                        #builds tree from newBoard
                        solveBoard(newBoard1, path, moves)
                    if validateEastHop(board.board, hopperIndex) == True:
                        pathPiece = [p]
                        newBoard2 = copy.deepcopy(board)
                        hopEast(newBoard2.board, hopperIndex, pathPiece)
                        newBoard2.pegCount = newBoard2.pegCount - 1
                        newBoard2.path = pathPiece
                        newBoard2.parent = board
                        solveBoard(newBoard2, path, moves)
                    if validateSouthEastHop(board.board, hopperIndex) == True:
                        pathPiece = [p]
                        newBoard3 = copy.deepcopy(board)
                        hopSouthEast(newBoard3.board, hopperIndex, pathPiece)
                        newBoard3.pegCount = newBoard3.pegCount - 1
                        newBoard3.path = pathPiece
                        newBoard3.parent = board
                        solveBoard(newBoard3, path, moves)
                    if validateNorthWestHop(board.board, hopperIndex) == True:
                        pathPiece = [p]
                        newBoard4 = copy.deepcopy(board)
                        hopNorthWest(newBoard4.board, hopperIndex, pathPiece)
                        newBoard4.pegCount = newBoard4.pegCount - 1
                        newBoard4.path = pathPiece
                        newBoard4.parent = board
                        solveBoard(newBoard4, path, moves)
                    if validateWestHop(board.board, hopperIndex) == True:
                        pathPiece = [p]
                        newBoard5 = copy.deepcopy(board)
                        hopWest(newBoard5.board, hopperIndex, pathPiece)
                        newBoard5.pegCount = newBoard5.pegCount - 1
                        newBoard5.path = pathPiece
                        newBoard5.parent = board
                        solveBoard(newBoard5, path, moves)
                    if validateSouthWestHop(board.board, hopperIndex) == True:
                        pathPiece = [p]
                        newBoard6 = copy.deepcopy(board)
                        hopSouthWest(newBoard6.board, hopperIndex, pathPiece)
                        newBoard6.pegCount = newBoard6.pegCount - 1
                        newBoard6.path = pathPiece
                        newBoard6.parent = board
                        solveBoard(newBoard6, path, moves)



#creates root board and builds tree from it
def findSolution(input, pegCount):
    global run
    global startTime
    run = True
    startTime = time.time()
    input = input
    pegCount = pegCount
    path = []
    moves = []
    board = Board(input, pegCount)
    solveBoard(board, path, moves)
    path, moves = formatPath(path, moves)
    return path, moves


#returns the path of steps to solve board
def findPath(board, path, moves):
    if board.parent != None:
        moves.append(board.board)
        path.append(board.path)
        findPath(board.parent, path, moves)
    else:
        moves.append(board.board)


#converts the input from webPage to a matrix of 1's and 0's, and counts pegs
def processInput(input):
    input = [str(i) for i in input]
    matrix = [[], [], [], [], []]
    pegCount = 0
    for i in input:
        if i == 'on':
            i = 1
            pegCount = pegCount + 1
        else:
            i = 0
    for i in range(15):
        if i == 0:
            if input[i] == 'None':
                matrix[0].append(0)
            else:
                matrix[0].append(1)
        if 0 < i < 3:
            if input[i] == 'None':
                matrix[1].append(0)
            else:
                matrix[1].append(1)
        if 2 < i < 6:
            if input[i] == 'None':
                matrix[2].append(0)
            else:
                matrix[2].append(1)
        if 5 < i < 10:
            if input[i] == 'None':
                matrix[3].append(0)
            else:
                matrix[3].append(1)
        if i > 9:
            if input[i] == 'None':
                matrix[4].append(0)
            else:
                matrix[4].append(1)
    return matrix, pegCount


#formats the path for webApp printing
def formatPath(path, moves):
    outputPath = ''
    outputMoves = ''
    pathForMoves = []
    for i in reversed(path):
        outputPath = outputPath + str(i[0]) + ' -> ' + str(i[1]) + '<br>'
        pathForMoves.append(i)
    cntr1 = 0
    for i in reversed(moves):
        cntr2 = 0
        cntr3 = 0
        #if the first board:
        if cntr1 == 0:
            outputMoves = outputMoves + 'Start:<br>'
        #if not the first board:
        else:
            outputMoves = outputMoves + '--------------------<br>'# + '\n'
            outputMoves = outputMoves + str(pathForMoves[cntr1 - 1][0]) + ' -> ' + str(pathForMoves[cntr1 - 1][1]) + '<br>'
        for j in i:
            for k in j:
                #if first checkbox in row:
                if cntr3 == 0 or cntr3 == 1 or cntr3 == 3 or cntr3 == 6 or cntr3 == 10:
                    if k == 0:
                        outputMoves = outputMoves + '<input type="checkbox" class="row' + str(cntr2) + '">'
                    if k == 1:
                        outputMoves = outputMoves + '<input type="checkbox" class="row' + str(cntr2) + '" checked>'
                #if not first checkbox:
                else:
                    if k == 0:
                        outputMoves = outputMoves + '<input type="checkbox">'
                    if k == 1:
                        outputMoves = outputMoves + '<input type="checkbox" checked>'
                # if last checkbox in row:
                if cntr3 == 0 or cntr3 == 2 or cntr3 == 5 or cntr3 == 9 or cntr3 == 14:
                    outputMoves = outputMoves + '<br>'
                cntr3 = cntr3 + 1
            cntr2 = cntr2 + 1
        cntr1 = cntr1 + 1

    path = outputPath
    moves = outputMoves
    return path, moves


#converts an index into a single number
def convertIndex(index):
    if index == [0,0]:
        index = 1
    if index == [1,0]:
        index = 2
    if index == [1,1]:
        index = 3
    if index == [2,0]:
        index = 4
    if index == [2,1]:
        index = 5
    if index == [2,2]:
        index = 6
    if index == [3,0]:
        index = 7
    if index == [3,1]:
        index = 8
    if index == [3,2]:
        index = 9
    if index == [3,3]:
        index = 10
    if index == [4,0]:
        index = 11
    if index == [4,1]:
        index = 12
    if index == [4,2]:
        index = 13
    if index == [4,3]:
        index = 14
    if index == [4,4]:
        index = 15
    return index