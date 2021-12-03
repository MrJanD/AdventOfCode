import copy

input = [list(line.strip()) for line in open("../Inputs/day11", "r")]

def isTaken(seatingPlan, row, column):
    if row >= 0 and row < len(seatingPlan):
        if column >= 0 and column < len(seatingPlan[0]):
            return seatingPlan[row][column] == "#"
    return False

def adjacentSeatsTaken(seatingPlan, row, column):
    seatsTaken = 0
    if isTaken(seatingPlan, row - 1, column - 1):
        seatsTaken += 1
    if isTaken(seatingPlan, row, column - 1):
        seatsTaken += 1
    if isTaken(seatingPlan, row + 1, column - 1):
        seatsTaken += 1
    if isTaken(seatingPlan, row - 1, column):
        seatsTaken += 1
    if isTaken(seatingPlan, row + 1, column):
        seatsTaken += 1
    if isTaken(seatingPlan, row - 1, column + 1):
        seatsTaken += 1
    if isTaken(seatingPlan, row, column + 1):
        seatsTaken += 1
    if isTaken(seatingPlan, row + 1, column + 1):
        seatsTaken += 1
    return seatsTaken

def listsEqual(list1, list2):
    for row in range(len(list1)):
        for column in range(len(list1)):
            if list1[row][column] != list2[row][column]:
                return False
    return True

def countSeats(list):
    count = 0
    for row in range(len(list)):
        for column in range(len(list[0])):
            if list[row][column] == "#":
                count += 1
    return count


floatingSeatingPlan = copy.deepcopy(input)
currentSeatingPlan = copy.deepcopy(input)

while True:
    for row in range(len(input)):
        for column in range(len(input[row])):
            if currentSeatingPlan[row][column] == ".":
                continue
            if adjacentSeatsTaken(currentSeatingPlan, row, column) == 0:
                floatingSeatingPlan[row][column] = "#"
            if adjacentSeatsTaken(currentSeatingPlan, row, column) >= 4:
                floatingSeatingPlan[row][column] = "L"
    if listsEqual(floatingSeatingPlan, currentSeatingPlan):
        break
    currentSeatingPlan = copy.deepcopy(floatingSeatingPlan)

print("Day 11, Part 1: " + str(countSeats(floatingSeatingPlan)))

