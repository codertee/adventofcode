from itertools import starmap
from operator import ne

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    return list(map(str.splitlines, input_str.split("\n\n")))


def symmetric_idx(grid: list[str], allowed_diffs=0):
    for i in range(1, len(grid)):
        up, down = "".join(grid[:i][::-1]), "".join(grid[i:])
        if sum(starmap(ne, zip(up, down))) == allowed_diffs:
            return i
    return 0


def rotate(grid):
    return tuple("".join(c[::-1]) for c in zip(*grid))


@aoc_timer(1, 13, 2023)
def solve_first(grids):
    return sum(symmetric_idx(g) * 100 or symmetric_idx(rotate(g)) for g in grids)


@aoc_timer(2, 13, 2023)
def solve_second(grids):
    return sum(symmetric_idx(g, 1) * 100 or symmetric_idx(rotate(g), 1) for g in grids)


if __name__ == "__main__":
    grids = parse_input(get_input(13, year=2023))
    solve_first(grids)
    solve_second(grids)
