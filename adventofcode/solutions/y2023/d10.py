import re
from itertools import starmap, product
from operator import add

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


class Vector(tuple):

    def __add__(self, other):
        return Vector(starmap(add, zip(self, other)))


def V(*args):
    return Vector(args)


DIRS = RIGHT, DOWN, LEFT, UP = V(0, 1), V(1, 0), V(0, -1), V(-1, 0)
BENDS = str.maketrans("J7FL|-", "┘┐┌└│─")
STEP = {
    (DOWN, "┘"): LEFT, (RIGHT, "┘"): UP,
    (RIGHT, "┐"): DOWN, (UP, "┐"): LEFT,
    (DOWN, "│"): DOWN, (UP, "│"): UP,
    (DOWN, "└"): RIGHT, (LEFT, "└"): UP,
    (LEFT, "┌"): DOWN, (UP, "┌"): RIGHT,
    (RIGHT, "─"): RIGHT, (LEFT, "─"): LEFT,
}


def parse_input(input_str):
    raw_grid = input_str.translate(BENDS).splitlines()
    extents = cols, rows = len(raw_grid), len(raw_grid[0])
    grid = {V(r, c): raw_grid[r][c] for r, c in product(range(cols), range(rows))}
    for coords, cell in grid.items():
        if cell == "S":
            return grid, coords, extents


def starting_orientation(grid, start):
    for facing in DIRS:
        coords = start + facing
        if (facing, grid[coords]) in STEP:
            return facing


def follow_loop(grid, start):
    delta = starting_orientation(grid, start)
    current = start + delta
    loop = {start: grid[start]}
    while current != start:
        part = grid[current]
        loop[current] = part
        delta = STEP[delta, part]
        current += delta
    return loop


@aoc_timer(1, 10, 2023)
def solve_first(grid, start, _):
    return int(len(follow_loop(grid, start)) / 2)


@aoc_timer(2, 10, 2023)
def solve_second(grid, start, extents):
    loop = follow_loop(grid, start)
    rows, cols = list(range(extents[0])), list(range(extents[1]))
    pipe_strings = ((loop.get((r, c), " ") for c in cols) for r in rows)
    pipe_strings = list(map("".join, pipe_strings))
    crossings_re = re.compile("│|┌─*┘|└─*┐")
    enclosed = 0
    for r, c in product(rows, cols):
        if (r, c) in loop:
            continue
        crossings = crossings_re.findall(pipe_strings[r][:c])
        enclosed += len(crossings) % 2
    return enclosed


if __name__ == "__main__":
    grid, start, extents = parse_input(get_input(10, year=2023))
    solve_first(grid, start, extents)
    solve_second(grid, start, extents)
