from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


CHARMAP = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}


def parse_input(input_str):
    return tuple(map(list, input_str.splitlines()))


def decimal(snafu: list[str]):
    if not snafu:
        return 0
    last = snafu.pop()
    return 5 * decimal(snafu) + CHARMAP[last]


def snafu(dec: int):
    if not dec:
        return ''
    q, r = divmod(dec + 2, 5)
    return snafu(q) + '=-012'[r]


@aoc_timer(1, 25, 2022)
def solve_first(snafus):
    return snafu(sum(map(decimal, snafus)))


if __name__ == '__main__':
    snafus = parse_input(get_input(25, year=2022))
    solve_first(snafus)
