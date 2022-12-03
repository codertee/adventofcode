from itertools import count
from string import ascii_letters

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer

CHARMAP = dict(zip(ascii_letters, count(1)))


def parse_input(input_str):
    return input_str.splitlines()


@aoc_timer(1, 3, 2022)
def solve_first(rucksacks):
    priorities = 0
    for sack in rucksacks:
        mid = len(sack) // 2
        first = set(sack[:mid])
        second = set(sack[mid:])
        common = first.intersection(second).pop()
        priorities += CHARMAP[common]
    return priorities


@aoc_timer(2, 3, 2022)
def solve_second(rucksacks):
    priorities = 0
    for i in range(0, len(rucksacks) - 2, 3):
        group = map(set, rucksacks[i: i + 3])
        common = set.intersection(*group).pop()
        priorities += CHARMAP[common]
    return priorities


if __name__ == '__main__':
    rucksacks = parse_input(get_input(3, year=2022))
    solve_first(rucksacks)
    solve_second(rucksacks)
