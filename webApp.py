from flask import Flask, request, render_template, helpers
from sorting import *
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


@app.route('/sorting', methods=['GET', 'POST'])

def sorting():
    if request.method == 'GET':
        return render_template('sorting.html')

    elif request.method == 'POST':
        if request.form['button'] == 'Generate':
            numGen = request.form['number']
            numGen = int(numGen)
            numGen = generateNumbers(numGen)
            print numGen
            return render_template('sorting.html', numGen=numGen)

        if request.form['button'] == 'RadixSort':
            numbers = request.form['numbers']
            numbers = numbers.replace(' ','').split('\n')
            numbers = [n.strip('\r') for n in numbers]
            numbers = [int(n) for n in numbers if n != '']
            sortedNumbers = radixSort(numbers)
            return render_template('sorting.html', sortedNumbers=sortedNumbers)

        if request.form['button'] == 'BubbleSort':
            numbers = request.form['numbers']
            numbers = numbers.replace(' ','').split('\n')
            numbers = [n.strip('\r') for n in numbers]
            numbers = [int(n) for n in numbers if n != '']
            sortedNumbers = bubbleSort(numbers)
            return render_template('sorting.html', sortedNumbers=sortedNumbers)

        if request.form['button'] == 'InsertionSort':
            numbers = request.form['numbers']
            numbers = numbers.replace(' ','').split('\n')
            numbers = [n.strip('\r') for n in numbers]
            numbers = [int(n) for n in numbers if n != '']
            sortedNumbers = insertionSort(numbers)
            return render_template('sorting.html', sortedNumbers=sortedNumbers)

        if request.form['button'] == 'SelectionSort':
            numbers = request.form['numbers']
            numbers = numbers.replace(' ','').split('\n')
            numbers = [n.strip('\r') for n in numbers]
            numbers = [int(n) for n in numbers if n != '']
            sortedNumbers = selectionSort(numbers)
            return render_template('sorting.html', sortedNumbers=sortedNumbers)

        if request.form['button'] == 'MergeSort':
            numbers = request.form['numbers']
            numbers = numbers.replace(' ','').split('\n')
            numbers = [n.strip('\r') for n in numbers]
            numbers = [int(n) for n in numbers if n != '']
            sortedNumbers = mergeSort(numbers)
            return render_template('sorting.html', sortedNumbers=sortedNumbers)

        if request.form['button'] == 'QuickSort':
            numbers = request.form['numbers']
            numbers = numbers.replace(' ','').split('\n')
            numbers = [n.strip('\r') for n in numbers]
            numbers = [int(n) for n in numbers if n != '']
            sortedNumbers = quickSort(numbers, 0, len(numbers) - 1)
            return render_template('sorting.html', sortedNumbers=sortedNumbers)



if __name__ == '__main__':
    app.run(debug=True)