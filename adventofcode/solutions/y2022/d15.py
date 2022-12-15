import re
from math import inf

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    sensors = []
    for line in input_str.splitlines():
        x, y, bx, by = map(int, re.findall(r'(-?\d+)', line))
        r = abs(x - bx) + abs(y - by)
        sensors.append((x, y, r))
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


def solve(sensors, y):
    ranges = []
    for sx, sy, r in sensors:
        dy = abs(y - sy)
        if dy > r:
            continue
        dx = r - dy
        ranges.append((sx - dx, sx + dx))
    ranges.sort()
    min_x, max_x = ranges[0]
    for x1, x2 in ranges[1:]:
        min_test = min_x - 1
        if x1 < min_test and x2 < min_test:
            return min_test
        max_test = max_x + 1
        if x1 > max_test and x2 > max_test:
            return max_test
        min_x = min(x1, min_x)
        max_x = max(x2, max_x)
    return False


@aoc_timer(2, 15, 2022)
def solve_second(sensors):
    for y in range(4_000_000):
        if x := solve(sensors, y):
            return x * 4_000_000 + y


if __name__ == '__main__':
    sensors = parse_input(get_input(15, year=2022))
    solve_first(sensors)
    solve_second(sensors)
