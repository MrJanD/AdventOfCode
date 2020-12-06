import math

input = [line.strip() for line in open("../Inputs/day5", "r")]

class BoardingPass:
    def __init__(self, stringPass):
        self.stringPass = stringPass
        self.seatID = self.getRow() * 8 + self.getColumn()

    def getRow(self):
        row = 0
        digitIndex = 6
        while (digitIndex >= 0):
            if self.stringPass[digitIndex] == 'B':
                row = row + 2 ** (6 - digitIndex)
            digitIndex -= 1
        return row

    def getColumn(self):
            column = 0
            digitIndex = 2
            while (digitIndex >= 0):
                if self.stringPass[digitIndex + 7] == 'R':
                    column = column + 2 ** (2 - digitIndex)
                digitIndex -= 1
            return column

boardingPasses = []
for line in input:
    boardingPasses.append(BoardingPass(line))

def getMissingSeatRow():
    lineIndex = 0
    while lineIndex < 128:
        for bP in boardingPasses:
            if [bP.getRow() == lineIndex for bP in boardingPasses].count(True) != 8:
                return lineIndex
        lineIndex += 1

def getMissingSeatColumn():
    columnIndex = 0
    while columnIndex < 8:
        for bP in boardingPasses:
            if [bP.getColumn() == columnIndex for bP in boardingPasses].count(True) != 128:
                return columnIndex
        columnIndex += 1

def getHighestSeatID():
    highestSeatID = 0
    for bp in boardingPasses:
        if highestSeatID < bp.seatID:
            highestSeatID = bp.seatID
    return highestSeatID

def getLowestSeatID():
    lowestSeatID = getHighestSeatID()
    for bp in boardingPasses:
        currentSeatIDRow = bp.getRow()
        currentSeatIDColumn = bp.getColumn()
        if lowestSeatID > bp.seatID:
            lowestSeatID = bp.seatID
    return lowestSeatID

def iDExists(id):
    for bP in boardingPasses:
        if bP.seatID == id:
            return True
    return False

def getOwnID():
    currentSeatID = getLowestSeatID() + 1
    highestSeatID = getHighestSeatID()
    while currentSeatID < highestSeatID:
        if not iDExists(currentSeatID):
            return currentSeatID
        currentSeatID += 1

print("Day 5, Part 1: " + str(getHighestSeatID()))
print("Day 5, Part 2: " + str(getOwnID()))
