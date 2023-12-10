from functools import reduce
from itertools import pairwise
from operator import itemgetter

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_line(line: str):
    return list(map(int, line.split()))


def parse_input(input_str):
    return list(map(parse_line, input_str.splitlines()))


def predict(history: list[int]):
    prediction = history[-1]
    while any(history):
        history = [other - one for one, other in pairwise(history)]
        prediction += history[-1]
    return prediction


@aoc_timer(1, 9, 2023)
def solve_first(histories):
    return sum(map(predict, histories))


@aoc_timer(2, 9, 2023)
def solve_second(histories):
    return sum(predict(h[::-1]) for h in histories)


if __name__ == "__main__":
    histories = parse_input(get_input(9, year=2023))
    solve_first(histories)
    solve_second(histories)
