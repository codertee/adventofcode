import re
from copy import deepcopy
from itertools import pairwise, count

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def sign(x, y):
    return (x < y) - (x > y)


def fill_line(start, end):
    (x, y), (x2, y2) = start, end
    dx, dy = sign(x, x2), sign(y, y2)
    while (x, y) != (x2, y2):
        x, y = x + dx, y + dy
        yield x, y


def parse_input(input_str):
    rocks = set()
    for line in input_str.splitlines():
        coords = re.findall(r'(\d+),(\d+)', line)
        path = [(int(x), int(y)) for x, y in coords]
        for start, end in pairwise(path):
            rocks.update([start, end])
            rocks.update(list(fill_line(start, end)))
    floor = max(y for x, y in rocks) + 2
    return rocks, floor


def solve(blocked, floor, part):
    
    for c in count():
        x, y = 500, 0
        if part == 2 and (x, y) in blocked:
            return c
        while True:
            if y + 1 == floor:
                if part == 1:
                    return c
                blocked.add((x, y))
                break
            if (step := (x, y + 1)) not in blocked:
                x, y = step
            elif (step := (x - 1, y + 1)) not in blocked:
                x, y = step
            elif (step := (x + 1, y + 1)) not in blocked:
                x, y = step
            else:
                blocked.add((x, y))
                break


@aoc_timer(1, 14, 2022)
def solve_first(rocks, floor):
    rocks = deepcopy(rocks)
    return solve(rocks, floor, 1)


@aoc_timer(2, 14, 2022)
def solve_second(rocks, floor):
    return solve(rocks, floor, 2)


if __name__ == '__main__':
    args = parse_input(get_input(14, year=2022))
    solve_first(*args)
    solve_second(*args)
