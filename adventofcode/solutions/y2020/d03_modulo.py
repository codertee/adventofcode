from functools import partial

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    return input_str.splitlines()


def count_trees(forest, right, down):
    rows, cols = len(forest), len(forest[0])
    trees = 0
    for row in range(down, rows, down):
        column = int((row / down) * right % cols) 
        if forest[row][column] == '#':
            trees += 1
    return trees


@aoc_timer(1, 3, 2020)
def solve_first(forest):
    return count_trees(forest, 3, 1)


@aoc_timer(2, 3, 2020)
def solve_second(forest):
    count = partial(count_trees, forest)
    return count(1, 1) * count(3, 1) * count(5, 1) * count(7, 1) * count(1, 2)


if __name__ == '__main__':
    forest = parse_input(get_input(3, year=2020))
    solve_first(forest)
    solve_second(forest)
