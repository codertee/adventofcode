import heapq
from collections import defaultdict
from itertools import product
from math import inf

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


RIGHT, DOWN, LEFT, UP = (0, 1), (1, 0), (0, -1), (-1, 0)
STEPS = {
    UP: [UP, RIGHT, LEFT], DOWN: [DOWN, LEFT, RIGHT],
    LEFT: [LEFT, UP, DOWN], RIGHT: [RIGHT, DOWN, UP],
    None: [RIGHT, DOWN]
}


def parse_input(input_str):
    str_grid = input_str.splitlines()
    rows, cols = len(str_grid), len(str_grid[0])
    grid = {}
    for r, c in product(range(rows), range(cols)):
        grid[(r, c)] = int(str_grid[r][c])
    return grid, (rows - 1, cols - 1)


def solve(grid, end, forward_check):
    q = [((0, 0), None, 0, 0)]
    heapq.heapify(q)
    best_heat, final_heat = defaultdict(lambda: inf), inf
    while q:
        (r, c), direction, heat, fwd = heapq.heappop(q)
        if (r, c) == end:
            final_heat = min(final_heat, heat); continue
        for dr, dc in STEPS[direction]:
            pushed = forward_check(direction, (dr, dc), fwd)
            if not pushed:
                continue
            nr, nc = r + dr, c + dc
            if (nr, nc) not in grid:
                continue
            nxt_heat = heat + grid[nr, nc]
            if nxt_heat >= best_heat[nr, nc, dr, dc, pushed]:
                continue
            best_heat[nr, nc, dr, dc, pushed] = nxt_heat
            heapq.heappush(q, ((nr, nc), (dr, dc), nxt_heat, pushed))
    return final_heat


def forward_count(direction, step, count):
    pushed = count + 1 if step == direction else 1
    if pushed == 4:
        return 0
    return pushed


@aoc_timer(1, 17, 2023)
def solve_first(grid, end):
    return solve(grid, end, forward_count)


def forward_check(direction, step, count):
    if direction and direction != step and count < 4:
        return 0
    pushed = count + 1 if step == direction else 1
    if pushed == 11:
        return 0
    return pushed


@aoc_timer(2, 17, 2023)
def solve_second(grid, end):
    return solve(grid, end, forward_check)


if __name__ == "__main__":
    grid, end = parse_input(get_input(17, year=2023))
    solve_first(grid, end)
    solve_second(grid, end)
