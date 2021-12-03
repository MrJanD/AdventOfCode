import re

input = [line.strip() for line in open("../Inputs/day4", "r")]

class PassportSet:
    def __init__(self, byr = -1, iyr = -1, eyr = -1, hgt = -1, hcl = -1, ecl = -1, pid = -1, cid = -1):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid
        self.cid = cid

    def datasetComplete(self):
        return (self.byr != -1) and (self.iyr != -1) and (self.eyr != -1) and (self.hgt != -1) and (self.hcl != -1) and (self.ecl != -1) and (self.pid != -1)

    def byrValid(self):
        if re.match('^[1][9][2-9][0-9]|200[0-2]$', str(self.byr)):
            return True
        return False

    def iyrValid(self):
        if re.match('^20[1][0-9]|2020$', str(self.iyr)):
            return True
        return False

    def eyrValid(self):
        if re.match('^20[2][0-9]|2030$', str(self.eyr)):
            return True
        return False

    def hgtValid(self):
        if re.match('^[1][5-8][0-9]cm|[1][9][0-3]cm|[5][9]in|[6][0-9]in|[7][0-6]in$', str(self.hgt)):
            return True
        return False

    def hclValid(self):
        if re.match('^#[0-9a-f]+$', str(self.hcl)):
            return True
        return False

    def eclValid(self):
        if re.match('^(amb|blu|brn|gry|grn|hzl|oth)$', str(self.ecl)):
            return True
        return False

    def pidValid(self):
        if re.match('^[0-9]{9}$', str(self.pid)):
            return True
        return False

    def datasetValid(self):
        return self.byrValid() and self.iyrValid() and self.eyrValid() and self.hgtValid() and self.hclValid() and self.eclValid() and self.pidValid()

def inputToStruct():
    lineIndex = 0
    fileLines = len(input)
    strippedPWS = []
    pws = PassportSet()
    while lineIndex < fileLines:
        if input[lineIndex] == '':
            strippedPWS.append(pws)
            pws = PassportSet()
            lineIndex += 1
        else:
            for partialSet in input[lineIndex].split(" "):
                keyValue = partialSet.split(":")
                if keyValue[0] == "byr":
                    pws.byr = keyValue[1]
                elif keyValue[0] == "iyr":
                    pws.iyr = keyValue[1]
                elif keyValue[0] == "eyr":
                    pws.eyr = keyValue[1]
                elif keyValue[0] == "hgt":
                    pws.hgt = keyValue[1]
                elif keyValue[0] == "hcl":
                    pws.hcl = keyValue[1]
                elif keyValue[0] == "ecl":
                    pws.ecl = keyValue[1]
                elif keyValue[0] == "pid":
                    pws.pid = keyValue[1]
                elif keyValue[0] == "cid":
                    pws.cid = keyValue[1]
            if lineIndex == (fileLines - 1):
                strippedPWS.append(pws)
            lineIndex += 1
    return strippedPWS

def datasetComplete():
    entries = inputToStruct()
    return [entry.datasetComplete() for entry in entries].count(True)

def datasetValid():
    entries = inputToStruct()
    return [entry.datasetValid() for entry in entries].count(True)

print("Day 4, Part 1: " + str(datasetComplete()))
print("Day 4, Part 2: " + str(datasetValid()))