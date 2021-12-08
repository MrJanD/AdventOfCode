from itertools import permutations

input = [line.strip() for line in open("../Inputs/day08", "r")]

sumP1 = 0
t_sum = 0
teachInList = []
patternList = []

for line in input:
    teachInList.append(line.split(' | ')[0])
    patternList.append(line.split(' | ')[1])

for pattern in patternList:
    for x in pattern.split(" "):
        if len(x) in [2,3,4,7]:
            sumP1 += 1

for x in range(len(teachInList)):
    sums = ""
    pattern = patternList[x].split(" ")
    teachIn = teachInList[x].split(" ")
    valid = ['abcefg','cf','acdeg','acdfg','bcdf','abdfg','abdefg','acf','abcdefg','abcdfg']
    assignments = {'a':'','b':'','c':'','d':'','e':'','f':'','g':''}
    ps = permutations([*assignments.keys()])
    for p in ps:
        p = iter(p)
        for chr in assignments.keys():
            assignments[chr] = next(p)
        ok = True
        for num in teachIn:
            build = ""
            for chr in num:
                build += assignments[chr]
            if "".join(sorted(build)) not in valid:
                ok = False
                break
        if ok:
            for num in pattern:
                build = ""
                for chr in num:
                    build += assignments[chr]
                sums += str(valid.index("".join(sorted(build))))
            t_sum += int(sums)

print("2021 Day 8, Part 1: " + str(sumP1))
print("2021 Day 8, Part 2: " + str(t_sum))