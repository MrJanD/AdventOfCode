from collections import Counter
from collections import defaultdict

#Parse input
input = [line.strip() for line in open("../Inputs/day14.ex", "r")]

polymer = ""
pairInsertionTuples = {}

for line in input:
    if line == "":
        continue
    if " -> " not in line:
        polymer = line
    if " -> " in line:
        pair, insertion = line.split(" -> ")
        pairInsertionTuples[pair] = insertion

def iteration(polymer, pairInsertionTuples):
    retPolymer = ""
    for idx in range(len(polymer) - 1):
        retPolymer = retPolymer + polymer[idx] + pairInsertionTuples[polymer[idx] + polymer[idx + 1]]
    retPolymer += polymer[-1]
    return retPolymer

def countingIteration(pairCountingDict):
    changedDict = defaultdict(lambda: 0)
    for key in pairCountingDict:
        if pairCountingDict[key] > 0:
            s = iteration(key, pairInsertionTuples)
            changedDict[s[0:2]] += pairCountingDict[key]
            changedDict[s[-2:]] += pairCountingDict[key]
    return changedDict

def stringToPairs(s):
    return [''.join(pair) for pair in zip(s[:-1], s[1:])]

poly10 = polymer
for i in range(10):
    poly10 = iteration(poly10, pairInsertionTuples)

statistics = Counter(poly10)
countList10 = statistics.values()
print("2021 Day 14, Part 1: " + str(max(countList10) - min(countList10)))

# Create an empty dict and fill only with the starting polymer in tuples
pairCountingDict = {}
for tup in pairInsertionTuples.keys():
    pairCountingDict[tup] = 0
for pair in stringToPairs(polymer):
    pairCountingDict[pair] += 1

# Get the count of pairs
for i in range(40):
    pairCountingDict = countingIteration(pairCountingDict)

# Split each pair of letters an get the number of letters
letterCountingDict = defaultdict(lambda: 0)
for key in pairCountingDict:
    letterCountingDict[key[0]] += pairCountingDict[key]
    letterCountingDict[key[1]] += pairCountingDict[key]

# Each letter in letter pairs have to be divided by 2.
letterCountingDict[polymer[0]] += 1
letterCountingDict[polymer[-1]] += 1
for key in letterCountingDict:
    letterCountingDict[key] = int(letterCountingDict[key] / 2)

print("2021 Day 14, Part 2: " + str(max(letterCountingDict.values()) - min(letterCountingDict.values())))
