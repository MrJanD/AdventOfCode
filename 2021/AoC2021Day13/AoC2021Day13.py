input = [line.strip() for line in open("../Inputs/day13", "r")]

matrix = set()
foldList = []
for line in input:
    if "," in line:
        x, y = line.split(",")
        matrix.add((int(x),int(y)))
    if "fold along y" in line:
        foldList.append(("y", int(line.split("=")[1])))
    if "fold along x" in line:
        foldList.append(("x", int(line.split("=")[1])))

def getFoldedY(foldLine, xy):
    tup = xy
    if tup[1] > foldLine:
        return (tup[0], 2 * foldLine - tup[1])
    return tup

def getFoldedX(foldLine, xy):
    tup = xy
    if tup[0] > foldLine:
        return(2 * foldLine - tup[0], tup[1])
    return tup

def foldMatrix(foldList, matrix):
    for foldOperation in foldList:
        foldedMatrix = set()
        for (x, y) in matrix:
            if foldOperation[0] == "y":
                (x, y) = getFoldedY(foldOperation[1], (x, y))
            elif foldOperation[0] == "x":
                (x, y) = getFoldedX(foldOperation[1], (x, y))
            foldedMatrix.add((x, y))
        matrix = foldedMatrix
    return matrix

matrixSingleFold = foldMatrix([foldList[0]], matrix)
print("2021 Day 11, Part 1: " + str(len(matrixSingleFold)))

print("2021 Day 11, Part 2: ")
matrix = foldMatrix(foldList, matrix)
for y in range(max([v[1] for v in matrix])+1):
    for x in range(max([v[0] for v in matrix])+1):
        print('#' if (x, y) in matrix else '.', end='')
    print()
