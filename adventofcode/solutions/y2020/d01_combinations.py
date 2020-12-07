import math
from itertools import combinations, dropwhile

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


@aoc_timer()
def parse_input(input_str):
    return list(map(int, input_str.split()))


def solve(expenses, n):
    constraint = lambda x: sum(x) != 2020
    accepted_values = next(dropwhile(constraint, combinations(expenses, n)))
    return math.prod(accepted_values)


@aoc_timer(1, 1, 2020)
def solve_first(expenses):
    return solve(expenses, 2)


@aoc_timer(2, 1, 2020)
def solve_second(expenses):
    return solve(expenses, 3)


if __name__ == '__main__':
    expenses = parse_input(get_input(1, year=2020))
    solve_first(expenses)
    solve_second(expenses)
