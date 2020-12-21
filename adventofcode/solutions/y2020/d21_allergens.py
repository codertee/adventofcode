from collections import Counter

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


@aoc_timer(1, 21, 2020)
def solve_first(args):
    can_contain, counts = args
    ingredients = set(counts)
    allergic = set.union(*can_contain.values())
    allergen_free = ingredients - allergic
    return sum(map(counts.get, allergen_free))


@aoc_timer(2, 21, 2020)
def solve_second(args):
    can_contain, _ = args
    allergic = {}
    while len(allergic) != len(can_contain):
        for allergen, ingredients in can_contain.items():
            diff = ingredients - set(allergic)
            if len(diff) == 1:
                allergic[diff.pop()] = allergen
    return ",".join(sorted(allergic, key=lambda ing: allergic[ing]))


def parse_line(line, can_contain=dict(), counts=Counter()):
    ingredients, allergens = line.split(' (contains ')
    ingredients = set(ingredients.split())
    counts += Counter(ingredients)
    for allergen in allergens.rstrip(')').split(', '):
        checked = can_contain.get(allergen, ingredients)
        can_contain[allergen] = checked & ingredients
    return can_contain, counts


def parse_input(input_str):
    return list(map(parse_line, input_str.splitlines())).pop()


if __name__ == '__main__':
    args = parse_input(get_input(21, year=2020))
    solve_first(args)
    solve_second(args)
