import re
from collections import defaultdict
from itertools import starmap
from math import prod

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_line(line):
    game = defaultdict(int)
    for amt, color in re.findall(r"(\d+) (\w+)", line):
        game[color] = max(int(amt), game[color])
    return game


def parse_input(input_str):
    """parses input according to part 2, which also works for part 1"""
    return list(map(parse_line, input_str.splitlines()))


def check(g_id, game):
    if game["red"] > 12 or game["green"] > 13 or game["blue"] > 14:
        return 0
    return g_id


@aoc_timer(1, 2, 2023)
def solve_first(games: list[dict[int]]):
    return sum(starmap(check, enumerate(games, start=1)))


@aoc_timer(2, 2, 2023)
def solve_second(games: list[dict[int]]):
    return sum(map(lambda g: prod(g.values()), games))


if __name__ == "__main__":
    games = parse_input(get_input(2, year=2023))
    solve_first(games)
    solve_second(games)
