from collections import defaultdict

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    return list(map(int, input_str.split(',')))


def solve(numbers, N):
    mem = {n: i for i, n in enumerate(numbers[:-1], 1)}
    mem = defaultdict(bool, mem)
    last = numbers[-1]
    for turn in range(len(numbers), N):
        current = mem[last]
        current = turn - current if current else 0
        mem[last] = turn
        last = current
    return current


@aoc_timer(1, 15, 2020)
def solve_first(numbers):
    return solve(numbers, 2020)


@aoc_timer(2, 15, 2020)
def solve_second(numbers):
    return solve(numbers, 30000000)


if __name__ == '__main__':
    numbers = parse_input(get_input(15, year=2020))
    solve_first(numbers)
    solve_second(numbers)
