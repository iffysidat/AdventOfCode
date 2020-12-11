def read_file(filename):
    with open(filename) as f:
        lines = f.read().split("\n\n")
    print(lines)
    return lines

def part_one():
    questions = read_file("input.txt")
    questions = [line.replace("\n", "") for line in questions]
    yes_count = 0
    for group in questions:
        questions_answered = len(set(group))
        print(set(group))
        print(questions_answered)
        yes_count += questions_answered

    print(yes_count)

def part_two():
    questions = read_file("input.txt")

    yes_common_count = 0
    for group in questions:
        individuals = group.split("\n")
        print(individuals)
        common_questions = list(individuals[0])
        #print(common_questions)
        for individual in individuals:
            common_questions = list(set(common_questions) & set(individual))
            #print("COMMON" + str(common_questions))
        print(len(common_questions))
        yes_common_count += len(common_questions)
    print(yes_common_count)

#part_one()
part_two()