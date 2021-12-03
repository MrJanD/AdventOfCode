with open("input", "r") as f:
    initialInputValues = [ int(x) for x in f.read().split(",") ]

def getSolvedOpcode(noun, verb, initialInputValues):
    inputValues = initialInputValues.copy()
    inputValues[1] = noun
    inputValues[2] = verb
    index = 0
    elements = len(inputValues)
    while index < elements - 3 and inputValues[index] != 99:
        inputValues = alignList(inputValues, index)
        index += 4
    return inputValues

def alignList(inputValues, operatorIndex):
    operator = inputValues[operatorIndex]
    value1 = inputValues[inputValues[operatorIndex + 1]]
    value2 = inputValues[inputValues[operatorIndex + 2]]
    storeAt = inputValues[operatorIndex + 3]

    inputValues[storeAt] = operatorInterpreter(operator, value1, value2)
    return inputValues

def operatorInterpreter(operator, value1, value2):
    # 1: Addition
    if operator == 1:
        result = value1 + value2

    # 2: Multiplication
    if operator == 2:
        result = value1 * value2

    return result

def getAnswerPart2(noun, verb):
       return 100 * noun + verb

def getResultPart2():
    noun = 0
    verb = 0
    while noun <= 99:
        while verb <= 99:
            if getSolvedOpcode(noun, verb, initialInputValues)[0] == 19690720:
                return getAnswerPart2(noun, verb)
            verb += 1
        noun += 1
        verb = 0

print("Value at position 0: " + str(getSolvedOpcode(12, 2, initialInputValues)[0]))
print("Answer for part 2: " + str(getResultPart2()))
