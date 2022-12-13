from collections import deque
from itertools import product

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer

MIN, MAX, START, END = map(ord, 'azSE')


class Square:

    def __init__(self, r, c, lines, grid):
        self.r, self.c = r, c
        self.rows = len(lines)
        self.cols = len(lines[0])
        self.grid = grid
        height = ord(lines[r][c])
        self.start = height == START
        self.end = height == END
        if self.start:
            self.height = MIN
        elif self.end:
            self.height = MAX
        else:
            self.height = height

    def neighbours(self, part):
        for r, c in (-1, 0), (1, 0), (0, 1), (0, -1):
            r, c = self.r + r, self.c + c
            if r < 0 or c < 0 or r >= self.rows or c >= self.cols:
                continue
            other = self.grid[r][c]
            if part == 1:
                neighbour = self.height + 1 >= other.height
            elif part == 2:
                neighbour = self.height - 1 <= other.height
            if neighbour:
                yield other


def parse_input(input_str):
    lines = input_str.splitlines()
    rows, cols = len(lines), len(lines[0])
    grid = [[0] * cols for _ in range(rows)]

    start, end = None, None
    for r, c in product(range(rows), range(cols)):
        s = Square(r, c, lines, grid)
        grid[r][c] = s
        if s.start:
            start = s
        if s.end:
            end = s

    return start, end


def shortest_path(start, part):
    queue = deque(((start, 0),))
    seen = set()
    while queue:
        square, distance = queue.popleft()
        if square in seen:
            continue
        if part == 1 and square.end or part == 2 and square.height == MIN:
            return distance
        seen.add(square)
        for s in square.neighbours(part):
            if s not in seen:
                queue.append((s, distance + 1))


@aoc_timer(1, 12, 2022)
def solve_first(start, _):
    return shortest_path(start, 1)


@aoc_timer(2, 12, 2022)
def solve_second(_, end):
    return shortest_path(end, 2)


if __name__ == '__main__':
    args = parse_input(get_input(12, year=2022))
    solve_first(*args)
    solve_second(*args)
