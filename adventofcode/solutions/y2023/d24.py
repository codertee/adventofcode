import re
from collections import namedtuple
from itertools import combinations

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    V = namedtuple("V", ["x", "y", "z"])
    lines = []
    for l in input_str.splitlines():
        numbers = list(map(int, re.findall(r"-?\d+", l)))
        lines.append((V(*numbers[:3]), V(*numbers[3:])))
    return lines


@aoc_timer(1, 24, 2023)
def solve_first(lines):
    total = 0
    start, end = 2e14, 4e14
    for (p1, v1), (p2, v2) in combinations(lines, 2):
        d = v1.x * v2.y - v2.x * v1.y
        if not d:
            continue
        dx, dy = p2.x - p1.x, p2.y - p1.y
        t = (dx * v2.y - dy * v2.x) / d
        u = (dx * v1.y - dy * v1.x) / d
        if t < 0 or u < 0:
            continue
        x = p1.x + t * v1.x
        y = p1.y + t * v1.y
        total += start <= x <= end and start <= y <= end
    return total


def solve(m):
    for i in range(len(m)):
        m[i] = [x / m[i][i] for x in m[i]]
        for j in range(i + 1, len(m)):
            m[j] = [x - m[j][i] * m[i][k] for k, x in enumerate(m[j])]
    for i in range(len(m) -1, 0, -1):
        for j in range(i):
            m[j] = [x - m[j][i] * m[i][k] for k, x in enumerate(m[j])]
    return [r[-1] for r in m]


def create_matrix(lines, f):
    m = [f(p, v) for p, v in lines]
    return [[a - b for a, b in zip(row, m[-1])] for row in m[:4]]


@aoc_timer(2, 24, 2023)
def solve_second(lines):
    m1 = create_matrix(lines, lambda p, v: [-v.y, v.x, p.y, -p.x, p.y * v.x - p.x * v.y])
    m2 = create_matrix(lines, lambda p, v: [-v.y, v.z, p.y, -p.z, p.y * v.z - p.z * v.y])
    x, y = solve(m1)[:2]
    z = solve(m2)[0]
    return int(x + y + z)


if __name__ == "__main__":
    lines = parse_input(get_input(24, year=2023))
    solve_first(lines)
    solve_second(lines)
