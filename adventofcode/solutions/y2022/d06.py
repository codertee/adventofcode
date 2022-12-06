from itertools import count
from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    return input_str


def find_packet(stream, N):
    for i in count():
        if len(set(stream[i: i + N])) == N:
            return i + N


@aoc_timer(1, 6, 2022)
def solve_first(stream):
    return find_packet(stream, 4)


@aoc_timer(2, 6, 2022)
def solve_second(stream):
    return find_packet(stream, 14)


if __name__ == '__main__':
    stream = parse_input(get_input(6, year=2022))
    solve_first(stream)
    solve_second(stream)
