from collections import *

input = [14, 1, 17, 0, 3, 20] # Given input
inputp2 = input.copy()

def getLastOccurance(list, number):
    lastOccIndex = len(list)
    for currentListIndex in range(len(list)):
        if list[currentListIndex] == number:
            lastOccIndex = currentListIndex
    return lastOccIndex

while len(input) < 2020:
    input.append(len(input) - 1 - getLastOccurance(input[0:-1], input[-1]))

print("Day 15, Part 1: " + str(input[-1]))

input = inputp2
numberToSpeak = input[-1]

# Reference: https://www.reddit.com/r/adventofcode/comments/kdf85p/2020_day_15_solutions/
turn_num = defaultdict(deque)

for value, key in enumerate(input):
    turn_num[key].append(value + 1)

turn = len(input) + 1
while turn <= 30000000:
    l = len(turn_num[numberToSpeak])
    if l > 1:
        numberToSpeak = turn_num[numberToSpeak][-1] - turn_num[numberToSpeak][-2]
        turn_num[numberToSpeak].append(turn)
    elif l == 1:
        numberToSpeak = 0
        turn_num[numberToSpeak].append(turn)
    else:
        numberToSpeak = 0
        turn_num[numberToSpeak].append(turn)

    turn += 1

print("Day 15, Part 2: " + str(numberToSpeak))
