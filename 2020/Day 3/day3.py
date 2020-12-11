import math

def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    #print(lines)
    return lines

def part_one(move_right, move_down):
    woods = read_file("input.txt")

    wood_width = len(woods) * move_right
    line_copies = wood_width/(len(woods[0]))

    final_map = [line*(math.ceil(line_copies)) for line in woods]

    final_map = [list(line) for line in final_map]

    row_index = 0
    column_index = 0

    trees = 0

    while row_index < len(woods):
        char_to_check = final_map[row_index][column_index]
        if char_to_check == "#":
            trees += 1
        row_index += move_down
        column_index += move_right

    print("Number of Trees: " + str(trees))
    return trees


def part_two():
    print(part_one(3, 1) * part_one(1, 1) * part_one(5, 1) * part_one(7, 1) * part_one(1, 2))

part_one(3, 1)
part_two()









