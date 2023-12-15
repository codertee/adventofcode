from functools import lru_cache
from itertools import count

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    return tuple(input_str.splitlines())


@lru_cache(maxsize=None)
def shift_line(line: str):
    return "#".join("".join(sorted(substr)) for substr in line.split("#"))


def shift_grid(grid):
    return tuple(map(shift_line, grid))


def rotate(grid):
    return tuple("".join(c[::-1]) for c in zip(*grid))


def calculate_load(grid: tuple[str]):
    return sum((len(grid) - i) * line.count("O") for i, line in enumerate(grid))


@aoc_timer(1, 14, 2023)
def solve_first(grid):
    return calculate_load(rotate(rotate(rotate(shift_grid(rotate(grid))))))


@aoc_timer(2, 14, 2023)
def solve_second(grid):
    seen = {}
    for i in count():       
        for _ in range(4):
            grid = shift_grid(rotate(grid))
        if grid in seen:
            interval = seen[grid] - i
            idx = (1000000000 - i) % interval + i
            return calculate_load(list(seen.keys())[idx - 1])
        seen[grid] = i


if __name__ == "__main__":
    grid = parse_input(get_input(14, year=2023))
    solve_first(grid)
    solve_second(grid)
