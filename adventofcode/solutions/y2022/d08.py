from itertools import product, count

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
        for tallest, *rest in grid:
            count += tallest.seen()
            for tree in rest:
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
    for i in count():
        r, c = r + dr, c + dc
        if r < 0 or c < 0 or r > boundary or c > boundary:
            return i
        if grid[r][c] >= height:
            return i + 1


@aoc_timer(2, 8, 2022)
def solve_second(grid):
    score = 0
    for i, j in product(range(len(grid[0])), repeat=2):
        e = count_trees(i, j, 0, 1, grid)
        w = count_trees(i, j, 0, -1, grid)
        s = count_trees(i, j, 1, 0, grid)
        n = count_trees(i, j, -1, 0, grid)
        score = max(score, n * w * s * e)
    return score


if __name__ == '__main__':
    grid = parse_input(get_input(8, year=2022))
    solve_first(grid)
    solve_second(grid)
