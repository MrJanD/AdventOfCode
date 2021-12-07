import statistics

#Parse input
input = [line.strip() for line in open("../Inputs/day07", "r")]
crabPositions = []
for crab in input[0].split(','):
        crabPositions.append(int(crab))

#Return fuel consumption to move to position when increased exponentially
def getFuel(pos):
    fuelRequired = 0
    for crabPosition in crabPositions:
        dstAvg = abs(crabPosition - pos)
        fuelRequired += ((dstAvg * dstAvg) + dstAvg) / 2
    return fuelRequired

#The best value for a linear fuel consumption shall be the rounded median
median = round(statistics.median(crabPositions))

#The best value for an exponential fuel consumption shall be around the average
avg = round(sum(crabPositions) / len(crabPositions))

#Calculate the fuel required for linear consumption
fuelRequiredMedian = 0
for crabPosition in crabPositions:
    fuelRequiredMedian += abs(crabPosition - median)

fuelRequiredAvgP2 = min(getFuel(avg - 1), getFuel(avg), getFuel(avg + 1))

print("2021 Day 6, Part 1: " + str(fuelRequiredMedian))
print("2021 Day 6, Part 2: " + str(fuelRequiredAvgP2))