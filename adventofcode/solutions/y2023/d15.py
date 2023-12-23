import re
from functools import reduce

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    return input_str.strip().split(",")


def _hash(data: str):
    return reduce(lambda a, b: (a + b) * 17 % 256, map(ord, data), 0)


@aoc_timer(1, 15, 2023)
def solve_first(seq):
    return sum(map(_hash, seq))


@aoc_timer(2, 15, 2023)
def solve_second(seq):
    boxes = [{} for _ in range(256)]
    for step in seq:
        match re.match(r"(\w+?)(=|-)(\d+)?", step).groups():
            case label, "=", f:
                boxes[_hash(label)][label] = int(f)
            case label, "-", None:
                boxes[_hash(label)].pop(label, None)
    power = 0
    for box, lenses in enumerate(boxes):
        for i, f in enumerate(lenses.values(), 1):
            power += (box + 1) * i * f
    return power


if __name__ == "__main__":
    seq = parse_input(get_input(15, year=2023))
    solve_first(seq)
    solve_second(seq)
