from flask import Flask, request, render_template, helpers
from hw1 import *
from hw2 import *
from hw3 import *
from hw4 import *
from hw5 import *
import random

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def base():
    if request.method == 'GET':
        return render_template('home.html')

@app.route("/calculator", methods=['GET', 'POST'])
def calculator():
    if request.method == 'GET':
        return render_template('calculator.html', result=None)

    elif request.method == 'POST':
        n1 = int(request.form['n1'])
        n2 = int(request.form['n2'])
        print n1, n2

        operator = request.form['operator']
        if operator == '+':
            result = n1 + n2
            return render_template('calculator.html', result=result)
        if operator == '-':
            result = n1 - n2
            return render_template('calculator.html', result=result)
        if operator == 'x':
            result = n1 * n2
            return render_template('calculator.html', result=result)
        if operator == '/':
            result = n1 / n2
            return render_template('calculator.html', result=result)


@app.route('/hw1', methods=['GET', 'POST'])
def sorting():
    if request.method == 'GET':
        return render_template('hw1.html')

    elif request.method == 'POST':
        if request.form['button'] == 'Generate':
            numGen = request.form['number']
            numGen = int(numGen)
            numGen = generateNumbers(numGen)
            return render_template('hw1.html', numGen=numGen)

        if request.form['button'] == 'RadixSort':
            numbers = request.form['numbers']
            numbers = numbers.replace(' ','').split('\n')
            numbers = [n.strip('\r') for n in numbers]
            numbers = [int(n) for n in numbers if n != '']
            sortedNumbers = radixSort(numbers)
            return render_template('hw1.html', sortedNumbers=sortedNumbers)

        if request.form['button'] == 'BubbleSort':
            numbers = request.form['numbers']
            numbers = numbers.replace(' ','').split('\n')
            numbers = [n.strip('\r') for n in numbers]
            numbers = [int(n) for n in numbers if n != '']
            sortedNumbers = bubbleSort(numbers)
            return render_template('hw1.html', sortedNumbers=sortedNumbers)

        if request.form['button'] == 'InsertionSort':
            numbers = request.form['numbers']
            numbers = numbers.replace(' ','').split('\n')
            numbers = [n.strip('\r') for n in numbers]
            numbers = [int(n) for n in numbers if n != '']
            sortedNumbers = insertionSort(numbers)
            return render_template('hw1.html', sortedNumbers=sortedNumbers)

        if request.form['button'] == 'SelectionSort':
            numbers = request.form['numbers']
            numbers = numbers.replace(' ','').split('\n')
            numbers = [n.strip('\r') for n in numbers]
            numbers = [int(n) for n in numbers if n != '']
            sortedNumbers = selectionSort(numbers)
            return render_template('hw1.html', sortedNumbers=sortedNumbers)

        if request.form['button'] == 'MergeSort':
            numbers = request.form['numbers']
            numbers = numbers.replace(' ','').split('\n')
            numbers = [n.strip('\r') for n in numbers]
            numbers = [int(n) for n in numbers if n != '']
            sortedNumbers = mergeSort(numbers)
            return render_template('hw1.html', sortedNumbers=sortedNumbers)

        if request.form['button'] == 'QuickSort':
            numbers = request.form['numbers']
            numbers = numbers.replace(' ','').split('\n')
            numbers = [n.strip('\r') for n in numbers]
            numbers = [int(n) for n in numbers if n != '']
            sortedNumbers = quickSort(numbers, 0, len(numbers) - 1)
            return render_template('hw1.html', sortedNumbers=sortedNumbers)


@app.route('/hw2', methods=['GET', 'POST'])
def closestPair():
    if request.method == 'GET':
        return render_template('hw2.html', difference=None)

    elif request.method == 'POST':
        if request.form['button'] == 'Generate':
            numGen = request.form['number']
            numGen = int(numGen)
            numGen = generateNumbersSorted(numGen)
            return render_template('hw2.html', numGen=numGen, difference=None)

        if request.form['button'] == 'Brute Force':
            numbers = request.form['numbers']
            numbers = numbers.replace(' ','').split('\n')
            numbers = [n.strip('\r') for n in numbers]
            numbers = [int(n) for n in numbers if n != '']
            values = closestPairB(numbers)
            pair = (values[0],values[1])
            difference = (values[2])
            return render_template('hw2.html', pair=pair, difference=difference)

        if request.form['button'] == 'Recursive':
            numbers = request.form['numbers']
            numbers = numbers.replace(' ','').split('\n')
            numbers = [n.strip('\r') for n in numbers]
            numbers = [int(n) for n in numbers if n != '']
            values = closestPairR(numbers)
            pair = (values[0], values[1])
            difference = (values[2])
            return render_template('hw2.html', pair=pair, difference=difference)


@app.route('/hw3', methods=['GET', 'POST'])
def colorGraph():
    if request.method == 'GET':
        return render_template('hw3.html')

    elif request.method == 'POST':
        if request.form['button'] == 'Process':
            input = request.form['input']
            graph = createGraph(input)
            combinationsOutput = colorCombinations(input)
            structureOutput = formatStructure(graph)
            return render_template('hw3.html', combinationsOutput=combinationsOutput, structureOutput=structureOutput)


@app.route('/hw4', methods=['GET', 'POST'])
def pegSolitaireSolver():
    if request.method == 'GET':
        return render_template('hw4.html')

    elif request.method == 'POST':
        if request.form['button'] == 'Find Solution':
            input = []
            for i in range(15):
                j = str(i)
                input.append(request.form.get('check' + j))
            input, pegCount = processInput(input)
            path, moves = findSolution(input, pegCount)
            return render_template('hw4.html', path=path, moves=moves)


@app.route('/hw5', methods=['GET', 'POST'])
def shortestPath():
    if request.method == 'GET':
        return render_template('hw5.html')

    elif request.method == 'POST':
        if request.form['button'] == 'Generate':
            count = request.form['count']
            input = generateInput(count)
            return render_template('hw5.html', input=input)

        if request.form['button'] == 'ShortestPath':
            input = request.form['input']
            start = request.form['start']
            destination = request.form['destination']
            path = findShortestPath(input, start, destination)
            path, distance = formatOutput(path, destination)
            return render_template('hw5.html', input=input, path= path, distance=distance)

@app.route('/final_project', methods=['GET', 'POST'])
def travelingSalesman():
    if request.method == 'GET':
        return render_template('final_project.html')

    elif request.method == 'POST':
        if request.form['button'] == 'Generate':
            count = request.form['count']
            input = generateInput(count)
            return render_template('hw5.html', input=input)

        if request.form['button'] == 'Compute Path':
            pass


if __name__ == '__main__':
    app.run(debug=True)