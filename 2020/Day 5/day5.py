def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    print(lines)
    return lines


def part_one():
    boarding_passes = read_file("input.txt")
    greatest_id = 0

    for boarding_pass in boarding_passes:
        upper_row = 0b1111111
        lower_row = 0b0000000

        upper_col = 0b111
        lower_col = 0b000

        for letter in boarding_pass:
            if letter == "F" or letter == "B":
                if letter == "F":
                    upper_row = (upper_row + lower_row) >> 1
                elif letter == "B":
                    lower_row = lower_row + ((upper_row - lower_row) >> 1) + 1
            elif letter == "L" or letter == "R":
                if letter == "L":
                    upper_col = (upper_col + lower_col) >> 1
                elif letter == "R":
                    lower_col = lower_col + ((upper_col - lower_col) >> 1) + 1
        id = upper_row * 8 + upper_col

        if id > greatest_id:
            greatest_id = id

    print(greatest_id)

def part_two():
    boarding_passes = read_file("input.txt")

    mapping = {
        'B': '1',
        'F': '0',
        'R': '1',
        'L': '0'
    }

    binary_passes =[]
    ids = []

    for boarding_pass in boarding_passes:
        pass_to_binary = [''.join(letter.replace(letter, mapping[letter]) for letter in boarding_pass)]
        binary_passes.append(pass_to_binary[0])

    print(binary_passes)

    for binary_string in binary_passes:
        row = int(binary_string[:7], 2)
        column = int(binary_string[7:], 2)
        ids.append(row * 8 + column)

    print(ids)

    missing_ids = set(range(0, 1024)) - set(ids)
    print(missing_ids)

    for missing_id in missing_ids:
        if (missing_id+1) in ids and (missing_id-1) in ids:
            print(missing_id)

#part_one()

part_two()