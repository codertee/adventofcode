from collections import defaultdict

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_constraint(constraint_str):
    count, color = constraint_str.split(' ', 1)
    color = color.rsplit(' ', 1)[0]
    return color, int(count)


def parse_rule(rule_str):
    color, constraints = rule_str.rstrip('.').split(' bags contain ')
    if constraints.startswith('no'):
        return color, {}
    return color, dict(map(parse_constraint, constraints.split(', ')))


def parse_input(input_str):
    return dict(map(parse_rule, input_str.splitlines()))


def search(target, rules, in_the_bag=set()):
    for color, constraints in rules.items():
        if color in in_the_bag:
            continue
        if target in constraints:
            in_the_bag.add(color)
            search(color, rules)
    return len(in_the_bag)


@aoc_timer(1, 7, 2020)
def solve_first(rules_dct):
    return search('shiny gold', rules_dct)


@aoc_timer(2, 7, 2020)
def solve_second(rules_dct):    
    final_count = 0
    bags_to_check = ['shiny gold']
    while bags_to_check:
        to_check = bags_to_check.pop()
        for color, count in rules_dct[to_check].items():
            final_count += count
            bags_to_check.extend([color] * count)
    return final_count


if __name__ == '__main__':
    rules = parse_input(get_input(7, year=2020))
    solve_first(rules)
    solve_second(rules)
