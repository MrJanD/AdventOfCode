import math

class Asteroid(object):
    def __init__(self, x_pos, y_pos, relative_angle = 0):
        self.x = x_pos
        self.relative_x = x_pos
        self.y = y_pos
        self.relative_y = y_pos
        self.relative_asteroid_list = []
        self.relative_angle = relative_angle

    def __eq__(self, other):
        if isinstance(other, Asteroid):
            return self.x == other.x and self.y == other.y
        return False

    def visible_asteroids(self):
        return len(self.relative_asteroid_list)

def get_asteroid_list():
    lines_of_file = open("input", "r").readlines()
    asteroid_list = []
    for y_value in range(len(lines_of_file)):
        line = list(lines_of_file[y_value])
        for x_value in range(len(line)):
            if line[x_value] == '#':
                asteroid_list.append(Asteroid(x_value, y_value))
    return asteroid_list

asteroid_list = get_asteroid_list()

def unique_list(list):
    unique_list = []
    for asteroid_index in range(len(list)):
        replaced = False
        for unique_asteroid_index in range(len(unique_list)):
            if list[asteroid_index].relative_angle == unique_list[unique_asteroid_index].relative_angle:
                if (list[asteroid_index].x + list[asteroid_index].y) < (unique_list[unique_asteroid_index].x +unique_list[unique_asteroid_index].y):
                    unique_list[unique_asteroid_index] = list[asteroid_index]
                replaced = True
        if not replaced:
            unique_list.append(list[asteroid_index])
    return unique_list

for asteroid_pov_index in range(len(asteroid_list)):
    for asteroid_target in asteroid_list:
        if asteroid_target != asteroid_list[asteroid_pov_index]:
            relative_x = asteroid_target.x - asteroid_list[asteroid_pov_index].x
            relative_y = asteroid_target.y - asteroid_list[asteroid_pov_index].y
            angle = math.degrees(math.atan2(relative_x, relative_y))
            asteroid_list[asteroid_pov_index].relative_asteroid_list.append(Asteroid(asteroid_target.x, asteroid_target.y, round(angle, 1)))
    asteroid_list[asteroid_pov_index].relative_asteroid_list = unique_list(asteroid_list[asteroid_pov_index].relative_asteroid_list)
    print("Calculating... " + str(round(asteroid_pov_index / len(asteroid_list) * 100)) + "% complete", end='\r')

best_asteroid = asteroid_list[0]
for asteroid_target in asteroid_list:
    if asteroid_target.visible_asteroids() > best_asteroid.visible_asteroids():
        best_asteroid = asteroid_target

print("Best asteroid coordinates: " + str(best_asteroid.x) + ", " + str(best_asteroid.y))
print("With a total number of visible asteroids: " + str(best_asteroid.visible_asteroids()) + "/" + str(len(asteroid_list)))

for asteroid in best_asteroid.relative_asteroid_list:
    asteroid.relative_angle = round(asteroid.relative_angle + 180.0, 1)
    if asteroid.relative_angle < 0:
        asteroid.relative_angle = 180.0 + abs(asteroid.relative_angle)

best_asteroid.relative_asteroid_list.sort(key = lambda x: x.relative_angle, reverse=True)
print("200th asteroid coordinates: " + str(best_asteroid.relative_asteroid_list[199].x) + ", " + str(best_asteroid.relative_asteroid_list[199].y))
print("200th asteroid x * 10 + y: " + str(best_asteroid.relative_asteroid_list[199].x * 100 + best_asteroid.relative_asteroid_list[199].y))

