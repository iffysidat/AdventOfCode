def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    print(lines)
    return lines

def part_one(number_list, set):
    for (number) in number_list:
        if 2020 - number in set:
            return number * (2020 - number)

def part_two(number_list, set):
    for num1 in number_list:
        for num2 in number_list:
            if 2020-num1-num2 in set:
                return num1 * num2 * (2020 - num1 - num2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input = read_file('input.txt')

    # Convert from list of string to list of int
    input = list(map(int, input))
    num_set = set(input)

    print(part_one(input, num_set))
    print(part_two(input, num_set))
