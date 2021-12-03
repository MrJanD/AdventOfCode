input = [line.strip() for line in open("../Inputs/day3", "r")]

def countTrees(right, down):
    trees = 0
    index = right
    line = down

    while line < len(input):
        lineLen = len(input[line])
        character = input[line][index % lineLen]
        if character == '#':
            trees = trees + 1
        index = index + right
        line = line + down
    return trees

print("Day 3, Part 1: " + str(countTrees(3, 1)))
print("Day 3, Part 2: " + str(countTrees(1, 1) * countTrees(3, 1) * countTrees(5, 1) * countTrees(7, 1) * countTrees(1, 2)))