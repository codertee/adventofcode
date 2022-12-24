from collections import defaultdict, deque
from itertools import count, product, starmap
from operator import add

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


class Vector(tuple):
    def __add__(self, other):
        return Vector(starmap(add, zip(self, other)))


def V(*args):
    return Vector(args)


DIRS = N, S, W, E, NE, NW, SE, SW = (
    V(-1, 0), V(1, 0), V(0, -1), V(0, 1),
    V(-1, 1), V(-1, -1), V(1, 1), V(1, -1)
)
CHECK = deque([(N, NE, NW), (S, SE, SW), (W, NW, SW), (E, NE, SE)])


def parse_input(input_str):
    elves = set()
    for r, line in enumerate(input_str.splitlines()):
        for c, tile in enumerate(line):
            if tile == '#':
                elves.add(V(r, c))
    return elves


def simulate(elves, checks):
    moved = False
    proposals = defaultdict(list)
    for elf in elves:
        if all(elf + d not in elves for d in DIRS):
            continue
        for left, mid, right in checks:
            the_spot = elf + left
            check = the_spot, elf + mid, elf + right
            if all(spot not in elves for spot in check):
                proposals[the_spot].append(elf)
                break
    for where, who in proposals.items():
        if len(who) > 1:
            continue
        moved = True
        elves.add(where)
        elves.remove(who.pop())
    return moved


@aoc_timer(1, 23, 2022)
def solve_first(elves):
    elves = elves.copy()
    checks = CHECK.copy()
    for _ in range(10):
        simulate(elves, checks)
        checks.rotate(-1)
    rows = [e[0] for e in elves]
    cols = [e[1] for e in elves]
    min_r, max_r = min(rows), max(rows) + 1
    min_c, max_c = min(cols), max(cols) + 1
    return (max_r - min_r) * (max_c - min_c) - len(elves)


@aoc_timer(2, 23, 2022)
def solve_second(elves):
    checks = CHECK.copy()
    for i in count(1):
        if not simulate(elves, checks):
            return i
        checks.rotate(-1)


if __name__ == '__main__':
    elves = parse_input(get_input(23, year=2022))
    solve_first(elves)
    solve_second(elves)
