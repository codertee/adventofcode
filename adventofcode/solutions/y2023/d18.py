from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


DIRS = RIGHT, DOWN, LEFT, UP = (0, 1), (1, 0), (0, -1), (-1, 0)
STEPS = {"R": RIGHT, "L": LEFT, "U": UP, "D": DOWN}


def parse_input(input_str):
    return input_str.splitlines()


def solve(lines: list[str], parse):
    r, c = 0, 0
    path, area = 0, 0
    for line in lines:
        (dr, dc), steps = parse(line)
        path += steps
        nr, nc = r + steps * dr, c + steps * dc
        area += r * nc - c * nr
        r, c = nr, nc
    return abs(area // 2) + path // 2 + 1


def parse_first(line: str):
    direction, amount, _ = line.split()
    return STEPS[direction], int(amount)


@aoc_timer(1, 18, 2023)
def solve_first(lines):
    return solve(lines, parse_first)


def parse_second(line: str):
    *_, instr = line.split()
    return DIRS[int(instr[7])], int(instr[2:7], 16)


@aoc_timer(2, 18, 2023)
def solve_second(lines):
    return solve(lines, parse_second)


if __name__ == "__main__":
    lines = parse_input(get_input(18, year=2023))
    solve_first(lines)
    solve_second(lines)
