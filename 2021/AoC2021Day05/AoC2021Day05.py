import math

input = [line.strip() for line in open("../Inputs/day05", "r")]
input = list(filter(('').__ne__, input))

class Point:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def tuple(self):
        return [self.X, self.Y]

class Venture:
    def __init__(self, sourceTuple, destTuple):
        self.Source = Point(int(sourceTuple[0]), int(sourceTuple[1]))
        self.Dest = Point(int(destTuple[0]), int(destTuple[1]))

    def getOneDirectionalLine(self):
        if (self.Source.X == self.Dest.X or self.Source.Y == self.Dest.Y):
            tupleLine = []
            if self.Source.X > self.Dest.X:
                for i in range(self.Source.X, self.Dest.X - 1, -1):
                    tupleLine.append(Point(i, self.Dest.Y))

            elif self.Source.X < self.Dest.X:
                for i in range(self.Source.X, self.Dest.X + 1, 1):
                    tupleLine.append(Point(i, self.Dest.Y))

            elif self.Source.Y > self.Dest.Y:
                for i in range(self.Source.Y, self.Dest.Y - 1, -1):
                    tupleLine.append(Point(self.Dest.X, i))

            elif self.Source.Y < self.Dest.Y:
                for i in range(self.Source.Y, self.Dest.Y + 1, 1):
                    tupleLine.append(Point(self.Dest.X, i))

            return tupleLine

        return None

    def getTwoDirectionalLine(self):
            if (abs(self.Source.X - self.Dest.X) == abs(self.Source.Y - self.Dest.Y)):
                xIncrement = []
                yIncrement = []
                tupleLine = []
                if self.Source.X > self.Dest.X:
                    for x in range(self.Source.X, self.Dest.X - 1, -1):
                        xIncrement.append(x)
                elif self.Source.X < self.Dest.X:
                    for x in range(self.Source.X, self.Dest.X + 1, 1):
                        xIncrement.append(x)

                if self.Source.Y > self.Dest.Y:
                    for y in range(self.Source.Y, self.Dest.Y - 1, -1):
                        yIncrement.append(y)
                elif self.Source.Y < self.Dest.Y:
                    for y in range(self.Source.Y, self.Dest.Y + 1, 1):
                        yIncrement.append(y)

                for index, elem in enumerate(xIncrement):
                    tupleLine.append(Point(xIncrement[index], yIncrement[index]))

                return tupleLine

            return None

Matrix = [[0 for x in range(1000)] for y in range(1000)]

for line in input:
    sD = line.split(' -> ')
    vent = Venture(sD[0].split(','), sD[1].split(','))
    if vent.getOneDirectionalLine():
        for p in vent.getOneDirectionalLine():
            Matrix[p.X][p.Y] += 1

count = 0
for line in Matrix:
    for point in line:
        if point > 1:
            count += 1

print("2021 Day 5, Part 1: " + str(count))

for line in input:
    sD = line.split(' -> ')
    vent = Venture(sD[0].split(','), sD[1].split(','))
    if vent.getTwoDirectionalLine():
        for p in vent.getTwoDirectionalLine():
            Matrix[p.X][p.Y] += 1

count = 0
for line in Matrix:
    for point in line:
        if point > 1:
            count += 1

print("2021 Day 5, Part 2: " + str(count))
