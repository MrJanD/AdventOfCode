input = [line.strip() for line in open("../Inputs/day06", "r")]

def getSwarmAfterDays(days):
    swarmAgeDistribution = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for fish in input[0].split(','):
        swarmAgeDistribution[int(fish)] += 1

    for day in range(days):
        reproductiveFishCount = swarmAgeDistribution[0]
        for ageCounter in range(1,9):
            swarmAgeDistribution[ageCounter - 1] = swarmAgeDistribution[ageCounter]
        swarmAgeDistribution[8] = reproductiveFishCount
        swarmAgeDistribution[6] += reproductiveFishCount

    return sum(swarmAgeDistribution)

print("2021 Day 6, Part 1: " + str(getSwarmAfterDays(80)))
print("2021 Day 6, Part 2: " + str(getSwarmAfterDays(256)))
