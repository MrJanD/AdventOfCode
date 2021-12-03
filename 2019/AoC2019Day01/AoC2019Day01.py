linesOfFile = open("input", "r").readlines()
totalFuel = 0
totalFuelWithFuel = 0

def calculateFuel(mass):
    return int(int(mass) / 3) - 2

for mass in linesOfFile:
    totalFuel += calculateFuel(mass)
    while calculateFuel(mass) > 0:
        totalFuelWithFuel += calculateFuel(mass)
        mass = calculateFuel(mass)

print("Total fuel required for modules only: " + str(totalFuel))

print("Total fuel required for modules and fuel: " + str(totalFuelWithFuel))