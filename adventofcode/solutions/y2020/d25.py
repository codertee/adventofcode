from itertools import count

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def loop(subject, count):
    res = 1
    for _ in range(count):
        res *= subject
        res %= 20201227
    return res


def find_loop(pubkey):
    res = 1
    for i in count(1):
        res *= 7
        res %= 20201227
        if res == pubkey:
            return i


@aoc_timer(1, 25, 2020)
def solve_first(pubkeys):
    card, door = pubkeys
    card_loop = find_loop(card)
    return loop(door, card_loop)


def parse_input(input_str):
    return tuple(map(int, input_str.splitlines()))


if __name__ == '__main__':
    pubkeys = parse_input(get_input(25, year=2020))
    solve_first(pubkeys)
