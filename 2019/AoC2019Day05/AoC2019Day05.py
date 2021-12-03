with open("AdventOfCode05/input", "r") as f:
    initialInputValues = [ int(x) for x in f.read().split(",") ]

indexOffset = 0
outputStream = []
inputValue = 5

def getSolvedOpcode(initialInputValues):
    inputValues = initialInputValues.copy()
    index = 0
    elements = len(inputValues)

    while index < elements and inputValues[index] != 99:
        inputValues, index = operatorInterpreter(inputValues, index)
        index += indexOffset

    return inputValues

def operatorInterpreter(inputValues, operatorIndex):
    global indexOffset
    A, B, C, operator = getParameterModes(inputValues[operatorIndex])

    if C == 0:
        parameter1 = inputValues[inputValues[operatorIndex + 1]]
    else:
        parameter1 = inputValues[operatorIndex + 1]

    # Operators 3 and 4 only support one parameter.
    if operator < 3 or operator > 4:
        if B == 0:
            parameter2 = inputValues[inputValues[operatorIndex + 2]]
        else:
            parameter2 = inputValues[operatorIndex + 2]

        if operator < 3 or operator > 6:
            if A == 0:
                parameter3 = inputValues[operatorIndex + 3]
            else:
                parameter3 = inputValues[operatorIndex + 3]

    # 1: Addition
    if operator == 1:
        inputValues[parameter3] = parameter1 + parameter2
        indexOffset = 4

    # 2: Multiplication
    if operator == 2:
        inputValues[parameter3] = parameter1 * parameter2
        indexOffset = 4

    # 3: Write
    if operator == 3:
        inputValues[inputValues[operatorIndex + 1]] = inputValue
        indexOffset = 2

    # 4: Print
    if operator == 4:
        outputStream.append(parameter1)
        indexOffset = 2

    # 5: Jump-If-True
    if operator == 5:
        if parameter1 != 0:
           operatorIndex = parameter2
           indexOffset = 0
        else:
            indexOffset = 3

    # 6: Jump-If-False
    if operator == 6:
        if parameter1 == 0:
           operatorIndex = parameter2
           indexOffset = 0
        else:
            indexOffset = 3

    # 7: Less Than
    if operator == 7:
        if parameter1 < parameter2:
            inputValues[parameter3] = 1
        else:
            inputValues[parameter3] = 0
        indexOffset = 4

    # 8: Equals
    if operator == 8:
        if parameter1 == parameter2:
            inputValues[parameter3] = 1
        else:
            inputValues[parameter3] = 0
        indexOffset = 4

    return inputValues, operatorIndex

def getParameterModes(operator):
    ABC, DE = divmod(operator, 100)
    AB, C = divmod(ABC, 10)
    A, B = divmod(AB, 10)
    return A, B, C, DE

getSolvedOpcode(initialInputValues)
print("Outputs: " + str(outputStream))
