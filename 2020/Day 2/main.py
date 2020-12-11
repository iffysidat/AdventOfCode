def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    print(lines)

    return lines


def parse_line(line):

    line = line.replace(":", "")
    line = line.split()

    line[0] = line[0].split("-")
    targets = {"min" : line[0][0], "max" : line[0][1]}

    parsed_line = [targets.get("min"), targets.get("max"), line[1], line[2]]
    return parsed_line



def part_one(input):
    valid_passwords = 0

    for line in input:
        line = parse_line(line)

        minletters = int(line[0])
        maxletters = int(line[1])
        letter = line[2]
        password = line[3]

        num_target_letter = 0

        for character in password:
            if character == letter:
                num_target_letter += 1

        if num_target_letter >= minletters and num_target_letter <= maxletters:
            valid_passwords += 1

    print(valid_passwords)


def part_two(input):
    valid_passwords = 0

    for line in input:
        line = parse_line(line)

        valid_index = int(line[0])
        invalid_index = int(line[1])
        letter = line[2]
        password = line[3]

        password = list(password)
        print(list(password))

        if password[valid_index-1] == letter and password[invalid_index-1] != letter or password[invalid_index-1] == letter and password[valid_index-1] != letter:
            valid_passwords += 1

    print(valid_passwords)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input = read_file('input.txt')
    #part_one(input)
    part_two(input)



