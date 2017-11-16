import random

class Node:
    def __init__(self, id):
        self.id = id
        self.visited = False
        self.paths = []

class priorityQueue:
    def __init__(self):
        self.queue = {}

    def enqueue(self, node, shortestPath, previous):
        self.queue[node] = (shortestPath, previous)

    def delete(self, node):
        del self.queue[node]

    def returnTop(self):
        lowest = None
        lowestNode = None
        for node,shortestPath in self.queue.items():
            if shortestPath[0] < lowest or lowest == None:
                lowest = shortestPath[0]
                lowestNode = node
        return lowestNode.id

    def printQueue(self):
        print '\n', "Queue="
        for node,shortestPath in self.queue.items():
            print node.id, "->", shortestPath


#finds the shortest Path between start and destination nodes and returns path and total weight
def findShortestPath(input, start, destination):
    graph = formatInput(input)
    print "graph=", graph

    #build initial queue
    queue = priorityQueue()
    for nodeID, node in graph.items():
        if nodeID == start:
            queue.enqueue(graph[nodeID], 0, None)
        else:
            queue.enqueue(graph[nodeID], 999999, None)
    queue.printQueue()

    deleted = {}
    current = start
    previousKey = current
    previousWeight = 0
    while current != destination:
        print '--------------------------------------'
        print "NEWLOOP", current
        #for every available path for current node
        for path in graph[current].paths:
            if path[0] not in deleted:
                print path
                #sets the current nodeID as child, the weight of the edge to get there as weight, and node as the object associated with the nodeID
                child = path[0]
                weight = int(path[1])
                node = graph[child]
                #if current weight is less than stored weight, change it
                print "$", weight, queue.queue[node][0]
                if weight + previousWeight < queue.queue[node][0]:                  ######### Here's where error was. Before it was just weight and not weight + previousWeight #########
                    queue.queue[node] = (weight + previousWeight, current)

        #deletes current node from queue after it has been checked and saves it
        deleted[current] = (queue.queue[graph[current]][0], queue.queue[graph[current]][1])
        queue.delete(graph[current])
        print "deleted=", deleted

        #sets current node as the top of the priority queue
        current = queue.returnTop()
        print "*", current
        previousWeight = queue.queue[graph[current]][0]
        print "*", previousWeight

        queue.printQueue()

    print '--------------------------------------'
    print '--------------------------------------'
    #find and save path and total weight
    path = findPath(graph, queue, deleted, start, destination, current)
    print "Path=", path
    return path


#finds and returns path shortest path from start to destination
def findPath(graph, queue, deleted, start, destination, current):
    path = []
    #adds total weight to path
    path.append(queue.queue[graph[current]][0])
    #adds final node in queue to deleted
    deleted[current] = (queue.queue[graph[current]][0], queue.queue[graph[current]][1])
    #sets destination as previous node until it's the same as start
    while start != destination:
        path.append(destination)
        destination = deleted[destination][1]
        if destination == start:
            path.append(start)
    return path


#generates input based on count input
def generateInput(count):
    letterChoices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    input = '-,'
    count = int(count)
    for i in range(count):
        input = input + letterChoices[i]
        if i != (count - 1):
            input = input + ','
    input = input + '\n'
    cntr = 0
    for letter in input:
        if letter != '-' and letter != ',' and letter != '\n':
            input = input + letter + ','
            for i in range(count):
                if i == cntr:
                    input = input + '-'
                    if i != (count - 1):
                        input = input + ','
                else:
                    randomNumber = random.randint(0,13)
                    if randomNumber == 0 or randomNumber > 9:
                        randomNumber = '-'
                    randomNumber = str(randomNumber)
                    input = input + randomNumber
                    if i != (count - 1):
                        input = input + ','
            input = input + '\n'
            cntr = cntr + 1
    return input


#formats input for findShortestPath function
def formatInput(input):
    input = input.replace(' ', '').replace('\r', '')
    input = input.split('\n')
    for i in input:
        print i
    #sets first line of input as the inputKey
    inputKey = input[0]
    inputKey = inputKey.split(',')
    #removes key-line from input
    input.remove(input[0])
    print '\n', '!!->', inputKey, '<-!!'
    print '-----------------------------------------', '\n'
    graph = {}
    #adds nodes to dictionary->graph (value = letter, key = node Object)
    for i in input:
        i = i.split(',')
        print i[0]
        node = Node(i[0])
        node.id = i[0]
        graph[i[0]] = node
        #adds node's chilren as tuple (edge value, dictKey)
        cntr = 0
        for j in i:
            #skips over dashes and the letter
            if j != '-' and cntr != 0:
                node.paths.append((inputKey[cntr],j))
            cntr = cntr + 1
        print node.paths
    print '-----------------------------------------', '\n'
    return graph


#formats ouput for displaying on webpage (path and weight)
def formatOutput(path, destination):
    distance = path[0]
    del path[0]
    pathOutput = ''
    for i in reversed(path):
        pathOutput = pathOutput + i
        if i != destination:
            pathOutput = pathOutput + ', '
    return pathOutput, distance