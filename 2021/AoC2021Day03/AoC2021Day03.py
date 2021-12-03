input = [line.strip() for line in open("../Inputs/day03", "r")]

def getCountsList(bitValue):
    counter = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for line in input:
        lineList = list(line)
        for index, value in enumerate(lineList):
            if value == bitValue:
                counter[index] += 1

    return counter

def countsListToBinaryString(counter):
    result = ""

    for count in counter:
        if count > len(input) / 2:
            result += "1"
        else:
            result += "0"

    return result

def countOnesAtPos(list, pos):
    counter = 0

    for line in list:
        if line[pos] == "1":
            counter += 1

    return counter

def removeLeastCommonAt(list, pos):
    listCopy = list.copy()

    value = "0"
    if countOnesAtPos(listCopy, pos) >= len(listCopy) / 2:
        value = "1"

    for line in list:
        if line[pos] != value:
            listCopy.remove(line)

    return listCopy

def removeMostCommonAt(list, pos):
    listCopy = list.copy()

    value = "0"
    if countOnesAtPos(listCopy, pos) < len(listCopy) / 2:
        value = "1"

    for line in list:
        if line[pos] != value:
            listCopy.remove(line)

    return listCopy

def getOxygenGeneratorRating():
    inputCopy = input.copy()
    for index in range(len(input[0])):
        inputCopy = removeLeastCommonAt(inputCopy, index)
    return inputCopy[0]

def getCo2ScrubberRating():
    inputCopy = input.copy()
    for index in range(len(input[0])):
        if len(inputCopy) > 1:
            inputCopy = removeMostCommonAt(inputCopy, index)
    return inputCopy[0]

gamma = int(countsListToBinaryString(getCountsList("1")), 2)
epsilon = int(countsListToBinaryString(getCountsList("0")), 2)

print("2021 Day 3, Part 1: " + str(gamma * epsilon))
print("2021 Day 3, Part 2: " + str(int(getOxygenGeneratorRating(), 2) * int(getCo2ScrubberRating(), 2)))

