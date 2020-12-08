input = [line.strip() for line in open("Inputs/day8", "r")]

class Instruction:
        def __init__(self, line):
            self.operation = line.split()[0]
            self.value = int(line.split()[1])
            self.executed = False
            self.toggle = False

        def proceedOperation(self, accumulator, operationIndex):
            if self.operation == "acc":
                operationIndex += 1
                accumulator += int(self.value)
            elif self.operation == "jmp" or (self.operation == "nop" and self.toggle):
                operationIndex += int(self.value)
            elif self.operation == "nop" or (self.operation == "jmp" and self.toggle):
                operationIndex += 1
            self.executed = True
            return accumulator, operationIndex

        def reset(self):
            self.executed = False
            self.toggle = False

instructions = []
for line in input:
    instructions.append(Instruction(line))

def runCode():
    accumulator = 0
    index = 0

    while index < len(instructions):
        if not instructions[index].executed:
            accumulator, index = instructions[index].proceedOperation(accumulator, index)
        else:
            break

    return accumulator, index

print("Day 8, Part 1: " + str(runCode()[0]))

def resetInstructions():
    for instruction in instructions:
        instruction.reset()

resetInstructions()
indexToToggle = 0
inLen = len(input)
while indexToToggle < len(input):
    if "acc"in input[indexToToggle]:
        indexToToggle += 1
        continue
    instructions[indexToToggle].toggle = True
    accumulator, index = runCode()
    if index >= len(input):
        print("Day 8, Part 2: " + str(accumulator))
        break
    resetInstructions()
    indexToToggle += 1
