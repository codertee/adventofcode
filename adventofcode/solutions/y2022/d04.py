import re

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    pairs = []
    for pair in input_str.splitlines():
        a, b, c, d = map(int, re.findall(r'\d+', pair))
        one = set(range(a, b + 1))
        other = set(range(c, d + 1))
        pairs.append((one, other))
    return pairs


@aoc_timer(1, 4, 2022)
def solve_first(pairs):
    return sum(one >= other or one <= other for one, other in pairs)


@aoc_timer(2, 4, 2022)
def solve_second(pairs):
    return sum(bool(one & other) for one, other in pairs)


if __name__ == '__main__':
    pairs = parse_input(get_input(4, year=2022))
    solve_first(pairs)
    solve_second(pairs)
