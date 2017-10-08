from flask import Flask, request, render_template, helpers
from hw1 import *
from hw2 import *
import random

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def base():
    if request.method == 'GET':
        return render_template('base.html')

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



if __name__ == '__main__':
    app.run(debug=True)