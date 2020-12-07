from math import ceil

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


OPTIMIZE = False


def binary_search(seq, low, high, half, instr_low):
    instr = seq.pop()
    half = ceil(half / 2)
    if instr == instr_low:
        high = high - half
    else:
        low = low + half
    if not seq:
        return low if instr == instr_low else high
    return binary_search(seq, low, high, half, instr_low)


def calculate_id(bpass):
    rows, columns = bpass[:7], bpass[7:]
    if OPTIMIZE:
        # 3X faster
        row = int(rows.translate(str.maketrans('FB', '01')), 2)
        col = int(columns.translate(str.maketrans('LR', '01')), 2)
    else:
        row = binary_search(list(reversed(rows)), 0, 127, 127, 'F')
        col = binary_search(list(reversed(columns)), 0, 7, 7, 'L')
    return row * 8 + col


@aoc_timer()
def parse_input(input_str):
    return list(map(calculate_id, input_str.splitlines()))


@aoc_timer(1, 5, 2020)
def solve_first(boarding_ids):
    return max(boarding_ids)


@aoc_timer(2, 5, 2020)
def solve_second(boarding_ids):
    sorted_ids = sorted(boarding_ids)
    for i, boarding_id in enumerate(sorted_ids):
        if sorted_ids[i + 1] - 2 == boarding_id:
            return boarding_id + 1


if __name__ == '__main__':
    boarding_passes = parse_input(get_input(5, year=2020))
    OPTIMIZE = True
    boarding_passes = parse_input(get_input(5, year=2020))
    solve_first(boarding_passes)
    solve_second(boarding_passes)
