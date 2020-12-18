input = [line.strip() for line in open("../Inputs/day14", "r")]

memory = {}
currentMask = None
currentValue = None
currentAddress = None

for line in input:
    k, v = line.split(" = ")
    if k == "mask":
        currentMask = v
    else:
        currentAddress = int(k[4:-1])
        currentValue = int(v)

        valueInBin = list(bin(currentValue)[2:].zfill(36))
        result = [0] * 36

        for i, (mask, value) in enumerate(zip(currentMask, valueInBin)):
            if mask == "X":
                result[i] = value
            else:
                result[i] = mask

        memory[currentAddress] = int("".join(result), 2)

print("Day 14, Part 1: " + str(sum(memory.values())))

# TODO: Part2
