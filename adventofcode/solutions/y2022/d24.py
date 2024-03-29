from collections import deque

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


class Blizzards:

    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def traversable(self, state):
        r, c, t = state
        return (
            0 <= r < self.rows and 0 <= c < self.cols and
            self.grid[(r + t) % self.rows][c] != '^' and
            self.grid[(r - t) % self.rows][c] != 'v' and
            self.grid[r][(c + t) % self.cols] != '<' and
            self.grid[r][(c - t) % self.cols] != '>'
        )


def parse_input(input_str):
    grid = [line[1:-1] for line in input_str.splitlines()[1:-1]]
    blizzards = Blizzards(grid)
    start = 0, 0
    end = blizzards.rows - 1, blizzards.cols - 1
    return blizzards, start, end


def solve(blizzards, start, end, t=0):
    q, seen = deque([(*start, t)]), set()
    while True:
        r, c, t = q.popleft()
        if (r, c, t) in seen:
            continue
        if (r, c) == end:
            return t + 1
        seen.add((r, c, t))
        for dr, dc in (-1, 0), (0, 1), (1, 0), (0, -1), (0, 0):
            state = r + dr, c + dc, t + 1
            if blizzards.traversable(state):
                q.append(state)
        if not q:
            q.append((*start, t + 1))


@aoc_timer(1, 24, 2022)
def solve_first(blizzards, start, end):
    return solve(blizzards, start, end)


@aoc_timer(2, 24, 2022)
def solve_second(blizzards, start, end):
    split = solve(blizzards, start, end)
    split = solve(blizzards, end, start, t=split)
    return solve(blizzards, start, end, t=split)


if __name__ == '__main__':
    blizzards, start, end = parse_input(get_input(24, year=2022))
    solve_first(blizzards, start, end)
    solve_second(blizzards, start, end)
