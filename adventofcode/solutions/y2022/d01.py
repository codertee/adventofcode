from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    return [
        sum(map(int, inventory.split()))
        for inventory in input_str.split('\n\n')
    ]


@aoc_timer(1, 1, 2022)
def solve_first(calories):
    return max(calories)


@aoc_timer(2, 1, 2022)
def solve_second(calories):
    return sum(sorted(calories)[-3:])


if __name__ == '__main__':
    calories = parse_input(get_input(1, year=2022))
    solve_first(calories)
    solve_second(calories)
