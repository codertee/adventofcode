import re
from collections import namedtuple
from itertools import combinations, product
from math import inf

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


Sensor = namedtuple('Sensor', ['x', 'y', 'radius'])


def parse_input(input_str):
    sensors = []
    for line in input_str.splitlines():
        x, y, bx, by = map(int, re.findall(r'(-?\d+)', line))
        r = abs(x - bx) + abs(y - by)
        sensors.append(Sensor(x, y, r))
    return sensors


@aoc_timer(1, 15, 2022)
def solve_first(sensors):
    # assuming no beacons or signal gaps on y = 2_000_000
    min_x, max_x = inf, -inf
    for x, y, r in sensors:
        dy = abs(2_000_000 - y)
        if dy > r:
            continue
        dx = r - dy
        min_x = min(x - dx, min_x)
        max_x = max(x + dx, max_x)
    return max_x - min_x


def distance(one, other):
    return abs(one.x - other.x) + abs(one.y - other.y)


@aoc_timer(2, 15, 2022)
def solve_second(sensors):
    one_away = []
    a_coeffs, b_coeffs = set(), set()
    for one, other in combinations(sensors, 2):
        if distance(one, other) == one.radius + other.radius + 2:
            one_away += [one, other]
            for x, y, r in one, other:
                a_coeffs.add(y - x + r + 1)
                a_coeffs.add(y - x - r - 1)
                b_coeffs.add(x + y + r + 1)
                b_coeffs.add(x + y - r - 1)
    for a, b in product(a_coeffs, b_coeffs):
        x = (b - a) // 2
        y = (a + b) // 2
        test = Sensor(x, y, 0)
        if all(
            distance(test, other) == other.radius + 1 
            for other in one_away
        ):
            return x * 4_000_000 + y


if __name__ == '__main__':
    sensors = parse_input(get_input(15, year=2022))
    solve_first(sensors)
    solve_second(sensors)
