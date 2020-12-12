from itertools import combinations, accumulate

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    return list(map(int, input_str.splitlines()))


def find_error(encrypted_ints):
    for i, coded_int in enumerate(encrypted_ints[25:]):
        preamble = encrypted_ints[i: i + 25]
        for x, y in combinations(preamble, 2):
            if x + y == coded_int:
                break
        else:
            return coded_int, i


@aoc_timer(1, 9, 2020)
def solve_first(encrypted_data):
    return find_error(encrypted_data)[0]


@aoc_timer(2, 9, 2020)
def solve_second(encrypted_ints):
    target_int, limit = find_error(encrypted_ints)
    for i, _ in enumerate(encrypted_ints[:limit]):
        sum_iterator = accumulate(encrypted_ints[i:])
        for j, running_sum  in enumerate(sum_iterator):
            if running_sum == target_int:
                return i + encrypted_ints[i + j]
            if running_sum > target_int:
                break


if __name__ == '__main__':
    encrypted_ints = parse_input(get_input(9, year=2020))
    solve_first(encrypted_ints)
    solve_second(encrypted_ints)
