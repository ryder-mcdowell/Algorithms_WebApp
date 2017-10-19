#splits input to a list of all nodes (color + id)
def splitInput(input):
    nodes = input.replace(' ', '').replace('\n', '|').replace('\r', '')
    nodes = nodes.replace('->','|').replace(' | ','|')
    nodes = nodes.split('|')
    nodes = [str(n) for n in nodes if n !='']
    return nodes


#splits input to a list of all nodes (colors only)
def onlyColors(input):
    nodes = input.replace(' ', '').replace('\n', '|').replace('\r', '')
    nodes = nodes.replace('->','|').replace('_', '|').replace(' | ','|')
    nodes = nodes.split('|')
    nodes = [str(n) for n in nodes if n != '']
    colors = []
    #isolate colors
    for i in range(len(nodes)):
        #gets rid of id's by focusing colors and skipping id's
        if i % 2 !=0:
            pass
        else:
            colors.append(nodes[i])
    #join color pairs for combination printing
    for i in range(len(colors) / 2):
        colors[i:i+2] = [' -> '.join(colors[i:i+2])]
    return colors


#creates graph (dictionary)
def createGraph(input):
    nodes = splitInput(input)
    graph = {}
    for i in range(len(nodes)):
        #focuses every other element of list(root nodes)
        if i % 2 != 0:
            pass
        else:
            nodeRoot = nodes[i]
            nodePoint = nodes[i + 1]
            #if is a new node(pointed at), add it (not pointing anywhere)
            if nodePoint not in graph:
                graph[nodePoint] = []
            #if is a new node(root), add it and where its pointing
            if nodeRoot not in graph:
                graph[nodeRoot] = [nodePoint]
            #node already exists, append where its pointing
            else:
                graph[nodeRoot].append(nodePoint)
    return graph


#counts color combinations and formats them for output
def colorCombinations(input):
    colorPairs = onlyColors(input)
    combinations = {}
    #creates dictionary of color combos and their tallies
    for i in range(len(colorPairs)):
        pair = colorPairs[i]
        #if the pair doesn't exit, add it
        if pair not in combinations:
            combinations[pair] = 1
        #if the pair does exist, add to running tally
        else:
            combinations[pair] += 1
    output = formatCombinations(combinations)
    return output


#formats color combos for printing (output)
def formatCombinations(combinations):
    output = ''
    for key, value in combinations.items():
         output += key + ' = ' + str(value) + '<br>'
    return output

#formats graph structure for printing (output)
def formatStructure(graph):
    output = ''
    for key, value in graph.items():
        output += key + '<br>'
        if value != None:
            for i in range(len(value)):
                output += "&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp==> " + value[i] + '<br>'
    return output