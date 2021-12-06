import math

input = [line.strip() for line in open("../Inputs/day06", "r")]

swarm = []
for fish in input[0].split(','):
    swarm.append(int(fish))

def dayCycle(swarm):
    for index, fish in enumerate(swarm):
        swarm[index] = fish - 1
        if swarm[index] == -1:
            swarm[index] = 6
            swarm.append(9)

for day in range(80):
    dayCycle(swarm)

print("2021 Day 6, Part 1: " + str(len(swarm)))

swarmAgeDistribution = []
for i in range(9):
    swarmAgeDistribution.append(0)

for fish in input[0].split(','):
    swarmAgeDistribution[int(fish)] += 1

for day in range(256):
    reproductiveFishCount = swarmAgeDistribution[0]

    for ageCounter in range(1,9):
        swarmAgeDistribution[ageCounter - 1] = swarmAgeDistribution[ageCounter]

    swarmAgeDistribution[8] = reproductiveFishCount
    swarmAgeDistribution[6] += reproductiveFishCount

sum = 0
for fishCount in swarmAgeDistribution:
    sum += fishCount

print("2021 Day 6, Part 2: " + str(sum))
