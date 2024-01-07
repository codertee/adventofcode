from itertools import starmap
from functools import lru_cache

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_line(line: str):
    record, counts = line.split()
    return record, tuple(map(int, counts.split(",")))


def parse_input(input_str):
    return list(map(parse_line, input_str.splitlines()))


@lru_cache
def solve(record: str, counts: tuple[int]):
    if not record:
        return not counts
    if not counts:
        return "#" not in record
    total, char = 0, record[0]
    if char in ".?":
        total += solve(record[1:], counts)
    c, *rest = counts
    if char not in "#?" or "." in record[:c] or c > len(record):
        return total
    if c == len(record) or record[c] != "#":
        total += solve(record[c + 1:], tuple(rest))
    return total


@aoc_timer(1, 12, 2023)
def solve_first(lines):
    return sum(starmap(solve, lines))


@aoc_timer(2, 12, 2023)
def solve_second(lines):
    solve.cache_clear()
    lines = [("?".join([rec] * 5), counts * 5) for rec, counts in lines]
    return sum(starmap(solve, lines))


if __name__ == "__main__":
    lines = parse_input(get_input(12, year=2023))
    solve_first(lines)
    solve_second(lines)
