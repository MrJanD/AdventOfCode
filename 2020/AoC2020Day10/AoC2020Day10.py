import itertools

input = [int(line.strip()) for line in open("../Inputs/day10", "r")]
input.append(0)
input.sort()
input.append(input[-1] + 3)

counter = {1 : 0, 2 : 0, 3 : 0}
for joltageIndex in range(len(input) - 1):
    counter[input[joltageIndex + 1] - input[joltageIndex]] += 1

print("Day 10, Part 1: " + str(counter[1] * counter[3]))

# Find out every distance
def sliceInput():
    slicedInput = []
    index = 0
    while index < len(input) - 1:
        previousSliceStartIndex = index
        while input[index] + 3 != input[index + 1]:
            index += 1
        index += 1
        slicedInput.append((previousSliceStartIndex, index))
    return slicedInput

def isValidSlice(list):
    for numberIndex in range(len(list) - 1):
        if list[numberIndex + 1] <= list[numberIndex] or list[numberIndex + 1] > list[numberIndex] + 3:
            return False
    return True

def validSlices(startingIndex, endingIndex):
    lst = input[startingIndex:endingIndex]
    validSlices = 1
    for L in range(2, len(lst)):
        for subset in itertools.combinations(lst, L):
            if subset[0] == lst[0] and subset[-1] == lst[-1]:
                if isValidSlice(list(subset)):
                    validSlices += 1
    return validSlices

lst = sliceInput()
currentValidSlices = 1
for slice in lst:
    valid = validSlices(slice[0], slice[1])
    currentValidSlices = currentValidSlices * valid

print("Day 10, Part 2: " + str(currentValidSlices))

