from collections import deque
from itertools import product
from math import ceil

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    str_grid = input_str.splitlines()
    rows, cols = len(str_grid), len(str_grid[0])
    blocked, start = set(), None
    for r, c in product(range(rows), range(cols)):
        match str_grid[r][c]:
            case "#":
                blocked.add((r, c))
            case "S":
                start = r, c
    return blocked, start, rows


@aoc_timer(1, 21, 2023)
def solve_first(blocked: set[tuple[int, int]], start: tuple[int, int], _):
    q = deque([(start, 0)])
    reached = 0
    seen = {start}
    while 1:
        (r, c), walked = q.popleft()
        if walked == 64:
            return reached + 1
        for dr, dc in (0, 1), (1, 0), (0, -1), (-1, 0):
            nxt = r + dr, c + dc
            if nxt in seen or nxt in blocked:
                continue
            reached += walked % 2
            seen.add(nxt)
            q.append((nxt, walked + 1))


@aoc_timer(2, 21, 2023)
def solve_second(blocked: set[tuple[int, int]], start: tuple[int, int], grid_size: int):
    q = deque([(start, 0)])
    odds, evens = 1, 0
    seen = {start}
    rem = 26501365 % grid_size
    stops = [rem, rem + grid_size, rem + 2 * grid_size]

    while 1:
        (r, c), steps = q.popleft()
        odd = steps % 2
        reached = evens if odd else odds
        if steps == stops[0]:
            stops[0] = reached
        elif steps == stops[1]:
            stops[1] = reached
        elif steps == stops[2]:
            stops[2] = reached
            break
        for dr, dc in (0, 1), (1, 0), (0, -1), (-1, 0):
            nxt = nr, nc = r + dr, c + dc 
            if nxt in seen or (nr % grid_size, nc % grid_size) in blocked:
                continue
            seen.add(nxt)
            q.append((nxt, steps + 1))
            odds += odd
            evens += not odd

    first = stops[1] - stops[0]
    second = stops[2] - stops[1] - first
    a = second // 2
    b = first - 3 * a
    c = stops[0] - b - a
    n = ceil(26501365 / grid_size)
    return a * n ** 2 + b * n + c


if __name__ == "__main__":
    args = parse_input(get_input(21, year=2023))
    solve_first(*args)
    solve_second(*args)
