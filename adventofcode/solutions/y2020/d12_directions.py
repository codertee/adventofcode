import re

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


EAST, NORTH, WEST, SOUTH = 'ENWS'
LEFT, RIGHT, FORWARD = 'LRF'

DELTAS = {
    EAST: (1, 0),
    NORTH: (0, 1),
    WEST: (-1, 0),
    SOUTH: (0, -1)
}

TURNS = {
    LEFT: {EAST: NORTH, NORTH: WEST, WEST: SOUTH, SOUTH: EAST},
    RIGHT: {EAST: SOUTH, SOUTH: WEST, WEST: NORTH, NORTH: EAST}
}


def parse_input(input_str):
    str_pairs = re.findall(r'(\w)(\d+)', input_str)
    return [(d, int(n)) for d, n in str_pairs]


def move(x, y, n, direction):
    dx, dy = DELTAS[direction]
    return x + n * dx, y + n * dy


@aoc_timer(1, 12, 2020)
def solve_first(nav_list):
    x, y = 0, 0
    facing = EAST
    for instr, arg in nav_list:
        if instr in {LEFT, RIGHT}:
            for _ in range(arg // 90):
                facing = TURNS[instr][facing]
        elif instr == FORWARD:
            x, y = move(x, y, arg, facing)
        else:
            x, y = move(x, y, arg, instr)
    return abs(x) + abs(y)


@aoc_timer(2, 12, 2020)
def solve_second(nav_list):
    sx, sy = 0, 0
    wx, wy = 10, 1
    for instr, arg in nav_list:
        if (instr, arg) in {(LEFT, 90), (RIGHT, 270)}:
            wx, wy = -wy, wx
        elif (instr, arg) in {(LEFT, 180), (RIGHT, 180)}:
            wx, wy = -wx, -wy
        elif (instr, arg) in {(LEFT, 270), (RIGHT, 90)}:
            wx, wy = wy, -wx
        elif instr == FORWARD:
            sx += wx * arg
            sy += wy * arg
        else:
            wx, wy = move(wx, wy, arg, instr)
    return abs(sx) + abs(sy)


if __name__ == '__main__':
    nav_list = parse_input(get_input(12, year=2020))
    solve_first(nav_list)
    solve_second(nav_list)
