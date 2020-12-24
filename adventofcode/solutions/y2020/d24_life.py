import re
from collections import defaultdict, Counter

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


MOVES = {
    'se': (0, -1, 1), 'e': (1, -1, 0), 'ne': (1, 0, -1),
    'nw': (0, 1, -1), 'w': (-1, 1, 0), 'sw': (-1, 0, 1),
}


@aoc_timer(1, 24, 2020)
def solve_first(tiles):
    return len(tiles)


@aoc_timer(2, 24, 2020)
def solve_second(tiles):
    deltas = tuple(MOVES.values())
    for _ in range(100):
        counter = Counter(
            neighbour(coords, delta)
            for coords in tiles
            for delta in deltas
        )
        tiles = set(
            coords
            for coords, nbrs in counter.items()
            if nbrs == 2 or (nbrs == 1 and coords in tiles)
        )
    return len(tiles)


def neighbour(coords, delta):
    return tuple(map(sum, zip(coords, delta)))


def parse_input(input_str):
    tiles = defaultdict(bool)
    regex = re.compile(r'e|se|sw|w|nw|ne')
    for line in input_str.splitlines():
        position = (0, 0, 0)
        for direction in regex.findall(line):
            position = neighbour(position, MOVES[direction])
        tiles[position] = not tiles[position]
    return set(filter(tiles.get, tiles))


if __name__ == '__main__':
    tiles = parse_input(get_input(24, year=2020))
    solve_first(tiles)
    solve_second(tiles)
