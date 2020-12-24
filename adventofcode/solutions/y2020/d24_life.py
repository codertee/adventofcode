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


def neighbours(coords):
    for delta in MOVES.values():
        yield tuple(map(sum, zip(coords, delta)))


@aoc_timer(2, 24, 2020)
def solve_second(tiles):
    for _ in range(100):
        counter = Counter(
            neighbour
            for coords in tiles
            for neighbour in neighbours(coords)
        )
        tiles = set(
            coords
            for coords, nbrs in counter.items()
            if (
                (coords in tiles and not (nbrs == 0 or nbrs > 2)) 
                or (coords not in tiles and nbrs == 2)
            )
        )
    return len(tiles)


def parse_input(input_str):
    tiles = defaultdict(bool)
    regex = re.compile(r'e|se|sw|w|nw|ne')
    for line in input_str.splitlines():
        directions = regex.findall(line)
        position = (0, 0, 0)
        for direction in directions:
            move = MOVES[direction]
            position = tuple(map(sum, zip(position, move)))
        tiles[position] = not tiles[position]
    return set(filter(lambda x: tiles[x], tiles))


if __name__ == '__main__':
    tiles = parse_input(get_input(24, year=2020))
    solve_first(tiles)
    solve_second(tiles)
