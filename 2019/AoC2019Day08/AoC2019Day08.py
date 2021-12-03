file = open("input", "r").readline()

width = 25
hight = 6

pixel_list = [int(i) for i in file]
picture = [[[]]]
pixel_index = 0
line_index = 0
layer_index = 0
index = 0

def validityCheck():
    is_valid = True
    if len(pixel_list) % width != 0:
        is_valid = False
    if len(pixel_list) % (width * hight) != 0:
        is_valid = False

    return is_valid

def get_picture():
    picture = []
    index = 0
    while index < len(pixel_list):
        picture.append(get_layer(index))
        index += (width * hight)
    return picture

def get_layer(index):
    layer = []
    relative_index = 0
    while relative_index < (width * hight):
        layer.append(get_line(index + relative_index))
        relative_index += width
    return layer

def get_line(index):
    line = []
    relative_index = 0
    while relative_index < width:
        line.append(pixel_list[index + relative_index])
        relative_index += 1
    return line

count_0 = 0
count_1 = 0
count_2 = 0
count_of_0s_in_layer = width * hight

def count_in_line(line, number):
    return line.count(number)

def count_in_layer(layer, number):
    count = 0
    for line in layer:
        count += line.count(number)
    return count

def count_in_picture(picture, number):
    count = 0
    for layer in picture:
        count += count_in_layer(layer, number)
    return count

for layer in get_picture():
    layer_count = count_in_layer(layer, 0)
    if  layer_count < count_of_0s_in_layer:
        count_0 = count_in_layer(layer, 0)
        count_1 = count_in_layer(layer, 1)
        count_2 = count_in_layer(layer, 2)
        count_of_0s_in_layer = layer_count

print("Occurrence of '1': " + str(count_1))
print("Occurrence of '2': " + str(count_2))
print("Multiplied answer: " + str(count_1 * count_2))

# Part2:
def overlay_layer(layer, current_picture):
    line_index = 0
    while line_index < hight:
        pixel_index = 0
        while pixel_index < width:
            if current_picture[line_index][pixel_index] == 2:
                current_picture[line_index][pixel_index] = layer[line_index][pixel_index]
            pixel_index += 1
        line_index += 1
    return current_picture

current_picture = [[2] * 25, [2] * 25, [2] * 25, [2] * 25, [2] * 25, [2] * 25]
for layer in get_picture():
    current_picture = overlay_layer(layer, current_picture)

def transform_to_picture(int_picture):
    stringified_picture = []
    for line in int_picture:
        stringified_line = []
        for pixel in line:
            if pixel == 0:
                stringified_line.append(' ')
            else:
                stringified_line.append('#')
        stringified_picture.append(stringified_line)
    return stringified_picture

stringified_picture = transform_to_picture(current_picture)
for line in stringified_picture:
    print(*line, sep = "")