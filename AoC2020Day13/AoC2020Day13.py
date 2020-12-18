input = [line.strip() for line in open("../Inputs/day13", "r")]

departureMin = int(input[0])
shedule = input[1].split(',')
clearedShedule = shedule.copy()

for x in shedule:
    if x == 'x':
        clearedShedule.remove(x)
clearedShedule = [int(busLine) for busLine in clearedShedule]

busLine = 0
earliestDeparture = departureMin + max(clearedShedule)

for busCycle in clearedShedule:
    earliestDepartureWithBus = (int(departureMin / busCycle) + 1) * busCycle
    if earliestDepartureWithBus < earliestDeparture:
        earliestDeparture = earliestDepartureWithBus
        busLine = busCycle

minutesToWait = earliestDeparture - departureMin
print("Day 13, Part 1: " + str(busLine * minutesToWait))

busses = ["x" if x == "x" else int(x) for x in shedule]

modulos = {bus: -i % bus for i, bus in enumerate(busses) if bus != "x"}
vals = list(reversed(sorted(modulos)))
val = modulos[vals[0]]
r = vals[0]
for b in vals[1:]:
    while val % b != modulos[b]:
        val += r
    r *= b

print("Day 13, Part 2: " + str(val))


