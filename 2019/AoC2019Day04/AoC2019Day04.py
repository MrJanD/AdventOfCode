minValue = 248345
maxValue = 746315

def splitInput(value):
    return [int(x) for x in str(value)]

def sameAdjacentDigits(value):
    previousDigit = -1
    for digit in splitInput(value):
        if digit == previousDigit:
            return True
        previousDigit = digit
    return False

def getAllIndexesWithChangingDigit(value):
    digitList = splitInput(value)
    previousDigit = -1
    digitIndex = 0
    positionListOfChangingDigits = []
    while digitIndex < len(digitList):
        if digitList[digitIndex] != previousDigit:
            positionListOfChangingDigits.append(digitIndex)
        previousDigit = digitList[digitIndex]
        digitIndex += 1
    positionListOfChangingDigits.append(6)
    return positionListOfChangingDigits

def hasExactlyTwoDescandingValues(value):
    positionListOfChangingDigits = getAllIndexesWithChangingDigit(value)
    changingDigitIndex = 1
    lastChangeOfDigitAtIndex = 0
    while changingDigitIndex < len(positionListOfChangingDigits):
        if positionListOfChangingDigits[changingDigitIndex] - lastChangeOfDigitAtIndex == 2:
            return True
        lastChangeOfDigitAtIndex = positionListOfChangingDigits[changingDigitIndex]
        changingDigitIndex += 1
    return False

def noneDecreasingDigits(value):
    previousDigit = -1
    for digit in splitInput(value):
        if digit < previousDigit:
            return False
        previousDigit = digit
    return True

def valueIsValid(value):
    if sameAdjacentDigits(value) and noneDecreasingDigits(value):
        return True
    return False

def countValidValues(lowestValidValue, highestValidValue):
    validValuesP1 = 0
    validValuesP2 = 0
    currentValue = lowestValidValue
    while currentValue <= highestValidValue:
        if valueIsValid(currentValue):
            validValuesP1 += 1
            if hasExactlyTwoDescandingValues(currentValue):
                validValuesP2 += 1
        currentValue += 1
    return [validValuesP1, validValuesP2]

validValues = countValidValues(minValue, maxValue)
print("Part1 valid values between " + str(minValue) + "-" + str(maxValue) + ": " + str(validValues[0]))
print("Part2 valid values between " + str(minValue) + "-" + str(maxValue) + ": " + str(validValues[1]))

