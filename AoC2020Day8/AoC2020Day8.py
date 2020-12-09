import copy

input = [line.strip() for line in open("../Inputs/day8", "r")]

class Instruction:
        def __init__(self, line):
            self.operation = line.split()[0]
            self.value = int(line.split()[1])
            self.executed = False

        def proceedOperation(self, accumulator, operationIndex):
            if self.operation == "acc":
                operationIndex += 1
                accumulator += int(self.value)
            elif self.operation == "jmp":
                operationIndex += int(self.value)
            elif self.operation == "nop":
                operationIndex += 1
            self.executed = True
            return accumulator, operationIndex

        def reset(self):
            self.executed = False

instructions = []
for line in input:
    instructions.append(Instruction(line))

def runCode(instructionSet):
    accumulator = 0
    index = 0

    while index < len(instructionSet):
        if not instructionSet[index].executed:
            accumulator, index = instructionSet[index].proceedOperation(accumulator, index)
        else:
            break

    return accumulator, index

print("Day 8, Part 1: " + str(runCode(instructions)[0]))

def resetInstructions():
    for instruction in instructions:
        instruction.reset()

def getToggledInstructions(indexToToggle):
    toggledInstructions = copy.deepcopy(instructions)
    if "jmp" in toggledInstructions[indexToToggle].operation:
        toggledInstructions[indexToToggle].operation = "nop"
    elif "nop" in toggledInstructions[indexToToggle].operation:
        toggledInstructions[indexToToggle].operation = "jmp"
    return toggledInstructions

for indexToToggle in range(len(input)):
    resetInstructions()
    if "acc"in input[indexToToggle]:
        indexToToggle += 1
        continue
    toggledInstructions = getToggledInstructions(indexToToggle)
    accumulator, index = runCode(toggledInstructions)
    if index >= len(input):
        print("Day 8, Part 2: " + str(accumulator))
        break

    indexToToggle += 1
