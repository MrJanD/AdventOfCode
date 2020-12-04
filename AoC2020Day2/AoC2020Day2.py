input = open("../Inputs/day2", "r").readlines()

class PasswordSet:
    def __init__(self, minOccurance, maxOccurance, letter, password):
        self.firstDigit = minOccurance
        self.secondDigit = maxOccurance
        self.letter = letter
        self.password = password
        self.letterCount = password.count(letter)
        self.Policy1 = (self.firstDigit <= self.letterCount) and (self.secondDigit >= self.letterCount)
        self.Policy2 = (self.password[self.firstDigit - 1] == letter) ^ (self.password[self.secondDigit - 1] == letter)

def inputToStruct():
    set = []
    for line in input:
        splittedLine = line.split()
        firstTwo = splittedLine[0].split("-")
        set.append(PasswordSet(int(firstTwo[0]), int(firstTwo[1]), splittedLine[1].replace(':', ''), splittedLine[2]))
    return set

def validEntries():
    entries = inputToStruct()
    return [entry.Policy1 for entry in entries].count(True), [entry.Policy2 for entry in entries].count(True)

print("Day 2, Part 1: " + str(validEntries()[0]))
print("Day 2, Part 2: " + str(validEntries()[1]))
