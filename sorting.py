import random

def generateNumbers(numGen):
    numbers = [random.randint(0, 10000) for i in range(numGen)]
    return numbers


#### radixSort ####
def radixSort(list):
	listLength = len(list)

	for i in range(listLength):		#converts elements to strings
		list[i] = str(list[i])

	currentLongest = list[0]
	for i in range(listLength - 1):		#finds the biggest number of digits
		if len(currentLongest) < len(list[i + 1]):
			currentLongest = list[i + 1]

	for i in range(listLength):		#converts elements to integers
		list[i] = int(list[i])

	numDigits = len(currentLongest)
	shift = 1
	loop = 1
	for loop in range(numDigits):		#sorts numbers into buckets
		buckets = [[] for i in range(10)]
		for i in range(listLength):
			digit = (list[i] / shift) % 10
			buckets[digit].append(list[i])
		list = combineBuckets(buckets)

		shift *= 10

	return list

def combineBuckets(buckets):
	bucketLength = len(buckets)
	tmp = []
	for i in range(bucketLength):	#combines buckets
		for j in range(len(buckets[i])):
			tmp.append(buckets[i][j])

	return tmp

#### bubbleSort ####
def bubbleSort(list):
	listLength = len(list) - 1
	sorted = False

	while not sorted:
		sorted = True						#ends function if all elements are in order

		for i in range(listLength):
			if list[i] > list[i + 1]:		#compares element to next element, swaps if smaller
				sorted = False				#indicates not sorted to continue running function
				tmp = list[i + 1]
				list[i + 1] = list[i]
				list[i] = tmp

	return list

#### insertionSort ####
def insertionSort(list):
	listLength = len(list)
	i = 1

	for i in range(listLength):
		n = list[i]					#starts element one as first in sorted list
		loc = i - 1
		while (loc >= 0 and list[loc] > n):		#moves bigger elements over to put smallest in correct spot
			list[loc + 1] = list[loc]
			loc = loc - 1
		list[loc + 1] = n					#places element in correct spot

	return list

#### selectionSort ####
def selectionSort(list):
	for i in range(len(list) - 1):
		index = i
		for j in range(i + 1, len(list)):		#finds next smallest element
			if list[j] < list[index]:
				index = j
		if index != i:
			tmp = list[i]
			list[i] = list[index]				#places next smallest element in front
			list[index] = tmp

	return list

#### mergeSort ####
def mergeSort(list):
	listLength = len(list)

	if listLength > 1:

		split = listLength // 2
		left = list[:split]
		right = list[split:]
		mergeSort(left)			#splits the list recursively until all sublists have size of one
		mergeSort(right)

		l = 0			#counter for left
		r = 0			#counter for right
		li = 0			#counter for list

		while (l < len(left) and r < len(right)):
			if left[l] < right[r]:
				list[li] = left[l]		#assign smaller number to list
				l = l + 1				#look at next element in left list
				li = li + 1				#move counter to next position in left list
			else:
				list[li] = right[r]
				r = r + 1
				li = li + 1

		while l < len(left):
			list[li] = left[l]
			l = l + 1
			li = li + 1

		while r < len(right):
			list[li] = right[r]
			r= r + 1
			li =li + 1

	return list

### quickSort ###
def quickSort(list, first, last):
	if first < last:
		pivot = pivotList(list, first, last)	#split list at pivot and sort, store pivot location
		quickSort(list, first, pivot - 1)		#recursively call quickSort on left half
		quickSort(list, pivot + 1, last)		#recursively call quickSort on right half

	return list

def pivotList(list, first, last):
	pivotValue = list[first]
	pivotPoint = first
	i = first
	while i <= last:
		if list[i] < pivotValue:
			pivotPoint = pivotPoint + 1
			tmp = list[pivotPoint]			#swap the value at pivotPoint with the value at i
			list[pivotPoint] = list[i]
			list[i] = tmp
		i = i + 1
	tmp = list[first]
	list[first] = list[pivotPoint]			#swap the value at first with the value at pivotPoint
	list[pivotPoint] = tmp

	return pivotPoint