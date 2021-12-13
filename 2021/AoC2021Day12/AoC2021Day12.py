from collections import defaultdict, deque

input = [line.strip() for line in open("../Inputs/day12", "r")]
map = defaultdict(list)
for line in input:
    left, right = line.split("-")
    if right != "start":
        map[left].append(right)
    if left != "start":
        map[right].append(left)

def singleVisit(map):
    validPaths = 0
    paths = deque([(["start"], set(), False)])

    while paths:
        path, smallCaves, doubleVisited = paths.popleft()
        for cave in map[path[-1]]:
            if cave == 'end':
                validPaths += 1
            elif cave.islower():
                if cave not in smallCaves:
                    s = smallCaves|{cave}
                    paths.append((path + [cave], s, doubleVisited))
            else:
                paths.append((path + [cave], smallCaves, doubleVisited))
    return validPaths

def doubleVisit(map):
    validPaths = 0
    paths = deque([(["start"], set(), False)])

    while paths:
        path, smallCaves, doubleVisited = paths.popleft()
        for cave in map[path[-1]]:
            if cave == 'end':
                validPaths += 1
            elif cave.islower():
                if cave not in smallCaves:
                    s = smallCaves|{cave}
                    paths.append((path + [cave], s, doubleVisited))
                elif not doubleVisited:
                    paths.append((path + [cave], smallCaves, True))
            else:
                paths.append((path + [cave], smallCaves, doubleVisited))
    return validPaths

print("2021 Day 12, Part 1: " + str(singleVisit(map)))
print("2021 Day 12, Part 2: " + str(doubleVisit(map)))