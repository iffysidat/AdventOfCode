import re


def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    print(lines)
    return lines


def build_colour_dict(data):
    colour_mapping = {}

    # Credit Chris Clarke for an absolute banger of a regex that blew my mind
    contains_re = re.compile(r"(\d+) (.*?) bag[,|s|.]*")

    for line in data:
        line = line.split(" bags contain")
        contains = contains_re.findall(line[1])
        colour_mapping[line[0]] = {colour: int(number) for number, colour in contains}

    print(colour_mapping)
    return colour_mapping


def find_parents(target_bag, list_of_bags):
    print("Searching for target: " + str(target_bag))
    parents_found = set()
    for bag in list_of_bags:
        if target_bag in list_of_bags[bag].keys():
            parents_found.add(bag)

    if len(parents_found) != 0:
        # print("Target bag: " + str(target_bag + " has parents"))
        parents_to_search = parents_found.copy()
        #print("Searching parents: " + str(parents_found))
        for parent in parents_to_search:
            #print("Searching parent: " + str(parent))
            new_parents = find_parents(parent, list_of_bags)
            #print("New parents found: " + str(new_parents) + "Adding to: " + str(parents_found))
            parents_found = parents_found.union(new_parents)
            #print("Total parents found: " + str(parents_found))
            #print("Parent of parents: " + str(parents_of_parents))
        return parents_found
    else:
        return parents_found


def get_num_bags(target_bag, list_of_bags):
    bagsum = 0
    print("Searching target bag: " + str(target_bag))
    if list_of_bags[target_bag].keys():
        print("Bag contains bags")
        for bag in list_of_bags[target_bag]:
            #print("Searching bag: " + str(bag))
            print("Contains " + str(list_of_bags[target_bag][bag]) + " " + str(bag))
            bagsum = bagsum + list_of_bags[target_bag][bag] + list_of_bags[target_bag][bag] * get_num_bags(bag, list_of_bags)
        return bagsum
            #get_num_bags(bag, list_of_bags)
    else:
        print("No further bags contained")
        return bagsum


def part_one():
    rules = read_file("input.txt")

    # Make dictionary with each colour bag as key and value is another dictionary with key inner bag and value number
    bag_list = build_colour_dict(rules)

    # Find all permutations for shiny gold ideally recursively
    # Find bags where the bag we're looking for is a key inside it
    # Go through the bags we've found and do the same thing

    parents_of_target = find_parents("shiny gold", bag_list)
    print(parents_of_target)
    print(len(parents_of_target))


def part_two():
    rules = read_file("input.txt")
    bag_list = build_colour_dict(rules)

    bagsum = get_num_bags("shiny gold", bag_list)
    print(bagsum)


#part_one()
part_two()
