import sys
import numpy as np

class Point():
    def __init__(self, p, value, size):
        self.Coords = p
        self.Value = value
        self.Visited = False
        self.ShortestDistance = 500 * 500 * 9 #
        self.PreviousPoint = (0, 0)
        self.MatrixSize = size

    def refreshPoint(self, preDst, preP):
        if (preDst + self.Value) < self.ShortestDistance:
            self.ShortestDistance = preDst + self.Value
            self.PreviousPoint = preP

    def getAdjacents(self):
        adj = []
        if self.MatrixSize > self.Coords[0] + 1:
            adj.append((self.Coords[0] + 1, self.Coords[1]))
        if self.Coords[0] - 1 >= 0:
            adj.append((self.Coords[0] - 1, self.Coords[1]))
        if self.MatrixSize > self.Coords[1] + 1:
            adj.append((self.Coords[0], self.Coords[1] + 1))
        if self.Coords[1] - 1 >= 0:
            adj.append((self.Coords[0], self.Coords[1] - 1))
        return adj

    def updateAdjacents(self, mtrx):
        for adj in self.getAdjacents():
            mtrx[adj[0]][adj[1]].refreshPoint(self.ShortestDistance, self.Coords)
        self.Visited = True

#Parse input
input = [line.strip() for line in open("../Inputs/day15", "r")]
matrix = []
for idy, line in enumerate(input):
    matrix.append([Point((idy, idx), int(n), 100) for idx, n in enumerate(line)])

# Dijkstra without remembering which node already visited
def dijkstra(depth, mat):
    for d in range(depth + 1):
        mat[d][depth].updateAdjacents(mat)
        mat[depth][d].updateAdjacents(mat)
        mat[d][d].updateAdjacents(mat)

matrix[0][0].ShortestDistance = 0
for i in range(100): #
    dijkstra(i, matrix)
print("2021 Day 15, Part 1: " + str(matrix[99][99].ShortestDistance)) #

resultMatrix2 = [[(500 * 500 * 10) for _ in range(500)] for _ in range(500)]

matrix2 = []
for x in range(len(matrix) * 5):
    addX = x//100 #
    xLine = []
    for y in range(len(matrix) * 5):
        addY = y//100 #
        value = matrix[x % 100][y % 100].Value + addX + addY #
        if value > 9:
            value -= 9
        xLine.append(Point((x, y), value, 500))
    matrix2.append(xLine)

matrix2[0][0].ShortestDistance = 0
shortestDst = 500 * 500 * 9
while True:
    for i in range(500): #
        dijkstra(i, matrix2)
    if shortestDst == matrix2[499][499].ShortestDistance:
        break
    shortestDst = matrix2[499][499].ShortestDistance

print("2021 Day 15, Part 2: " + str(shortestDst))
