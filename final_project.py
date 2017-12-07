from __future__ import division
import copy, random

class Node:
    def __init__(self, id):
        self.id = id
        self.visited = False
        self.paths = []

class Wolf:
    def __init__(self, id):
        self.id = id
        #self.alpha = False
        self.path = []
        self.pathWeight = 0
        self.current = None
        self.hopsAway = 0
        self.fitnessScore = 0
        self.softAndFurry = True

class WolfPack:
    def __init__(self,id):
        self.id = id
        self.members = []
        self.alpha = None
        self.visited = []

    def addWolves(self, packSize, location):
        for i in range(packSize):
            #if not self.members:
            wolf = Wolf(i)
            wolf.current = location
            if i == 0:
                self.alpha = wolf
            self.members.append(wolf)

    def printMembers(self):
        print "WOLFPACK:", self.id, '\n'
        for wolf in self.members:
            print wolf.id, ':', wolf.current, ":", wolf.pathWeight
        print '-----------------------------------------', '\n'


#builds intitial population of "high-fitness wolves" for genetic algorithm
def buildPopulation(input, graph, start, packSize):
    packSize = int(packSize)

    #create pack
    wolfPack = WolfPack(0)
    wolfPack.addWolves(packSize, start)

    #counter for appending start
    counter = 0
    #end wolf population for genetic algo
    population = []

    while len(population) < packSize:
        #check for new alpha
        previousAlphaWeight = wolfPack.alpha.pathWeight
        newAlphaRatio = 0.8
        for wolf in wolfPack.members:
            #if wolf is far away and their path looks good, swap who's alpha
            if wolf.hopsAway > 3 and wolf.pathWeight / previousAlphaWeight < newAlphaRatio:
                #print 'Wolf:', wolf.id, "| Is the New Alpha"
                wolfPack.alpha = wolf
                newAlphaRatio = wolf.pathWeight / previousAlphaWeight
                tmp = copy.deepcopy(wolfPack.members[0])
                index = wolfPack.members.index(wolf)
                wolfPack.members[0] = wolf
                wolfPack.members[index] = tmp

        #copy of graph to avoid deleting from source
        graphCopy = copy.deepcopy(graph)
        #stores alpha weight before it makes a move decision for comparing other wolf's path weights
        previousAlphaWeight = wolfPack.alpha.pathWeight
        for wolf in wolfPack.members:
            #if wolf gets too far away from pack and their path isn't looking good, return to alpha
            if wolf.hopsAway > 3 and wolf.pathWeight / previousAlphaWeight > 1.3 and len(wolf.path) != len(graph):
                #print 'Wolf:', wolf.id, "| Returned to Alpha"
                #change relevant info to alpha's info
                wolf.hopsAway = 0
                wolf.current = copy.copy(wolfPack.alpha.current)
                wolf.path = copy.copy(wolfPack.alpha.path)
                wolf.pathWeight = copy.copy(wolfPack.alpha.pathWeight)
            else:
                #path options for each wolf
                pathOptions = graphCopy[wolf.current].paths
                shortestPath = None
                delete = True
                #counter for deleting paths that have already been taken
                counter4 = 0
                #find shortest available path
                for path in pathOptions:
                    #counter for path deletion index
                    counter4 = counter4 + 1
                    #stops wolf from going to an already visited location
                    if path[0] not in wolf.path:
                        if shortestPath == None:
                            shortestPath = path
                            delIndex = counter4
                        elif path[1] < shortestPath[1]:
                            shortestPath = path
                            delIndex = counter4

                #if no path got assigned (either a wolf has already taken only available path or wolf has made it back to start)
                if shortestPath == None:
                    for path in graph[wolf.current].paths:
                        #in case where there is only one possible path to take and its already been taken, take it anyways
                        if path[0] not in wolf.path:
                            if shortestPath == None:
                                shortestPath = path     #check if even need this
                                delete = False
                            elif path[1] < shortestPath[1]:
                                shortestPath = path
                                delete = False
                        #if path option is the start and all nodes have been visited, then a solution has been found
                        elif path[0] == start:
                            if len(wolf.path) == len(graph):
                                wolf.path.append(start)
                                wolf.pathWeight = wolf.pathWeight + path[1]
                                wolf.current = start
                                population.append(wolf)
                                #print "SOLUTION FOUND | FINAL WEIGHT = ", wolf.pathWeight

                #update wolf's status/info
                if counter == 0:
                    wolf.path.append(start)
                if shortestPath != None:
                    wolf.path.append(shortestPath[0])
                    wolf.pathWeight = wolf.pathWeight + shortestPath[1]
                    wolf.current = shortestPath[0]
                    wolf.hopsAway = wolf.hopsAway + 1
                    #del path option so other wolves don't take the same one
                    if delete == True:
                        del pathOptions[delIndex - 1]


        counter = counter + 1

    #print '\n', '-----------------------------------------'
    return population

#genetic algorithm!
def geneticAlgorithm(population, packSize, graph, generations, recombinationRate, mutationRate):
    packSize = int(packSize)
    generations = int(generations)
    recombinationRate = float(recombinationRate)
    mutationRate = float(mutationRate)
    IDcounter = packSize
    for i in range(generations):
        #print "Generation", i + 1
        totalFitness = evaluatePopulation(population)
        if i == 0:
            startFitness = totalFitness
        parents = selectParents(population, totalFitness)
        IDcounter = mate(parents, graph, population, recombinationRate, mutationRate, IDcounter)
        survivalOfTheFittest(population, packSize)
        #print "Fitness = ", totalFitness
        #print '------------------'

    totalFitness = 0
    for wolf in population:
        totalFitness = totalFitness + wolf.fitnessScore
    #print "Start Fitness:", startFitness, ' | ', 'End Fitness:', totalFitness
    return population

#evaluates fitness of wolf population
def evaluatePopulation(population):
    #calculate wolves' fitness score and the total fitness of the population
    totalFitness = 0
    for wolf in population:
        wolf.fitnessScore = round((((1 / wolf.pathWeight) * 10000) ** 5) / 10000)
        totalFitness = totalFitness + wolf.fitnessScore
    return totalFitness

#selects two parents for "breeding"
def selectParents(population, totalFitness):
    #two random numbers for picking parents based on a fraction of total total fitness (more fit have higher chance of being picked)
    random1 = random.randint(1, totalFitness)
    random2 = random.randint(1, totalFitness)
    #area for random numbers to fall into which decides which wolf gets picked
    pickCheck = 0
    #counter for picking second parent wolf when same wolf gets picked twice
    counter = 0
    #picks two parents
    parents = [None, None]
    for wolf in population:
        counter = counter + 1
        picked = (False, None)
        pickCheck = pickCheck + wolf.fitnessScore
        if random1 <= pickCheck and parents[0] == None:
            parents[0] = wolf
            picked = (True, counter)
        if random2 <= pickCheck and parents[1] == None:
            if picked[0] == False:
                parents[1] = wolf
            #in the case where the same wolf gets picked by both random values, pick a new random value
            if picked[0] == True:
                values = list(range(len(population)))
                values.remove(picked[1] - 1)
                random3 = random.choice(values)
                parents[1] = population[random3]
    return parents

#creates child wolf by recombining parent's paths and has chance of mutation
def mate(parents, graph, population, recombinationRate, mutationRate, IDcounter):
    parent1 = parents[0]
    parent2 = parents[1]
    pup = Wolf(IDcounter)    #chance for twins+?
    IDcounter = IDcounter + 1

    #swaps genes from parent1 genes into parent2 genes which = child genes
    pup.path = copy.copy(parent2.path)
    recombinations = round(len(pup.path) // 2 * recombinationRate)
    for i in range(int(recombinations)):
        switchpoint = random.randint(0, len(pup.path) - 1)
        gene = parent1.path[switchpoint]
        for j in range(len(pup.path)):
            if pup.path[j] == gene:
                pup.path[j] = pup.path[switchpoint]
                pup.path[switchpoint] = gene
    #finds child's new total path weight
    for i in range(len(pup.path) - 1):
        current = pup.path[i]
        next = pup.path[i + 1]
        for path in graph[current].paths:
            if path[0] == next:
                pup.pathWeight = pup.pathWeight + path[1]
    pup.fitnessScore = round((((1 / pup.pathWeight) * 10000) ** 5) / 10000)

    # mutation
    mutationWindow = round(mutationRate * 100)
    mutationPick = random.randint(0, 100)
    if mutationPick < mutationWindow:
        switchpoint1 = random.randint(0, len(pup.path) - 1)
        switchpoint2 = random.randint(0, len(pup.path) - 1)
        #print "Mutation! Swapping", pup.path[switchpoint1], "with", pup.path[switchpoint2]
        #print "Before:\n", pup.path
        tmp = pup.path[switchpoint1]
        pup.path[switchpoint1] = pup.path[switchpoint2]
        pup.path[switchpoint2] = tmp
        #print "After:\n", pup.path, "\n"

    #add pup to the population
    population.append(pup)
    return IDcounter

#eliminates the least fit wolves in the pack
def survivalOfTheFittest(population, packSize):
    populationDelta = len(population) - packSize
    #if the pack is too large, kill the least fit to make the pack size == packSize
    if populationDelta > 0:
        for killSpot in range(populationDelta):
            leastFit = population[0]
            eliminateIndex = 0
            for i in range(len(population)):
                if population[i].fitnessScore < leastFit.fitnessScore:
                    leastFit = population[i]
                    eliminateIndex = i
            #print 'wolf', population[eliminateIndex].id, 'did not survive'
            del population[eliminateIndex]

#generates input based on count input
def generateInput(count):
    letterChoices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    input = '-,'
    count = int(count)
    for i in range(count):
        input = input + letterChoices[i]
        if i != (count - 1):
            input = input + ','
    input = input + '\n'
    counter = 0
    for letter in input:
        if letter != '-' and letter != ',' and letter != '\n':
            input = input + letter + ','
            for i in range(count):
                if i >= counter:
                    input = input + '-'
                    if i != (count - 1):
                        input = input + ','
                else:
                    randomNumber = random.randint(1,99)
                    randomNumber = str(randomNumber)
                    input = input + randomNumber
                    if i != (count - 1):
                        input = input + ','
            input = input + '\n'
            counter = counter + 1
    inputMatrix = input.split('\n')
    inputMatrix2 = []
    for i in inputMatrix:
        i = i.split(',')
        inputMatrix2.append(i)
    inputMatrix = inputMatrix2
    input = ''
    for i in range(len(inputMatrix)):
        for j in range(len(inputMatrix[i]) - 1):
            if inputMatrix[i][j] != '-' and inputMatrix[i][j] != ',' and j != 0 and i != 0:
                tmp = inputMatrix[i][j]
                inputMatrix[j][i] = tmp
    for i in range(len(inputMatrix)):
        for j in range(len(inputMatrix[i])):
            if inputMatrix[i][j] != '':
                input = input + inputMatrix[i][j]
                if j == count:
                    input = input + '\n'
                if j != count:
                    input = input + ','
    return input

#formats input for findShortestPath function
def formatInput(input):
    input = input.replace(' ', '').replace('\r', '')
    input = input.split('\n')
    #sets first line of input as the inputKey
    inputKey = input[0]
    inputKey = inputKey.split(',')
    #removes key-line from input
    input.remove(input[0])
    graph = {}
    #adds nodes to dictionary->graph (value = letter, key = node Object)
    for i in input:
        i = i.split(',')
        if i[0] == '':
            del i[0]
        else:
            node = Node(i[0])
            node.id = i[0]
            graph[i[0]] = node
        #adds node's chilren as tuple (edge value, dictKey)
        cntr = 0
        for j in i:
            #skips over dashes and the letter
            if j != '-' and cntr != 0:
                node.paths.append((inputKey[cntr],int(j)))
            cntr = cntr + 1
    return graph

#returns the path and path weight from wolf in population with smallest path weight
def returnPath(population):
    smallestWeight = None
    path = None
    pathOutput = ''
    for wolf in population:
        if wolf.pathWeight < smallestWeight or smallestWeight == None:
            smallestWeight = wolf.pathWeight
            path = wolf.path
    for i in range(len(path)):
        pathOutput = pathOutput + path[i]
        if i != len(path):
            pathOutput = pathOutput + ', '
    return smallestWeight, pathOutput
