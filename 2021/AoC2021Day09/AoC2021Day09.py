#Parse input
input = [line.strip() for line in open("../Inputs/day09", "r")]

class Point:
    def __init__(self, value):
        self.value = value
        self.inBasin = False
        self.isDeepest = False

positions = []
for line in input:
    positions.append([Point(int(value)) for value in line])

def isValidPoint(x, y):
    if x < 0 or x > len(positions[0]) - 1:
        return False
    if y < 0 or y > len(positions) - 1:
        return False
    return True

def getAdjacents(x, y):
    a = []
    if isValidPoint(x - 1, y):
        a.append([x-1, y])
    if isValidPoint(x, y - 1):
        a.append([x, y - 1])
    if isValidPoint(x + 1, y):
        a.append([x + 1, y])
    if isValidPoint(x, y + 1):
        a.append([x, y + 1])
    return a

def isDeepest(x, y):
    if isValidPoint(x - 1, y):
        if positions[x - 1][y].value <= positions[x][y].value:
            return False
    if isValidPoint(x + 1, y):
        if positions[x + 1][y].value <= positions[x][y].value:
            return False
    if isValidPoint(x, y - 1):
        if positions[x][y - 1].value <= positions[x][y].value:
            return False
    if isValidPoint(x, y + 1):
        if positions[x][y + 1].value <= positions[x][y].value:
            return False

    return True

def getBasinPointCount(x, y):
    ret = 0
    if not positions[x][y].inBasin and positions[x][y].value < 9:
        ret =+ 1
        positions[x][y].inBasin = True
        for p in getAdjacents(x, y):
            ret += getBasinPointCount(p[0], p[1])
    return ret

sum = 0
for iLine, line in enumerate(positions):
    for iPos, pos in enumerate(line):
        if isDeepest(iLine, iPos):
            sum += (pos.value + 1)
            pos.isDeepest = True

print("2021 Day 9, Part 1: " + str(sum))

basinSizes = []
for iLine, line in enumerate(positions):
    for iPos, pos in enumerate(line):
        if pos.isDeepest:
            basinSizes.append(getBasinPointCount(iLine, iPos))
basinSizes.sort()

print("2021 Day 9, Part 2: " + str(basinSizes[-1] * basinSizes[-2] * basinSizes[-3]))