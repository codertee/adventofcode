from collections import deque
from itertools import product, chain

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


class Square:

    def __init__(self, r, c, lines):
        self.r, self.c = r, c
        self.rows = len(lines)
        self.cols = len(lines[0])
        self.linked = []
        height = ord(lines[r][c])
        self.start = height == ord('S')
        self.end = height == ord('E')
        if self.start:
            self.height = ord('a')
        elif self.end:
            self.height = ord('z')
        else:
            self.height = height

    def link(self, grid, condition):
        self.linked = []
        for r, c in (-1, 0), (1, 0), (0, 1), (0, -1):
            r, c = self.r + r, self.c + c
            if r < 0 or c < 0 or r >= self.rows or c >= self.cols:
                continue
            other = grid[r][c]
            if condition(self.height, other.height):
                self.linked.append(other)


def parse_input(input_str):
    lines = input_str.splitlines()
    rows, cols = len(lines), len(lines[0])
    grid = [[None] * cols for _ in range(rows)]

    start, end = None, None
    for r, c in product(range(rows), range(cols)):
        s = Square(r, c, lines)
        grid[r][c] = s
        if s.start:
            start = s
        if s.end:
            end = s

    return start, end, grid


def shortest_path(start, end_condition):
    queue = deque(((start, 0),))
    seen = set()
    while queue:
        square, distance = queue.popleft()
        if end_condition(square):
            return distance
        if square in seen:
            continue
        seen.add(square)
        for s in square.linked:
            if s not in seen:
                queue.append((s, distance + 1))


@aoc_timer(1, 12, 2022)
def solve_first(start, _, grid):
    for square in chain(*grid):
        square.link(grid, lambda one, other: one + 1 >= other)
    return shortest_path(start, lambda x: x.end)


@aoc_timer(2, 12, 2022)
def solve_second(_, end, grid):
    for square in chain(*grid):
        square.link(grid, lambda one, other: one - 1 <= other)
    minimum = ord('a')
    return shortest_path(end, lambda x: x.height == minimum)


if __name__ == '__main__':
    args = parse_input(get_input(12, year=2022))
    solve_first(*args)
    solve_second(*args)
