input = [line.strip() for line in open("../Inputs/day6", "r")]

class Passenger:
    def __init__(self, questions):
        self.questions = questions

    def hasDuplicates(self):
        for letter in self.questions:
            if self.questions.count(letter) > 1:
                return True
        return False

def inputToStruct():
    groups = []
    group = []
    for passenger in input:
        if passenger == '':
            groups.append(group)
            group = []
        else:
            group.append(passenger)
    return groups

def countYesForGroup(group):
    allQuestions = ""
    for passenger in group:
        allQuestions = allQuestions + passenger

    yesSet = set([answer for answer in allQuestions if allQuestions.count(answer) > 0])
    yesAnswers = len(yesSet)
    return len(set([answer for answer in allQuestions if allQuestions.count(answer) > 0]))

def countCommonYesForGroup(group):
    allQuestions = ""
    for passenger in group:
        allQuestions = allQuestions + passenger

    yesSet = set([answer for answer in allQuestions if allQuestions.count(answer) == len(group)])
    return len(yesSet)

def sumQuestions():
    sum = 0
    parsedInput = inputToStruct()
    for group in parsedInput:
        sum = sum + countYesForGroup(group)
    return sum

def sumCommonAnswers():
    sum = 0
    parsedInput = inputToStruct()
    for group in parsedInput:
        sum = sum + countCommonYesForGroup(group)
    return sum

print("Day 6, Part 1: " + str(sumQuestions()))
print("Day 6, Part 2: " + str(sumCommonAnswers()))