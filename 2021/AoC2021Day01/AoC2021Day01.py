input = [int(line.strip()) for line in open("../Inputs/day01", "r")]

def findIncreasingP1():
    increasingCounter = 0
    for index, value in enumerate(input):
        if index > 0 and value > input[index - 1]:
            increasingCounter += 1
    return increasingCounter

def findIncreasingWindowsP2():
    increasingCounter = 0
    for index, value in enumerate(input):
        if getThreeSum(index) > getThreeSum(index - 1):
            increasingCounter += 1
    return increasingCounter

def getThreeSum(index):
    sum = 0
    if index < (len(input) - 2):
        sum = input[index] + input[index + 1] + input[index + 2]
    return sum

print("2021 Day 1, Part 1: " + str(findIncreasingP1()))
print("2021 Day 1, Part 2: " + str(findIncreasingWindowsP2()))