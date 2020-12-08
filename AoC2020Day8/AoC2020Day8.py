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

instructions = []
for line in input:
    instructions.append(Instruction(line))

accumulator = 0
index = 0

while index < len(instructions):
    if not instructions[index].executed:
        accumulator, index = instructions[index].proceedOperation(accumulator, index)
    else:
        break

print("Day 8, Part 1: " + str(accumulator))
