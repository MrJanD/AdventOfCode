class Position:
    def __init__(self, direction, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.direction = direction

    def nextStep(self, action, value):
        if action == 'N':
            self.ypos += value
        if action == 'S':
            self.ypos -= value
        if action == 'E':
            self.xpos += value
        if action == 'W':
            self.xpos -= value
        if action == 'L':
            self.direction = (self.direction - (value / 90)) % 4
        if action == 'R':
            self.direction = (self.direction + (value / 90)) % 4
        if action == 'F':
            if self.direction == 0:
                self.nextStep('N', value)
            if self.direction == 1:
                self.nextStep('E', value)
            if self.direction == 2:
                self.nextStep('S', value)
            if self.direction == 3:
                self.nextStep('W', value)

with open("../Inputs/day12", "r") as fp:
    lines = [(line.rstrip()[0], int(line.rstrip()[1:]))  for line in fp.readlines()]

position = Position(1, 0, 0)
for line in lines:
    position.nextStep(line[0], line[1])

print("Day 12, Part 1: " + str(abs(position.xpos) + abs(position.ypos)))

class RelativePosition:
    def __init__(self, waypointx, waypointy, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.waypointx = waypointx
        self.waypointy = waypointy

    def nextStep(self, action, value):
        if action == 'N':
            self.waypointy += value
        if action == 'S':
            self.waypointy -= value
        if action == 'E':
            self.waypointx += value
        if action == 'W':
            self.waypointx -= value
        if action == 'L':
            if (value / 90) %  4 == 1:
                tempY = self.waypointy
                self.waypointy = self.waypointx
                self.waypointx = -(tempY)
            if (value / 90) %  4 == 2:
                self.waypointy = -(self.waypointy)
                self.waypointx = -(self.waypointx)
            if (value / 90) %  4 == 3:
                tempY = self.waypointy
                self.waypointy = -(self.waypointx)
                self.waypointx = tempY
        if action == 'R':
            if value == 90:
                self.nextStep('L', 270)
            if value == 180:
                self.nextStep('L', 180)
            if value == 270:
                self.nextStep('L', 90)
        if action == 'F':
            self.xpos = self.xpos + (self.waypointx * value)
            self.ypos = self.ypos + (self.waypointy * value)

relativePosition = RelativePosition(10, 1, 0, 0)
for line in lines:
    relativePosition.nextStep(line[0], line[1])

print("Day 12, Part 2: " + str(abs(relativePosition.xpos) + abs(relativePosition.ypos)))
