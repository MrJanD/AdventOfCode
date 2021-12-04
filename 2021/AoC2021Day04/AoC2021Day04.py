input = [line.strip() for line in open("../Inputs/day04", "r")]
input = list(filter(('').__ne__, input))
drawnInput = [int(number) for number in input[0].split(',')]

class BingoBox:
    def __init__(self, intBox):
        self.Box =[]
        for line in intBox:
            intLine = []
            for number in line.split():
                intLine.append(int(number))
            self.Box.append(intLine)
        self.Match = None


    def xMatch(self, drawnList):
        for line in self.Box:
            matchCounter = 0
            for number in line:
                if number in drawnList:
                    matchCounter += 1
            if matchCounter == 5:
                self.Match = line
                return line

        return None

    def yMatch(self, drawnList):
        for yPos in range(4):
            matchCounter = 0
            for line in self.Box:
                if line[yPos] in drawnList:
                    matchCounter += 1
            if matchCounter == 5:
                self.Match = line
                return [self.Box[yPos][0], self.Box[yPos][1], self.Box[yPos][2], self.Box[yPos][3], self.Box[yPos][4]]

        return None

    def anyMatch(self, drawnList):
        if self.Match != None:
            return self.Match

        if self.xMatch(drawnList) != None:
            return self.xMatch(drawnList)

        if self.yMatch(drawnList) != None:
            return self.yMatch(drawnList)

        return None

    def noMatch(self, drawnList):
        unmatchedList = []
        for line in self.Box:
            for number in line:
                if number not in drawnList:
                    unmatchedList.append(number)

        return unmatchedList

    def noMatchSum(self, drawnList):
        sum = 0
        for number in self.noMatch(drawnList):
            sum += number

        return sum

boxList = []
startingElement = 1
endElement = startingElement + 5

while len(input) >= endElement:
    boxList.append(BingoBox(input[startingElement:endElement]))
    startingElement += 5
    endElement += 5

def getResultList():
    resultList = []
    for nextDrawnIndex in range(len(drawnInput)):
        for box in boxList:
            if box.Match == None:
                if box.anyMatch(drawnInput[0:nextDrawnIndex]) != None:
                    resultList.append(box.noMatchSum(drawnInput[0:nextDrawnIndex]) * drawnInput[nextDrawnIndex - 1])
    return resultList

L = getResultList()

print("2021 Day 4, Part 1: " + str(L[0]))
print("2021 Day 4, Part 2: " + str(L[-1]))