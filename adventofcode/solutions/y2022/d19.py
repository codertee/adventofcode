import re
from functools import partial
from itertools import starmap
from math import prod
from multiprocessing import Pool
from operator import add, sub, ge

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


class Array(list):
    def __add__(self, other):
        return Array(starmap(add, zip(self, other)))

    def __sub__(self, other):
        return Array(starmap(sub, zip(self, other)))

    def __ge__(self, other):
        return Array(starmap(ge, zip(self, other)))


def A(*args):
    return Array(args)


def parse_input(input_str):
    blueprints = []
    for line in input_str.splitlines():
        _, oo, oc, oob, co, og, obg = list(map(int, re.findall(r'\d+', line)))
        blueprints.append((
            # resource order: geoede, obsidian, clay, ore
            # cost               resource type
            (A(0, 0,   0,  oo ), A(0, 0, 0, 1)),
            (A(0, 0,   0,  oc ), A(0, 0, 1, 0)),
            (A(0, 0,   co, oob), A(0, 1, 0, 0)),
            (A(0, obg, 0,  og ), A(1, 0, 0, 0)),
            (A(0, 0,   0,  0  ), A(0, 0, 0, 0))
        )) 
    return blueprints


def key(step):
    inventory, robots = step
    return inventory + robots


def solve(minutes, blueprint):
    q = [(A(0, 0, 0, 0), A(0, 0, 0, 1))]
    for _ in range(minutes):
        choices = []
        for resources, robots in q:
            for cost, resource_type in blueprint:
                if all(resources >= cost):
                    choices.append(
                        (resources + robots - cost, robots + resource_type))
        q = sorted(choices, key=key)[-999:]
    resources, _ = q[-1]
    return resources[0]


@aoc_timer(1, 19, 2022)
def solve_first(blueprints):
    with Pool() as p:
        worker = partial(solve, 24)
        geodes = p.map(worker, blueprints)
        return sum(i * g for i, g in enumerate(geodes, 1))


@aoc_timer(2, 19, 2022)
def solve_second(blueprints):
    with Pool() as p:
        worker = partial(solve, 32)
        return prod(p.map(worker, blueprints[:3]))


if __name__ == '__main__':
    blueprints = parse_input(get_input(19, year=2022))
    solve_first(blueprints)
    solve_second(blueprints)
