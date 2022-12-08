from uuid import uuid4
from itertools import product

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer

MAX_HEIGHT = 9


def parse_input(input_str):
    return [
        list(map(int, trees))
        for trees in input_str.splitlines()
    ]


def rotate(grid):
    return [c[::-1] for c in zip(*grid)]


@aoc_timer(1, 8, 2022)
def solve_first(grid_orig):
    grid = []
    for trees in grid_orig:
        grid.append([(t, uuid4()) for t in trees])
    seen = set()
    for _ in range(4):
        for row in grid:
            tallest, uid = row[0]
            seen.add(uid)
            for tree, uid in row[1:]:
                if tallest == MAX_HEIGHT:
                    break
                if tree > tallest:
                    seen.add(uid)
                    tallest = tree
        grid = rotate(grid)
    return len(seen)


def count_trees(r, c, dr, dc, condition, grid):
    boundary = len(grid[0]) - 1
    count = 0
    while True:
        r += dr
        c += dc
        if r < 0 or c < 0 or r > boundary or c > boundary:
            break
        count += 1
        if grid[r][c] >= condition:
            break
    return count


@aoc_timer(2, 8, 2022)
def solve_second(grid):
    grid_length = len(grid[0])
    best = 0
    for i, j in product(range(grid_length), repeat=2):
        tree = grid[i][j]
        e = count_trees(i, j, 0, 1, tree, grid)
        w = count_trees(i, j, 0, -1, tree, grid)
        s = count_trees(i, j, 1, 0, tree, grid)
        n = count_trees(i, j, -1, 0, tree, grid)
        score = n * w * s * e
        if score > best:
            best = score
    return best


if __name__ == '__main__':
    grid = parse_input(get_input(8, year=2022))
    solve_first(grid)
    solve_second(grid)
