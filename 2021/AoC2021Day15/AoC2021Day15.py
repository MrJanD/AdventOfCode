import sys
import numpy as np

class Point():
    def __init__(self, p, value):
        self.Coords = p
        self.Value = value
        self.Visited = False
        self.ShortestDistance = 50 * 50 * 9 #
        self.PreviousPoint = (0, 0)
        self.MatrixSize = (10, 10) #

    def refreshPoint(self, preDst, preP):
        if (preDst + self.Value) < self.ShortestDistance:
            self.ShortestDistance = preDst + self.Value
            self.PreviousPoint = preP

    def getAdjacents(self):
        adj = []
        if self.MatrixSize[0] > self.Coords[0] + 1:
            adj.append((self.Coords[0] + 1, self.Coords[1]))
        if self.Coords[0] - 1 >= 0:
            adj.append((self.Coords[0] - 1, self.Coords[1]))
        if self.MatrixSize[1] > self.Coords[1] + 1:
            adj.append((self.Coords[0], self.Coords[1] + 1))
        if self.Coords[1] - 1 >= 0:
            adj.append((self.Coords[0], self.Coords[1] - 1))
        return adj

    def updateAdjacents(self, mtrx):
        for adj in self.getAdjacents():
            mtrx[adj[0]][adj[1]].refreshPoint(self.ShortestDistance, self.Coords)
        self.Visited = True

    def print(self):
        print("Coords: " + str(self.Coords[0]) + ", " + str(self.Coords[1]))
        print("Value: " + str(self.Value))
        print("ShortestDistance: " + str(self.ShortestDistance))
        print("PreviousPoint: " + str(self.PreviousPoint[0]) + ", " + str(self.PreviousPoint[1]))
        print("MatrixSize: " + str(self.MatrixSize[0]) + ", " + str(self.MatrixSize[1]))

#Parse input
input = [line.strip() for line in open("../Inputs/day15.ex", "r")]
matrix = []
for idy, line in enumerate(input):
    matrix.append([Point((idy, idx), int(n)) for idx, n in enumerate(line)])

matrixList = []
for line in input:
    matrixList.append([int(n) for n in line])

def dijkstra(depth, mat):
    for d in range(depth + 1):
        mat[d][depth].updateAdjacents(mat)
        mat[depth][d].updateAdjacents(mat)
        mat[d][d].updateAdjacents(mat)

matrixSmall2 = matrix.copy()

matrix[0][0].ShortestDistance = 0
for i in range(10): #
    dijkstra(i, matrix)
print("2021 Day 15, Part 1: " + str(matrix[9][9].ShortestDistance)) #

#matrixList2 = []
#for x in range(len(matrixList2) * 5):
#    addX = x//100
#    xLine = []
#    for y in range(len(matrixList2) * 5):
#        addY = y//100
#        value = matrixList2[x % 100][y % 100] + addX + addY
#        if value > 9:
#            value -= 9
#        print("WRONG VALUE IN: " + str(x) + ", " + str(y))
#        xLine.append(value)
#    matrixList2.append(xLine)

#resultMatrix2 = [[(500 * 500 * 10) for _ in range(500)] for _ in range(500)]

#l = [[0, 0], [0, 0]]
#m = l.copy()

matrix2 = []
for x in range(len(matrixSmall2) * 5):
    addX = x//10 #
    xLine = []
    for y in range(len(matrixSmall2) * 5):
        addY = y//10 #
        value = matrixSmall2[x % 10][y % 10].Value + addX + addY #
        p = Point((x, y), value)
        p.MatrixSize = (50, 50) #
        xLine.append(p)
    matrix2.append(xLine)

for x in range(len(matrix2)):
    for y in range(len(matrix2[0])):
        if matrix2[x][y].Value > 9:
            matrix2[x][y].Value -= 9
        if matrix2[x][y].Value < 1 or matrix2[x][y].Value > 9:
            print("WRONG VALUE IN: ")
            matrix2[x][y].print()

matrix2[0][0].ShortestDistance = 0
for i in range(50): #
    dijkstra(i, matrix2)


print("2021 Day 15, Part 2: ")
#matrix2[499][499].print()
#print("498, 499: ")
#matrix2[498][499].print()
#print("499, 498: ")
#matrix2[499][498].print()