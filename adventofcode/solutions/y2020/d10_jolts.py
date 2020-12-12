from collections import defaultdict, Counter
from itertools import starmap
from operator import sub

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    jolts = list(map(int, input_str.splitlines()))
    jolts.extend([0, max(jolts) + 3])
    return sorted(jolts)


@aoc_timer(1, 10, 2020)
def solve_first(jolts):
    counter = Counter(starmap(sub, zip(jolts[1:], jolts)))
    return counter[1] * counter[3]


@aoc_timer(2, 10, 2020)
def solve_second(jolts_lst):
    cache = defaultdict(int, {0: 1})
    for j in jolts_lst[1:]:
        cache[j] = sum(cache[i] for i in range(j - 3, j))
    return cache[jolts_lst[-1]]


if __name__ == '__main__':
    jolts_lst = parse_input(get_input(10, year=2020))
    solve_first(jolts_lst)
    solve_second(jolts_lst)
