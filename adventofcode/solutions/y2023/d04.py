import re
from collections import Counter

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


LINE_GROUPS = re.compile(r"Card +(\d+): +(.*?) \| +(.*?)$")


def parse_line(line: str):
    card, winning, have = LINE_GROUPS.match(line).groups()
    matches = set(winning.split()) & set(have.split())
    return int(card), len(matches)


def parse_input(input_str):
    return dict(map(parse_line, input_str.splitlines()))


@aoc_timer(1, 4, 2023)
def solve_first(cards: dict[int, int]):
    return sum(2 ** (m - 1) for m in cards.values() if m)


@aoc_timer(2, 4, 2023)
def solve_second(cards: dict[int, int]):
    accounts = Counter(cards.keys())
    for original, matches in cards.items():
        for below in range(original, original + matches):
            accounts[below + 1] += accounts[original]
    return accounts.total()


if __name__ == '__main__':
    pairs = parse_input(get_input(4, year=2023))
    solve_first(pairs)
    solve_second(pairs)
