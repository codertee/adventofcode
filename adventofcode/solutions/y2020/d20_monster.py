import re
from math import prod
from itertools import combinations

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer

TOP, BOTTOM, LEFT, RIGHT = range(4)


def flip(grid):
    return tuple(row[::-1] for row in grid)


def rotate(grid):
    return tuple(''.join(c[::-1]) for c in zip(*grid))


class Tile:

    def __init__(self, raw_str):
        name, *grid = raw_str.splitlines()
        self.id = int(re.search(r'\d+', name).group(0))
        self.inner = [line[1:-1] for line in grid[1:-1]]
        self.neighbours = set()

        top, bottom = grid[0], grid[-1]
        left = ''.join(row[0] for row in grid)
        right = ''.join(row[-1] for row in grid)
        self.edges = [top, bottom, left, right]
        self.edge_combinations = set(self.edges + [e[::-1] for e in self.edges])
        self.rotation_count = 0
        self.flipped = False

    def __hash__(self):
        return self.id

    def connection_check(self, other):
        for edge in self.edges:
            if edge in other.edge_combinations:
                self.neighbours.add(other)
                other.neighbours.add(self)
                return True
        return False

    def flip(self):
        top, bottom, left, right = self.edges
        self.edges = [top[::-1], bottom[::-1], right, left]
        self.flipped = not self.flipped

    def rotate(self):
        top, bottom, left, right = self.edges
        self.edges = [left[::-1], right[::-1], bottom, top]
        self.rotation_count += 1 % 4

    def _rotate_match(self, own_edge, target_edge):
        for _ in range(4):
            if self.edges[own_edge] == target_edge:
                return True
            else:
                self.rotate()
        return False

    def aligned(self, other, own_edge, other_edge):
        target_edge = other.edges[other_edge]
        if self._rotate_match(own_edge, target_edge):
            return True
        self.flip()
        if self._rotate_match(own_edge, target_edge):
            return True
        self.flip()
        return False

    def _get_neighbour(self, disconnect, own_edge=RIGHT, other_edge=LEFT):
        for neighbour in self.neighbours:
            if neighbour.aligned(self, other_edge, own_edge):
                if disconnect:
                    neighbour.neighbours.discard(self)
                    self.neighbours.discard(neighbour)
                return neighbour
        return None

    def right_neighbour(self, disconnect=True):
        return self._get_neighbour(disconnect)

    def below_neighbour(self, disconnect=True):
        return self._get_neighbour(disconnect, BOTTOM, TOP)

    def align_inner(self):
        if self.flipped:
            self.inner = flip(self.inner)
        for _ in range(self.rotation_count):
            self.inner = rotate(self.inner)
        return self.inner


@aoc_timer(1, 20, 2020)
def solve_first(corners):
    return prod(tile.id for tile in corners)


MONSTER = [
    '..................#.',
    '#....##....##....###',
    '.#..#..#..#..#..#...',
]

# a) flip the monster to look for more specific match
# b) lookahead to capture overlapping matches
MONSTER_RE1 = re.compile(f'(?=({MONSTER[2]}))')
MONSTER_RE2 = re.compile(MONSTER[1])
MONSTER_RE3 = re.compile(MONSTER[0])


def count_monsters(img):
    count = 0
    for first, second, third in zip(img[:-2], img[1:-1], img[2:]):
        for match in MONSTER_RE1.finditer(first):
            # zero width match due to lookahead searching
            start = match.span()[0]
            end = start + 20
            if (
                MONSTER_RE2.match(second[start:end]) 
                and MONSTER_RE3.match(third[start:end])
            ):
                count += 1
    return count


def top_left(corners):
    for corner in corners:
        for _ in range(4):
            corner.rotate()
            right = corner.right_neighbour(disconnect=False)
            below = corner.below_neighbour(disconnect=False)
            if right and below:
                return corner


@aoc_timer(2, 20, 2020)
def solve_second(corners):
    tile = top_left(corners)
    aligned = []
    while True:
        row = [tile]
        while True:
            if not (tile := tile.right_neighbour()):
                break
            row.append(tile)
        aligned.append(row)        
        if not (tile := row[0].below_neighbour()):
            break

    image = []
    for row in aligned:
        inners_row = tuple(tile.align_inner() for tile in row)
        image.extend(map(''.join, zip(*inners_row)))

    for rotation in range(8):
        if monster_count := count_monsters(image):
            water = sum(row.count('#') for row in image)
            monster = sum(row.count('#') for row in MONSTER)
            return water - monster * monster_count
        if rotation == 4:
            image = flip(image)
        else:
            image = rotate(image)


@aoc_timer()
def parse_input(input_str):
    tiles = tuple(map(Tile, input_str.strip().split('\n\n')))
    for tile_a, tile_b in combinations(tiles, 2):
        tile_a.connection_check(tile_b)
    corners = filter(lambda t: len(t.neighbours) == 2,  tiles)
    return tuple(corners)


if __name__ == '__main__':
    corners = parse_input(get_input(20, year=2020))
    solve_first(corners)
    solve_second(corners)
