#Parse input
input = [line.strip() for line in open("../Inputs/day11.ex", "r")]

class Point:
    def __init__(self, value, x = 0, y = 0):
        self.value = value
        self.flashing = False
        self.flashCounter = 0
        self.x = x
        self.y = y

    def increase(self, byValue = 1):
        if not self.flashing:
            self.value += 1
        if self.value > 9 and not self.flashing:
            self.flashing = True
            self.flashCounter += 1
            for adj in getAdjacents(self):
                adj.increase(1)

    def resetFlash(self):
        if self.flashing:
            self.flashing = False
            self.value = 0

positions = []
for idx, line in enumerate(input):
    positions.append([Point(int(value), idx, i) for i, value in enumerate(line)])

def isValidPoint(x, y):
    if x < 0 or x > len(positions[0]) - 1:
        return False
    if y < 0 or y > len(positions) - 1:
        return False
    return True

def getAdjacents(point):
    a = []
    x = point.x
    y = point.y
    if isValidPoint(x - 1, y):
        a.append(positions[x - 1][y])

    if isValidPoint(x, y - 1):
        a.append(positions[x][y - 1])

    if isValidPoint(x + 1, y):
        a.append(positions[x + 1][y])

    if isValidPoint(x, y + 1):
        a.append(positions[x][y + 1])

    if isValidPoint(x - 1, y - 1):
        a.append(positions[x - 1][y - 1])

    if isValidPoint(x - 1, y + 1):
        a.append(positions[x - 1][y + 1])

    if isValidPoint(x + 1, y - 1):
        a.append(positions[x + 1][y - 1])

    if isValidPoint(x + 1, y + 1):
        a.append(positions[x + 1][y + 1])
    return a

flashCounter = 0
allFlashingAt = 0
for i in range(1000):
    print()
    for line in positions:
        for point in line:
            point.increase(1)

    for line in positions:
        print()
        for point in line:
            point.resetFlash()
            print(str(point.value) + " ", end='')

    if i == 99:
        for line in positions:
            for point in line:
                flashCounter += point.flashCounter

    allFlashing = True
    for line in positions:
        for point in line:
            if point.value != 0:
                allFlashing = False

    if allFlashing and allFlashingAt == 0:
        allFlashingAt = i + 1

print("2021 Day 11, Part 1: " + str(flashCounter))
print("2021 Day 11, Part 2: " + str(allFlashingAt))
