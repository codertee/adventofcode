from collections import Counter
from itertools import product

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def neighbour_set(coords):
    neighbours = ((c + 1, c, c - 1) for c in coords)
    neighbours = set(product(*neighbours))
    neighbours.remove(coords)
    return neighbours


def solve(initial_state, N):
    pocket_length = len(initial_state)
    zeroes = [0] * (N - 2)
    pocket = set(
        (x, y, *zeroes)
        for x, y in product(range(pocket_length), repeat=2)
        if initial_state[x][y] == '#'
    )
    for _ in range(6):
        counter = Counter(
            neighbour
            for coords in pocket
            for neighbour in neighbour_set(coords)
        )
        pocket = set(
            coords
            for coords, active in counter.items()
            if (active == 2 and coords in pocket) or active == 3
        )
    return len(pocket)


@aoc_timer(1, 17, 2020)
def solve_first(initial_state):
    return solve(initial_state, 3)


@aoc_timer(2, 17, 2020)
def solve_second(initial_state):
    return solve(initial_state, 4)


def parse_input(input_str):
    return input_str.splitlines()


if __name__ == '__main__':
    initial_state = parse_input(get_input(17, year=2020))
    solve_first(initial_state)
    solve_second(initial_state)
