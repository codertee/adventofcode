import re
from math import prod, ceil, floor

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str: str):
    times, distances = input_str.splitlines()
    return re.findall(r"\d+", times), re.findall(r"\d+", distances)


def solve(time, distance):
    """quadratic formula params: a = -1, b = time, c = -distance"""
    discr = time ** 2 - 4 * distance
    x1 = (time - discr ** 0.5) / 2
    x2 = (time + discr ** 0.5) / 2
    return ceil(x2) - floor(x1) - 1


@aoc_timer(1, 6, 2023)
def solve_first(times, distances):
    times, distances = map(int, times), map(int, distances)
    return prod(solve(t, d) for t, d in zip(times, distances))


@aoc_timer(2, 6, 2023)
def solve_second(times, distances):
    time, distance = int("".join(times)), int("".join(distances))
    return solve(time, distance)


if __name__ == "__main__":
    times, dists = parse_input(get_input(6, year=2023))
    solve_first(times, dists)
    solve_second(times, dists)
