#Parse input
input = [line.strip() for line in open("../Inputs/day10", "r")]

opening = ["<", "{", "(", "["]
closing = [">", "}", ")", "]"]
pairs = ["<>", "{}", "()", "[]"]
points = {
    ")" : 3,
    "]" : 57,
    "}" : 1197,
    ">" : 25137
}
pointsp2 = {
    ")" : 1,
    "]" : 2,
    "}" : 3,
    ">" : 4
}
counterBrackets = {
    ")" : "(",
    "]" : "[",
    "}" : "}",
    ">" : "<",
    "(" : ")",
    "[" : "]",
    "{" : "}",
    "<" : ">"
}

def getCounterPuzzles(puzzles):
    p2CounterPuzzles = []
    for puzzle in puzzles:
        counterPuzzle = ""
        for bracket in puzzle:
            counterPuzzle = counterBrackets[bracket] + counterPuzzle
        p2CounterPuzzles.append(counterPuzzle)
    return p2CounterPuzzles

def getScoreBoard(puzzles):
    scoreBoard = []
    for puzzle in puzzles:
        scorep2 = 0
        for bracket in puzzle:
            scorep2 = (scorep2 * 5) + pointsp2[bracket]
        scoreBoard.append(scorep2)
    scoreBoard.sort()
    return scoreBoard

strippedPuzzles = []
for puzzle in input:
    strippedPuzzle = puzzle
    for i in range(len(puzzle)):
        for pair in pairs:
            strippedPuzzle = strippedPuzzle.replace(pair, "")
    strippedPuzzles.append(strippedPuzzle)

scorep1 = 0
p2ValidPuzzles = strippedPuzzles.copy()
for solvedPuzzle in strippedPuzzles:
    for idx, char in enumerate(solvedPuzzle):
        if char in closing:
            scorep1 += points[char]
            p2ValidPuzzles.remove(solvedPuzzle)
            break

print("2021 Day 10, Part 1: " + str(scorep1))

p2CounterPuzzles = getCounterPuzzles(p2ValidPuzzles)
scoreBoard = getScoreBoard(p2CounterPuzzles)

print("2021 Day 10, Part 2: " + str(scoreBoard[round((len(scoreBoard) - 1) / 2)]))
