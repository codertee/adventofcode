from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_policy(policy_str):
    policy, password = policy_str.split(": ")
    counts, letter = policy.split()
    first, second = counts.split('-')
    return first, second, letter, password


def parse_input(input_str):
    return list(map(parse_policy, input_str.splitlines()))


def valid_count(policy):
    count_low, count_high, letter, password = policy
    return int(count_low) <= password.count(letter) <= int(count_high)


@aoc_timer(1, 2, 2020)
def solve_first(policies):
    return sum(map(valid_count, policies))


def valid_position(policy):
    pos1, pos2, letter, password = policy
    char1 = password[int(pos1) - 1]
    char2 = password[int(pos2) - 1]
    return [char1, char2].count(letter) == 1


@aoc_timer(2, 2, 2020)
def solve_second(policies):
    return sum(map(valid_position, policies))


if __name__ == '__main__':
    policies = parse_input(get_input(2, year=2020))
    solve_first(policies)
    solve_second(policies)
