import math
import re

def read_file(filename):
    with open(filename) as f:
        lines = f.read().split("\n\n")
    lines = [line.replace("\n", " ") for line in lines]
    print(lines)
    return lines

def parse_passport(passport_list):
    passport_dict = []

    for passport in passport_list:
        temp_dict = {}
        for pair in passport.split(' '):
            kv = pair.split(":")
            temp_dict[kv[0]] = kv[1]
        passport_dict.append(temp_dict)

    return passport_dict


def validate_byr(byr):
    return len(byr) == 4 and 1920 <= int(byr) <= 2002


def validate_iyr(iyr):
    return len(iyr) == 4 and 2010 <= int(iyr) <=2020


def validate_eyr(eyr):
    return len(eyr) == 4 and 2020 <= int(eyr) <= 2030


def validate_hgt(hgt):
    if hgt.endswith("cm"):
        return 150 <= int(hgt[:-2]) <= 193
    elif hgt.endswith("in"):
        return 59 <= int(hgt[:-2]) <= 76


def validate_hcl(hcl):
    return bool(re.match(r"^#[a-f0-9]{6}$", hcl))


def validate_ecl(ecl):
    eye_colours = ["amb","blu","brn","gry","grn","hzl","oth"]
    return ecl in eye_colours


def validate_pid(pid):
    return len(pid) == 9


def validate_passport(passport):
    return validate_byr(passport['byr']) and validate_hcl(passport['hcl']) and validate_hgt(passport['hgt'])\
           and validate_ecl(passport['ecl']) and validate_iyr(passport['iyr']) and validate_eyr(passport['eyr'])\
           and validate_pid(passport['pid'])


def part_one():
    passports = read_file("input.txt")
    passport_dictionary = parse_passport(passports)

    print(passport_dictionary)
    print(len(passport_dictionary))

    valid_passports = 0

    for passport in passport_dictionary:
        if len(passport) == 8:
            valid_passports += 1
        elif len(passport) == 7 and "cid" not in passport:
            valid_passports += 1

    print(valid_passports)


def part_two():
    passports = read_file("input.txt")
    passport_dictionary = parse_passport(passports)

    valid_passports = 0

    for passport in passport_dictionary:
        if len(passport) == 8 and validate_passport(passport):
            valid_passports += 1
        elif len(passport) == 7 and "cid" not in passport and validate_passport(passport):
            valid_passports += 1

    print(valid_passports)

part_one()
part_two()