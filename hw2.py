import random

def generateNumbersSorted(numGen):
    numbers = [random.randint(0, 10000) for i in range(numGen)]
    numbers = sorted(numbers)
    return numbers

def closestPairB(list):
    listLength = len(list)

    if listLength == 2:
        d = list[0] - list[1]
        return (list[0], list[1], abs(d))

    else:
        d = None
        #iterate through list
        for i in range(listLength - 1):
            tmp = list[i] - list[i + 1]
            #assign to values if first pair in list or closer than previously stored pair
            if d == None or abs(d) > abs(tmp):
                d = tmp
                p1 = list[i]
                p2 = list[i + 1]
        return (p1, p2, abs(d))


def closestPairR(list):
    listLength = len(list)

    if listLength == 2:
        d = list[0] - list[1]
        return (list[0], list[1], abs(d))

    elif listLength == 3:
        d = None
        #iterate through list
        for i in range(listLength - 1):
            tmp = list[i] - list[i + 1]
            #assign to values if first pair in list or closer than previously stored pair
            if d == None or abs(d) > abs(tmp):
                d = tmp
                p1 = list[i]
                p2 = list[i + 1]
        return (p1, p2, abs(d))


    else:
        #find mid point
        split = listLength // 2

        #split and assign sides
        left = list[:split]
        right = list[split:]

        #recursively call closestPair on both sides
        (lp1, lp2, ld) = closestPairR(left)
        (rp1, rp2, rd) = closestPairR(right)


        #compare results
        md = abs(left[len(left) - 1] - right[0])

        if ld < rd:
            p1 = lp1
            p2 = lp2
            d = ld
        else:
            p1 = rp1
            p2 = rp2
            d = rd

        if md < d:
            p1 = left[len(left) - 1]
            p2 = right[0]
            d = md

        return (p1, p2, d)