import os
from functools import partial
from itertools import starmap, product, chain
from multiprocessing import Pool
from operator import add

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


class Vector(tuple):

    def __add__(self, other):
        return Vector(starmap(add, zip(self, other)))


def V(*args):
    return Vector(args)


RIGHT, DOWN, LEFT, UP = V(0, 1), V(1, 0), V(0, -1), V(-1, 0)
STEPS = {
    "\\": {RIGHT: [DOWN], LEFT: [UP], DOWN: [RIGHT], UP: [LEFT]},
    "/": {RIGHT: [UP], LEFT: [DOWN], DOWN: [LEFT], UP: [RIGHT]},
    "-": {RIGHT: [RIGHT], LEFT: [LEFT], DOWN: [LEFT, RIGHT], UP: [LEFT, RIGHT]},
    "|": {RIGHT: [UP, DOWN], LEFT: [UP, DOWN], DOWN: [DOWN], UP: [UP]},
    ".": {RIGHT: [RIGHT], LEFT: [LEFT], DOWN: [DOWN], UP: [UP]}
}


def parse_input(input_str):
    str_grid = input_str.splitlines()
    rows, cols = len(str_grid), len(str_grid[0])
    grid = {}
    for r, c in product(range(rows), range(cols)):
        grid[V(r, c)] = str_grid[r][c]
    return grid, (rows, cols)


def energize(grid: dict[Vector, str], start: tuple[Vector, Vector]):
    stack, seen = [start], {start}
    while stack:
        cur, dir = stack.pop()
        for step in STEPS[grid[cur]][dir]:
            nxt = cur + step
            if nxt not in grid or (nxt, step) in seen:
                continue
            stack.append((nxt, step))
            seen.add((nxt, step))
    return len(set(loc for loc, _ in seen))


@aoc_timer(1, 16, 2023)
def solve_first(grid, _):
    return energize(grid, (V(0, 0), RIGHT))


@aoc_timer(2, 16, 2023)
def solve_second(grid, extents):
    rows, cols = extents
    starts = chain(
        [(V(0, c), DOWN) for c in range(cols)],
        [(V(rows - 1, c), UP) for c in range(cols)],
        [(V(r, 0), RIGHT) for r in range(rows)],
        [(V(r, cols - 1), LEFT) for r in range(rows)]
    )
    with Pool(int(os.cpu_count() / 2)) as p:
        return max(p.map(partial(energize, grid), starts))


if __name__ == "__main__":
    grid, extents = parse_input(get_input(16, year=2023))
    solve_first(grid, extents)
    solve_second(grid, extents)
