from math import inf

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    return set(
        tuple(map(int, line.split(',')))
        for line in input_str.splitlines()
    )


def neighbours(coords):
    x, y, z = coords
    for dx, dy, dz in (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1):
        yield x + dx, y + dy, z + dz


@aoc_timer(1, 18, 2022)
def solve_first(cubes):
    area = len(cubes) * 6
    for c in cubes:
        for n in neighbours(c):
            area -= n in cubes
    return area


class Bounds:

    def __init__(self, cubes):
        mins = inf, inf, inf
        maxs = 0, 0, 0
        for c in cubes:
            mins = tuple(map(min, zip(c, mins)))
            maxs = tuple(map(max, zip(c, maxs)))
        self.ranges = [set(range(lo - 1, hi + 2)) for lo, hi in zip(mins, maxs)]
        self.mins = mins
    
    def __contains__(self, coords):
        for c, _range in zip(coords, self.ranges):
            if c not in _range:
                return False
        return True


@aoc_timer(2, 18, 2022)
def solve_second(cubes):
    bounds = Bounds(cubes)
    q = [bounds.mins]
    seen = {bounds.mins}
    area = 0
    while q:
        coords = q.pop()
        for n in neighbours(coords):
            if n in seen or n not in bounds:
                continue
            if n in cubes:
                area += 1
            else:
                seen.add(n)
                q.append(n)
    return area


if __name__ == '__main__':
    cubes = parse_input(get_input(18, year=2022))
    solve_first(cubes)
    solve_second(cubes)
