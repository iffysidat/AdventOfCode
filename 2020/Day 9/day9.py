def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    print(lines)
    return lines


def find_anomaly(preamble, numbers):
    # Start from index list[preamble]
    # Loop from here to end
    for number in numbers[preamble:]:
        print("Checking: " + str(number))
        #print(numbers.index(number, preamble))

        preamble_list = list(map(int, numbers[numbers.index(number, preamble) - preamble:numbers.index(number, preamble)]))
        print(preamble_list)
        number_satisfies_condition = 0
        # For each number check it can be made with the sum of 2 number from the preamble
        for i in preamble_list:
            #print(int(number) - int(i))
            if (int(number) - int(i)) in preamble_list:
                #print("Satisfies condition")
                number_satisfies_condition = 1
        if not number_satisfies_condition:
            print("Number does not satisfy condition: " + str(number))
            return number


def encryption_weakness(invalid, number_list):
    # If over target value remove first entry in current contiguous list
    # If under target value add the next entry to current contiguous list
    current_sum = 0
    target_value = invalid
    contiguous_values =[]
    index_to_add = 0
    index_to_remove = 0

    while current_sum != target_value:
        print("Current Sum: " + str(current_sum))
        if current_sum < target_value:
            current_sum += number_list[index_to_add]
            contiguous_values.append(number_list[index_to_add])
            print(contiguous_values)
            index_to_add += 1
            print(index_to_add)
        if current_sum > target_value:
            current_sum -= contiguous_values.pop(0)
            print(contiguous_values)
    print("Current sum is equal to target value: " + str(current_sum))
    print("Max: " + str(max(contiguous_values)))
    print("Min: " + str(min(contiguous_values)))

    print(max(contiguous_values) + min(contiguous_values))

def part_one():
    input = read_file("input.txt")
    print(find_anomaly(25, input))


def part_two():
    input = read_file("input.txt")
    invalid_number = find_anomaly(25, input)
    print(invalid_number)
    input = list(map(int, input))
    encryption_weakness(int(invalid_number), input)


#part_one()
part_two()