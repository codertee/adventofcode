from functools import partial
from adventofcode.inputs import get_input


def parse_input(input_str):
    return input_str.splitlines()


def count_trees(forest, right, down):
    rows = len(forest)
    cols = len(forest[0])
    trees = 0
    for row in range(down, rows, down):
        column = int((row / down) * right % cols)
        current_cell = forest[row][column]
        if current_cell == '#':
            trees += 1
    return trees


def solve_first(forest):
    trees = count_trees(forest, 3, 1)
    print('2020.3 part one:', trees)


def solve_second(forest):
    count = partial(count_trees, forest)
    answer = count(1, 1) * count(3, 1) * count(5, 1) * count(7, 1) * count(1, 2)
    print('2020.3 part two:', answer)


if __name__ == '__main__':
    forest = parse_input(get_input(3, year=2020))
    solve_first(forest)
    solve_second(forest)