import intcode

class Robot(object):
    def __init__(self):
        self.direction_facing = 0 # 0 = up, 1 = 90°, 2 = 180°, 3 = 270°
        self.position = (0, 0)

    def set_direction_facing(turn_direction):
        if turn_direction == 0:
            self.direction_facing = (self.direction_facing + 3) % 4
        elif turn_direction == 1:
            self.direction_facing = (self.direction_facing + 1) % 4

    def get_direction_facing():
        return self.direction_facing

    def get_direction_facing_degrees():
        return self.direction_facing * 90

    def move():
        coordinate = list(self.position)
        if self.direction_facing == 0:
            coordinate[1] -= 1
        if self.direction_facing == 1:
            coordinate[0] += 1
        if self.direction_facing == 2:
            coordinate[1] += 1
        if self.direction_facing == 3:
            coordinate[0] -= 1
        self.position = tuple(coordinate)

with open("input", "r") as f:
    read_input_values = [ int(x) for x in f.read().split(",") ]

robot = Robot()
panel_color = 0

amp = intcode.Intcode(read_input_values)
amp.solveOpcode(panel_color)
while len(amp.output_stream) == 2:
    amp.output_stream = []


