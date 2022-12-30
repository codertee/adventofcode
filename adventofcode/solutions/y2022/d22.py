import re
from itertools import starmap
from operator import add

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


class Vector(tuple):

    def __add__(self, other):
        return Vector(starmap(add, zip(self, other)))

    def __mul__(self, obj):
        if isinstance(obj, int):
            return Vector((obj * x for x in self))
        return super().__mul__(obj)


def V(*args):
    return Vector(args)


def parse_input(input_str):
    raw_grid, raw_path = input_str.split("\n\n")
    grid, start = {}, None
    for r, line in enumerate(raw_grid.splitlines()):
        for c, char in enumerate(line):
            if char == " ":
                continue
            elif not start and char == ".":
                start = V(r, c)
            grid[(r, c)] = char
    path = [
        int(instr) if instr.isdigit() else instr
        for instr in re.findall(r"\d+|[LR]", raw_path)
    ]
    return grid, start, path


FACING = (EAST, SOUTH, WEST, NORTH) = V(0, 1), V(1, 0), V(0, -1), V(-1, 0)
TURNS = {
    'L': {EAST: NORTH, NORTH: WEST, WEST: SOUTH, SOUTH: EAST},
    'R': {EAST: SOUTH, SOUTH: WEST, WEST: NORTH, NORTH: EAST},
}


def solve(grid, location, path, wrap):
    direction = EAST
    for instruction in path:
        if instruction in TURNS:
            direction = TURNS[instruction][direction]
        else:
            for _ in range(instruction):
                step = location + direction
                tile = grid.get(step)
                if tile is None:
                    step, tile, newdir = wrap(step, direction)
                    direction = newdir if tile != "#" else direction
                if tile == "#":
                    break
                location = step
    r, c = location + V(1, 1)
    return 1000 * r + 4 * c + FACING.index(direction)


@aoc_timer(1, 22, 2022)
def solve_first(grid, start, path):
    turnaround = {NORTH: SOUTH, EAST: WEST, SOUTH: NORTH, WEST: EAST}

    def wrap(step, direction):
        backward = turnaround[direction]
        while step + backward in grid:
            step += backward
        return step, grid[step], direction

    return solve(grid, start, path, wrap)


@aoc_timer(2, 22, 2022)
def solve_second(grid, start, path):
    PORTALS = {}
    for from_corner, delta, step, to_corner, deltab, stepb, turn in [
        (V(0, 50), EAST, NORTH, V(150, 0), SOUTH, WEST, 1),
        (V(0, 100), EAST, NORTH, V(199, 0), EAST, SOUTH, 0),
        (V(0, 149), SOUTH, EAST, V(149, 99), NORTH, EAST, 2),
        (V(0, 50), SOUTH, WEST, V(149, 0), NORTH, WEST, 2),
        (V(50, 50), SOUTH, WEST, V(100, 0), EAST, NORTH, 3),
        (V(49, 100), EAST, SOUTH, V(50, 99), SOUTH, EAST, 1),
        (V(149, 50), EAST, SOUTH, V(150, 49), SOUTH, EAST, 1)
    ]:
        for i in range(50):
            entrance = from_corner + delta * i
            exit = to_corner + deltab * i
            PORTALS[entrance + step] = exit, turn
            PORTALS[exit + stepb] = entrance, -turn

    def wrap(step, direction):
        newloc, newdir = PORTALS[step]
        curdir = FACING.index(direction)
        return newloc, grid[newloc], FACING[(curdir + newdir) % 4]

    return solve(grid, start, path, wrap)


if __name__ == '__main__':
    grid, start, instr = parse_input(get_input(22, year=2022))
    solve_first(grid, start, instr)
    solve_second(grid, start, instr)
