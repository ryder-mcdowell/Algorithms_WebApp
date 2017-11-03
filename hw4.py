import copy


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
def hopNorthEast(board, hopperIndex, path):
    board[hopperIndex[0]][hopperIndex[1]] = 0
    board[hopperIndex[0] - 1][hopperIndex[1]] = 0
    board[hopperIndex[0] - 2][hopperIndex[1]] = 1
    landedIndex = [hopperIndex[0] - 2, hopperIndex[1]]
    path.append(convertIndex(landedIndex))
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
def hopEast(board, hopperIndex, path):
    board[hopperIndex[0]][hopperIndex[1]] = 0
    board[hopperIndex[0]][hopperIndex[1] + 1] = 0
    board[hopperIndex[0]][hopperIndex[1] + 2] = 1
    landedIndex = [hopperIndex[0], hopperIndex[1] + 2]
    path.append(convertIndex(landedIndex))
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
def hopSouthEast(board, hopperIndex, path):
    board[hopperIndex[0]][hopperIndex[1]] = 0
    board[hopperIndex[0] + 1][hopperIndex[1] + 1] = 0
    board[hopperIndex[0] + 2][hopperIndex[1] + 2] = 1
    landedIndex = [hopperIndex[0] + 2, hopperIndex[1] + 2]
    path.append(convertIndex(landedIndex))

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
def hopNorthWest(board, hopperIndex, path):
    board[hopperIndex[0]][hopperIndex[1]] = 0
    board[hopperIndex[0] - 1][hopperIndex[1] - 1] = 0
    board[hopperIndex[0] - 2][hopperIndex[1] - 2] = 1
    landedIndex = [hopperIndex[0] - 2, hopperIndex[1] - 2]
    path.append(convertIndex(landedIndex))
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
def hopWest(board, hopperIndex, path):
    board[hopperIndex[0]][hopperIndex[1]] = 0
    board[hopperIndex[0]][hopperIndex[1] - 1] = 0
    board[hopperIndex[0]][hopperIndex[1] - 2] = 1
    landedIndex = [hopperIndex[0], hopperIndex[1] - 2]
    path.append(convertIndex(landedIndex))
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
def hopSouthWest(board, hopperIndex, path):
    board[hopperIndex[0]][hopperIndex[1]] = 0
    board[hopperIndex[0] + 1][hopperIndex[1]] = 0
    board[hopperIndex[0] + 2][hopperIndex[1]] = 1
    landedIndex = [hopperIndex[0] + 2, hopperIndex[1]]
    print landedIndex
    path.append(convertIndex(landedIndex))


run = True
#Builds Tree of Boards
def buildTree(board):
    global run
    print 'run=', run
    print 'pegCount=', board.pegCount
    move = False
    p = 0
    if run == True:
        #base case
        if board.pegCount == 1:
            print "Solution Found"
            run = False
            moves = []
            path = []
            findPath(board, path, moves)
            return path, moves
        else:
            #bucket for all of the hop variations that are possible
            hoppers = []
            for i in range(len(board.board)):
                for j in range(len(board.board[i])):
                    p = p + 1
                    hopperIndex = [i, j]
                    #checks which hops are possible for current board, makes the hop on a copy and saves the copy
                    if validateNorthEastHop(board.board, hopperIndex) == True:
                        path = [p]
                        print '*', path
                        #creates copy from root board
                        newBoard1 = copy.deepcopy(board)
                        #makes the hop on the copied board
                        hopNorthEast(newBoard1.board, hopperIndex, path)
                        #reduces the pegCount on the copy by 1
                        newBoard1.pegCount = newBoard1.pegCount - 1
                        print '**', path
                        newBoard1.path = path
                        #appends the copy to a list of all possible hops for the current board
                        hoppers.append(newBoard1)
                        #marks that a move has been made
                        move = True
                    if validateEastHop(board.board, hopperIndex) == True:
                        path = [p]
                        print '*', path
                        newBoard2 = copy.deepcopy(board)
                        hopEast(newBoard2.board, hopperIndex, path)
                        newBoard2.pegCount = newBoard2.pegCount - 1
                        print '**', path
                        newBoard2.path = path
                        hoppers.append(newBoard2)
                        move = True
                    if validateSouthEastHop(board.board, hopperIndex) == True:
                        path = [p]
                        print '*', path
                        newBoard3 = copy.deepcopy(board)
                        hopSouthEast(newBoard3.board, hopperIndex, path)
                        newBoard3.pegCount = newBoard3.pegCount - 1
                        print '**', path
                        newBoard3.path = path
                        hoppers.append(newBoard3)
                        move = True
                    if validateNorthWestHop(board.board, hopperIndex) == True:
                        path = [p]
                        print '*', path
                        newBoard4 = copy.deepcopy(board)
                        hopNorthWest(newBoard4.board, hopperIndex, path)
                        newBoard4.pegCount = newBoard4.pegCount - 1
                        print '**', path
                        newBoard4.path = path
                        hoppers.append(newBoard4)
                        move = True
                    if validateWestHop(board.board, hopperIndex) == True:
                        path = [p]
                        print '*', path
                        newBoard5 = copy.deepcopy(board)
                        hopWest(newBoard5.board, hopperIndex, path)
                        newBoard5.pegCount = newBoard5.pegCount - 1
                        print '**', path
                        newBoard5.path = path
                        hoppers.append(newBoard5)
                        move = True
                    if validateSouthWestHop(board.board, hopperIndex) == True:
                        path = [p]
                        print '*', path
                        newBoard6 = copy.deepcopy(board)
                        hopSouthWest(newBoard6.board, hopperIndex, path)
                        newBoard6.pegCount = newBoard6.pegCount - 1
                        print '**', path
                        newBoard6.path = path
                        hoppers.append(newBoard6)
                        move = True

        #if a move was made, add all the copies as children of their parent's board and call buildTree on them
        if move == True:
            for i in range(len(hoppers)):
                board.children.append(hoppers[i])
                hoppers[i].parent = board
                buildTree(hoppers[i])


#creates root board and builds tree from it
def findSolution(input, pegCount):
    input = input
    pegCount = pegCount
    board = Board(input, pegCount)
    buildTree(board)
    # need to get path here !
    # formatPath(path, moves)
    # return path, moves

#returns the path of steps to solve board
def findPath(board, path, moves):
    if board.parent != None:
        print '$$$$$$', board.board
        moves.append(board.board)
        print board.path
        path.append(board.parent.path)
        findPath(board.parent, path, moves)
    else:
        print '$$$$$$', board.board
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
    for i in path:
        outputPath = outputPath + str(i) + '\n'
    for i in moves:
        outputMoves = outputMoves + str(i) + '\n'

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