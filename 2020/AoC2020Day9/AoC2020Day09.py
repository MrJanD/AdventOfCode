input = [line.strip() for line in open("../Inputs/day9", "r")]

validSetRange = 25
indexToCheck = 25
numbers = []

for line in input:
    numbers.append(int(line))

# Part 1:
def checkNumberSet(set, value):
    for firstNumber in set:
        for secondNumber in set:
            if firstNumber != secondNumber and firstNumber + secondNumber == value:
                return firstNumber, secondNumber
    return 0, 0

while indexToCheck < len(numbers):
    firstNumber, secondNumber = checkNumberSet(numbers[indexToCheck - validSetRange:indexToCheck], numbers[indexToCheck])
    if (firstNumber == 0 and secondNumber == 0):
        print("Day 9, Part 1: " + str(numbers[indexToCheck]))
        break
    indexToCheck += 1


# Part 2:
toSearchFor = numbers[indexToCheck]
numberSpan = 2

def sumList(list):
    sum = 0
    for number in list:
        sum = sum + number
    return sum

def checkSpan(numberSpan):
    startingIndex = 0
    while (startingIndex + numberSpan) <= len(numbers):
        if sumList(numbers[startingIndex : startingIndex + numberSpan]) == toSearchFor:
            return min(numbers[startingIndex : startingIndex + numberSpan]) + max(numbers[startingIndex : startingIndex + numberSpan])
        startingIndex += 1
    return 0

while numberSpan < len(numbers):
    if checkSpan(numberSpan) != 0:
        print("Day 9, Part 2: " + str(checkSpan(numberSpan)))
    numberSpan += 1

