from ast import literal_eval
from functools import cmp_to_key
from itertools import chain


from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    return [
        list(map(literal_eval, pair.splitlines()))
        for pair in input_str.split('\n\n')
    ]


def compare(left, right):
    match left, right:
        case int(), int():
            return left - right
        case list(), list():
            for l, r in zip(left, right):
                result = compare(l, r)
                if result != 0:
                    return result
            return len(left) - len(right)
        case list(), int():
            return compare(left, [right])
        case int(), list():
            return compare([left], right)


@aoc_timer(1, 13, 2022)
def solve_first(packets):
    idx_sum = 0
    for i, (left, right) in enumerate(packets, 1):
        if compare(left, right) < 0:
            idx_sum += i
    return idx_sum


@aoc_timer(2, 13, 2022)
def solve_second(packets):
    p1, p2 = [[2]], [[6]]
    packets = list(chain([p1, p2], *packets))
    packets.sort(key=cmp_to_key(compare))
    return (packets.index(p1) + 1) * (packets.index(p2) + 1)


if __name__ == '__main__':
    packets = parse_input(get_input(13, year=2022))
    solve_first(packets)
    solve_second(packets)
