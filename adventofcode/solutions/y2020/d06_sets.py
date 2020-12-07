from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    groups = input_str.split('\n\n')
    groups = map(str.split, groups)
    return [list(map(set, g)) for g in groups]


def count_uniques(answer_sets):
    unique_answers = set.union(*answer_sets)
    return len(unique_answers)


def count_same(answer_sets):
    same_answers = set.intersection(*answer_sets)
    return len(same_answers)


@aoc_timer(1, 6, 2020)
def solve_first(groups):
    return sum(map(count_uniques, groups))


@aoc_timer(2, 6, 2020)
def solve_second(groups):
    return sum(map(count_same, groups))


if __name__ == '__main__':
    answers = parse_input(get_input(6, year=2020))
    solve_first(answers)
    solve_second(answers)
