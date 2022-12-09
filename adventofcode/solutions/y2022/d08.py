from itertools import product

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer

MAX_HEIGHT = 9


class Tree(int):
    def __new__(cls, value):
        cls.checked = False
        return super(cls, cls).__new__(cls, value)
    
    def seen(self):
        if not self.checked:
            self.checked = True
            return 1
        return 0


def parse_input(input_str):
    return [
        list(map(Tree, trees))
        for trees in input_str.splitlines()
    ]


def rotate(grid):
    return [c[::-1] for c in zip(*grid)]


@aoc_timer(1, 8, 2022)
def solve_first(grid):
    count = 0
    for _ in range(4):
        for row in grid:
            tallest = row[0]
            count += tallest.seen()
            for tree in row[1:]:
                if tallest == MAX_HEIGHT:
                    break
                if tree > tallest:
                    count += tree.seen()
                    tallest = tree
        grid = rotate(grid)
    return count


def count_trees(r, c, dr, dc, grid):
    height = grid[r][c]
    boundary = len(grid[0]) - 1
    count = 0
    while True:
        r += dr
        c += dc
        if r < 0 or c < 0 or r > boundary or c > boundary:
            return count
        count += 1
        if grid[r][c] >= height:
            return count


@aoc_timer(2, 8, 2022)
def solve_second(grid):
    grid_length = len(grid[0])
    best = 0
    for i, j in product(range(grid_length), repeat=2):
        e = count_trees(i, j, 0, 1, grid)
        w = count_trees(i, j, 0, -1, grid)
        s = count_trees(i, j, 1, 0, grid)
        n = count_trees(i, j, -1, 0, grid)
        score = n * w * s * e
        if score > best:
            best = score
    return best


if __name__ == '__main__':
    grid = parse_input(get_input(8, year=2022))
    solve_first(grid)
    solve_second(grid)
