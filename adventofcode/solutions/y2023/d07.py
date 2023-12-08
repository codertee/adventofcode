from collections import Counter

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_line(line: str):
    hand, bid = line.split()
    return hand, int(bid)


def parse_input(input_str):
    table = str.maketrans("AKQJT", "EDCBA")
    lines = input_str.translate(table).splitlines()
    return list(map(parse_line, lines))


JOKER = "1"


def keyfun(item):
    hand = item[0]
    counter = dict(Counter(hand).most_common())
    counts = list(counter.values())
    if JOKER not in counter:
        return counts, hand
    if hand == JOKER * 5:
        return [5], hand
    jokers = counter[JOKER]
    counts.remove(jokers)
    counts[0] += jokers
    return counts, hand


def solve(game):
    bids = (bid for _, bid in sorted(game, key=keyfun))
    return sum(rank * bid for rank, bid in enumerate(bids, 1))


@aoc_timer(1, 7, 2023)
def solve_first(game):
    return solve(game)


@aoc_timer(2, 7, 2023)
def solve_second(game):
    return solve(((hand.replace('B', JOKER), bid) for hand, bid in game))


if __name__ == "__main__":
    game = parse_input(get_input(7, year=2023))
    solve_first(game)
    solve_second(game)
