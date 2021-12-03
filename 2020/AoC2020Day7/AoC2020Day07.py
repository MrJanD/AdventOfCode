input = [line.strip() for line in open("../Inputs/day7", "r")]
import re

class Bag:
    def __init__(self, line):
        self.splittedLine = re.split(' bags contain | bag\.| bag, | bags\.| bags, ', line)
        if self.splittedLine[-1] == '':
            self.splittedLine.pop()
        self.color = self.splittedLine[0]
        self.content = self.splittedLine.copy()
        self.content.pop(0)
        self.content = [item for item in self.content if item != "no other"]
        self.foundIn = []
        self.count = 0
        self.containingBagColors = self.getColorContent()

    def getColorContent(self):
        lst = []
        for item in self.content:
            lst.append(item[2:])
            self.count += int(item[0])
        return lst

    def getCountOfColor(self, color):
        for content in self.content:
            if color in content:
                return int(content[0])
        return 0

bags = {}
for line in input:
    currentBag = Bag(line)
    bags[currentBag.color] = currentBag

def canContainBag(currentBagColor, wantedBagColor):
    if currentBagColor == wantedBagColor:
        return True
    elif currentBagColor not in bags:
        return False
    else:
        for bag in bags[currentBagColor].containingBagColors:
            if canContainBag(bags[bag].color, wantedBagColor):
                return True
        return False

def countBags(wantedBagColor):
    count = bags[wantedBagColor].count
    for bag in bags[wantedBagColor].containingBagColors:
        count += bags[wantedBagColor].getCountOfColor(bag) * countBags(bag)
    return count

count = 0
for bagKey, bagValue in bags.items():
    if canContainBag(bagKey, "shiny gold"):
        count += 1
count -= 1

print("Day 7, Part 1: " + str(count))
print("Day 7, Part 2: " + str(countBags("shiny gold")))
