import re
from functools import partial
from itertools import count
from pprint import pprint

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def validate(low, high, low2, high2, x):
    return (low <= x <= high) or (low2 <= x <= high2)


def parse_rule(rule_str):
    key, ranges = rule_str.split(': ')
    ranges = map(int, re.findall(r'\d+', ranges))
    return key, partial(validate, *ranges)


def parse_ticket(ticket_str):
    return list(map(int, ticket_str.split(',')))


def parse_input(input_str):
    rules, my_ticket, nearby = input_str.split('\n\n')
    rules = list(map(parse_rule, rules.splitlines()))
    nearby = tuple(map(parse_ticket, nearby.splitlines()[1:]))
    my_ticket = parse_ticket(my_ticket.splitlines()[1])
    return rules, my_ticket, nearby


def valid(rules, value):
    for _, in_range in rules:
        if in_range(value):
            break
    else:
        return False
    return True


def invalid_values(rules, ticket):
    return sum(value for value in ticket if not valid(rules, value))


def valid_ticket(rules, ticket):
    return all(valid(rules, value) for value in ticket)


@aoc_timer(1, 16, 2020)
def solve_first(args):
    rules, _, nearby = args
    count = partial(invalid_values, rules)
    return sum(map(count, nearby))


@aoc_timer(2, 16, 2020)
def solve_second(args):
    rules, my_ticket, nearby = args
    nearby = [t for t in nearby if valid_ticket(rules, t)]
    transposed = list(zip(*nearby))
    header_sets = [set() for _ in range(len(transposed))]
    for header, in_range in rules:
        for col, values in enumerate(transposed):
            if all(map(in_range, values)):
                header_sets[col].add(header)
    header_mapping = {}
    while len(header_mapping) != len(transposed):
        for col, headers in enumerate(header_sets):
            if len(headers) != 1:
                continue
            header = headers.pop()
            for headers_ in header_sets:
                headers_.difference_update({header})
            header_mapping[col] = header
    result = 1
    for col, header in header_mapping.items():
        if header.startswith('departure'):
            result *= my_ticket[col]
    return result


if __name__ == '__main__':
    args = parse_input(get_input(16, year=2020))
    solve_first(args)
    solve_second(args)
