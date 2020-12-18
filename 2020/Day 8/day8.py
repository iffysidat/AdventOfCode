import copy

def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    print(lines)
    return lines


def parse_input(input):
    # Input is list of instructions
    # Turn list of instructions into a list of dictionaries with 2 keys
    instruction_list = []

    # This can easily be done with list comprehension
    for instruction in input:
        inst_dict = {}
        instruction = instruction.split()
        inst_dict['operation'] = instruction[0]
        inst_dict['argument'] = instruction[1]
        instruction_list.append(inst_dict)

    return instruction_list

def run_program(instructions):
    end_program = False
    inst_num = 0
    accumulator = 0
    instruction_history = []

    # While not duplicate or end of program list
    # Check instruction
    # Execute instruction
    # Add instruction number to instruction history
    # Increment instruction number
    # Check if next instruction_num is in instruction history or if instruction_num >= len(instructions)
    while not end_program:
        instruction = instructions[inst_num]
        operation = instruction['operation']
        #print(operation)
        argument = instruction['argument']
        #print(argument)

        instruction_history.append(inst_num)

        if operation == 'acc':
            accumulator += int(argument)
            inst_num += 1
        elif operation == 'jmp':
            inst_num += int(argument)
        elif operation == 'nop':
            inst_num += 1
        else:
            print("Bad Instruction")

        if inst_num in instruction_history:
            end_program = True
            print("This program will loop infinitely with latest acc value of: " + str(accumulator))

        if inst_num >= len(instructions):
            end_program = True
            print("This program has executed to the end with acc value of: " + str(accumulator))

        #print(len(instruction_history))
        #print(accumulator)



def part_one():
    instructions = parse_input(read_file("test.txt"))
    print(instructions)
    run_program(instructions)


def part_two():
    instructions = parse_input(read_file("input.txt"))
    print(instructions)

    for i in range(0, len(instructions) - 1):
        instruction_copy = copy.deepcopy(instructions)

        if instructions[i]['operation'] == 'jmp':
            instruction_copy[i]['operation'] = 'nop'
        elif instructions[i]['operation'] == 'nop':
            instruction_copy[i]['operation'] = 'jmp'

        run_program(instruction_copy)


#part_one()
part_two()