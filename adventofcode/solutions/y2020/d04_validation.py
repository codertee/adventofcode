import re

from adventofcode.inputs import get_input


def parse_input(input_str):
    return input_str.split('\n\n')


def solve_first(passports):
    required_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    valid = 0
    for passport_str in passports:
        all_keys = set()
        for token in passport_str.split():
            field, value = token.split(':')
            all_keys.add(field)
        if required_keys.issubset(all_keys):
            valid += 1
    print('2020.4 part one:', valid)


def validate_hgt(x):
    unit = x[-2:]
    height = int(x[:-2])
    if unit == 'cm':
        return 150 <= height <= 193
    elif unit == 'in':
        return 59 <= height <= 76
    else:
        return False


rules = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": validate_hgt,
    "hcl": lambda x: re.match("^#[0-9a-f]{6}$", x), 
    "ecl": lambda x: x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
    "pid": lambda x: re.match("^[0-9]{9}$", x)
}


def validate(passport):
    for key, validate_f in rules.items():
        value = passport.get(key)
        if value is None:
            return False
        try:
            if not validate_f(value):
                return False
        except Exception as e:
            return False
    return True


def solve_second(passports):
    valid = 0
    for passport_str in passports:
        passport = dict(
            token.split(':')
            for token in passport_str.split()
        )
        if validate(passport):
            valid += 1
    print('2020.4 part two:', valid)


if __name__ == '__main__':
    passports = parse_input(get_input(4, year=2020))
    solve_first(passports)
    solve_second(passports)