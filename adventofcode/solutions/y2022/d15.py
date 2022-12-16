import re
from functools import partial
from itertools import combinations
from math import inf
from multiprocessing import Pool

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
    if len(ranges) < 4:
        return
    ranges.sort()
    prev_x2 = ranges[0][1]
    for x1, x2 in ranges[1:]:
        if x1 > prev_x2:
            return prev_x2 + 1, y
        prev_x2 = max(x2, prev_x2)
    return False


@aoc_timer(2, 15, 2022)
def solve_second(sensors):
    filtered_sensors = []
    for one, other in combinations(sensors, 2):
        (x1, y1, r1), (x2, y2, r2) = one, other
        if abs(x1 - x2) + abs(y1 - y2) == r1 + r2 + 2:
            filtered_sensors.extend([one, other])
    filtered_sensors.sort(key=lambda x: x[2])
    min_y, max_y = 4_000_000, 0
    for _, y, _ in sensors:
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    with Pool() as p:
        results = p.map(partial(solve, filtered_sensors), range(min_y, max_y))
        x, y = next(filter(bool, results))
        return x * 4_000_000 + y


if __name__ == '__main__':
    sensors = parse_input(get_input(15, year=2022))
    solve_first(sensors)
    solve_second(sensors)
