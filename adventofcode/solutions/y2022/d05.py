import re
from copy import deepcopy

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    stacks_str, operations_str = input_str.split('\n\n')
    transposed = list(zip(*stacks_str.splitlines()))
    stacks = {}
    for line in transposed[1::4]:
        stack = list(c for c in line if c != ' ')
        key = stack.pop()
        stack.reverse()
        stacks[key] = stack
    operations = []
    for o in operations_str.splitlines():
        amount, key, to = re.findall(r'(\d+) from (\d+) to (\d+)', o).pop()
        operations.append((int(amount), key, to))
    return stacks, operations


@aoc_timer(1, 5, 2022)
def solve_first(stacks, ops):
    stacks = deepcopy(stacks)
    for amount, key, to in ops:
        for _ in range(amount):
            stacks[to].append(stacks[key].pop())
    return ''.join(map(list.pop, stacks.values()))


@aoc_timer(2, 5, 2022)
def solve_second(stacks, ops):
    for amount, key, to in ops:
        take_from = stacks[key]
        stacks[to].extend(take_from[-amount:])
        stacks[key] = take_from[:-amount]
    return ''.join(map(list.pop, stacks.values()))


if __name__ == '__main__':
    stacks, ops = parse_input(get_input(5, year=2022))
    solve_first(stacks, ops)
    solve_second(stacks, ops)
