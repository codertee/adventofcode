from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def match(rules, rule, msg):
    leaf_rule, string_end = rule == [], msg == ''
    if leaf_rule or string_end:
        return leaf_rule and string_end
    target, rest = rule[0], rule[1:]
    current = rules[target]
    if isinstance(current, str):
        return msg[0] == current and match(rules, rest, msg[1:])
    else:
        return any(match(rules, rule + rest, msg) for rule in current)


@aoc_timer(1, 19, 2020)
def solve_first(args):
    rules, messages = args
    return sum(match(rules, ['0'], msg) for msg in messages)


@aoc_timer(2, 19, 2020)
def solve_second(args):
    rules, messages = args
    rules['8'] = [['42'], ['42', '8']]
    rules['11'] = [['42', '31'], ['42', '11', '31']]
    return sum(match(rules, ['0'], msg) for msg in messages)


def parse_rule(line):
    key, val = line.split(': ')
    if val in {'"a"', '"b"'}:
        return key, val.strip('"')
    return key, [pair.split() for pair in val.split(' | ')]


def parse_input(input_str):
    rules_str, messages = input_str.split('\n\n')
    rules = dict(map(parse_rule, rules_str.splitlines()))
    return rules, messages.splitlines()


if __name__ == '__main__':
    args = parse_input(get_input(19, year=2020))
    solve_first(args)
    solve_second(args)
