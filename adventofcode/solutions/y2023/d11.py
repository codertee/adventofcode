from itertools import starmap, combinations, product

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    grid = input_str.splitlines()
    rows, cols = list(range(len(grid))), list(range(len(grid[0])))
    empty_rows, empty_cols = set(rows), set(cols)
    galaxies = []
    for r, c in product(rows, cols):
        if grid[r][c] == "#":
            empty_cols -= {c}
            empty_rows -= {r}
            galaxies.append((r, c))

    def distance(a, b, expand=1):
        (r1, c1), (r2, c2) = a, b
        rows = len(empty_rows.intersection(range(r1, r2, r2 >= r1 or -1)))
        cols = len(empty_cols.intersection(range(c1, c2, c2 >= c1 or -1)))
        return abs(r1 - r2) + abs(c1 - c2) + rows * expand + cols * expand

    return galaxies, distance


@aoc_timer(1, 11, 2023)
def solve_first(galaxies, distance):
    return sum(starmap(distance, combinations(galaxies, 2)))


@aoc_timer(2, 11, 2023)
def solve_second(galaxies, distance):
    return sum(distance(a, b, 1_000_000) for a, b in combinations(galaxies, 2))


if __name__ == "__main__":
    g, distf = parse_input(get_input(11, year=2023))
    solve_first(g, distf)
    solve_second(g, distf)
