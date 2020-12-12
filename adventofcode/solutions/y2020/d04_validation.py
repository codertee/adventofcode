import re
from functools import partial

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_passport(passport_str):
    return dict(token.split(':') for token in passport_str.split())


def parse_input(input_str):
    return list(map(parse_passport, input_str.split('\n\n')))


@aoc_timer(1, 4, 2020)
def solve_first(passports):
    required_keys = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    validate = partial(set.issubset, required_keys)
    return len(list(filter(validate, passports)))


def validate_hgt(x):
    m = re.match(r'(\d+)(in|cm)', x)
    if not m:
        return False
    height, unit = int(m.group(1)), m.group(2)
    if unit == 'cm':
        return 150 <= height <= 193
    elif unit == 'in':
        return 59 <= height <= 76
    else:
        return False


RULES = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": validate_hgt,
    "hcl": lambda x: re.match("^#[0-9a-f]{6}$", x), 
    "ecl": lambda x: x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
    "pid": lambda x: re.match("^[0-9]{9}$", x)
}


def validate(passport):
    for key, valid in RULES.items():
        if key not in passport:
            return False
        if not valid(passport[key]):
            return False
    return True


@aoc_timer(1, 4, 2020)
def solve_second(passports):
    return len(list(filter(validate, passports)))


if __name__ == '__main__':
    passports = parse_input(get_input(4, year=2020))
    solve_first(passports)
    solve_second(passports)
