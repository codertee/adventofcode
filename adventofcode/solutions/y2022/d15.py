import re
from collections import namedtuple
from itertools import combinations
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


def sign(a, b):
    return (a > b) - (a < b)


def distance(one, other):
    return abs(one.x - other.x) + abs(one.y - other.y)


@aoc_timer(2, 15, 2022)
def solve_second(sensors):
    one_away = []
    for one, other in combinations(sensors, 2):
        if distance(one, other) == one.radius + other.radius + 2:
            one_away += [one, other]
    (x1, y1, r1), (x2, y2, _) = one_away[:2]
    dx = sign(x1, x2)
    dy = -sign(y1, y2)
    x, y = x1 - dx * (r1 + 1), y1
    for _ in range(r1 + 2):
        test = Sensor(x, y, 0)
        if all(
            distance(test, other) == other.radius + 1 
            for other in one_away
        ):
            return x * 4_000_000 + y
        x += dx
        y += dy
    return "edge cases not handled"


if __name__ == '__main__':
    sensors = parse_input(get_input(15, year=2022))
    solve_first(sensors)
    solve_second(sensors)
