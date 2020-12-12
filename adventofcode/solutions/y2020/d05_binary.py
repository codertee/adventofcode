from itertools import count

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def calculate_id(bitstring):
    row = int(bitstring[:7], 2)
    col = int(bitstring[7:], 2)
    return row * 8 + col


def parse_input(input_str):
    char_table = str.maketrans('FBLR', '0101')
    bitstrings = input_str.translate(char_table).splitlines()
    return list(map(calculate_id, bitstrings))


@aoc_timer(1, 5, 2020)
def solve_first(boarding_ids):
    return max(boarding_ids)


@aoc_timer(2, 5, 2020)
def solve_second(boarding_ids):
    id_set = set(boarding_ids)
    for boarding_id in count(min(boarding_ids)):
        if boarding_id not in id_set:
            return boarding_id


if __name__ == '__main__':
    boarding_passes = parse_input(get_input(5, year=2020))
    solve_first(boarding_passes)
    solve_second(boarding_passes)
