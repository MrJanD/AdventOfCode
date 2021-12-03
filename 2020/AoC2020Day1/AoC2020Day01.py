input = [int(i) for i in open("../Inputs/day01", "r").readlines()]

def find2():
    for firstIndex in range(len(input)):
        for secondIndex in range(len(input)):
            if input[firstIndex] != input[secondIndex]:
                if input[firstIndex] + input[secondIndex] == 2020:
                    return input[firstIndex] * input[secondIndex]
    return -1

def find3():
    for firstIndex in range(len(input)):
        for secondIndex in range(len(input)):
            for thirdIndex in range(len(input)):
                if (input[firstIndex] != input[secondIndex]) & (input[firstIndex] != input[thirdIndex]) & (input[secondIndex] != input[thirdIndex]):
                    if input[firstIndex] + input[secondIndex] + input[thirdIndex] == 2020:
                        return input[firstIndex] * input[secondIndex] * input[thirdIndex]
    return -1

print("Day 1, Part 1: " + str(find2()))

print("Day 1, Part 2: " + str(find3()))