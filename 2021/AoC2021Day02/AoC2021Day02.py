input = [line.strip() for line in open("../Inputs/day02", "r")]

def getCoordinates(function):
    x, y, aim = 0, 0, 0
    for line in input:
        xStep, yStep, aim = function(line.split()[0], (int)(line.split()[1]), aim)
        x += xStep
        y += yStep
    return x, y, aim

def getIncrement(command, distance, aim):
    if command == "forward":
        return (int)(distance), 0, 0
    if command == "up":
        return 0, -(int)(distance), 0
    if command == "down":
        return 0, (int)(distance), 0
    return 0, 0, 0

def getCorrectIncrement(command, value, aim):
    if command == "forward":
        return (int)(value), (aim * (int)(value)), aim
    if command == "up":
        aim -= value
    if command == "down":
        aim += value
    return 0, 0, aim

x, y, aim = getCoordinates(getIncrement)
print("2021 Day 2, Part 1: " + str(x * y))
x, y, aim = getCoordinates(getCorrectIncrement)
print("2021 Day 2, Part 2: " + str(x * y))