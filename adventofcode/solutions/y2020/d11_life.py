from copy import deepcopy

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    return tuple(map(list, input_str.splitlines()))


DELTAS = (-1, -1), (0, -1), (1, -1), (-1, 0), (1, -0), (-1, 1), (0, 1), (1, 1)
TAKEN, FREE = '#L'


def count_adjacent(r, c, seat_map):
    count = 0
    for dr, dc in DELTAS:
        if seat_at(r + dr, c + dc, seat_map) == TAKEN:
            count += 1
    return count


def count_seen(r, c, seat_map):
    count = 0
    for dr, dc in DELTAS:
        row = r + dr
        col = c + dc
        while True:
            seat = seat_at(row, col, seat_map)
            if seat in {None, FREE}:
                break
            if seat == TAKEN:
                count += 1
                break
            row += dr
            col += dc
    return count


def seat_at(row, col, seat_map):
    if row < 0 or col < 0:
        return
    try:
        return seat_map[row][col]
    except IndexError:
        return


def crowding_pass(seat_map, count_func, max_occupied):
    changed = False
    new_map = deepcopy(seat_map)
    for i, row in enumerate(seat_map):
        for j, seat in enumerate(row):
            occupied = count_func(i, j, seat_map)
            if seat == FREE and occupied == 0:
                new_map[i][j] = TAKEN
                changed = True
            elif seat == TAKEN and occupied >= max_occupied:
                new_map[i][j] = FREE
                changed = True
    return new_map, changed


def solve(seat_map, count_f, n):
    changed = True
    while changed:
        seat_map, changed = crowding_pass(seat_map, count_f, n)
    return sum(row.count(TAKEN) for row in seat_map)


@aoc_timer(1, 11, 2020)
def solve_first(seat_map):
    return solve(seat_map, count_adjacent, 4)


@aoc_timer(2, 11, 2020)
def solve_second(seat_map):
    return solve(seat_map, count_seen, 5)


if __name__ == '__main__':
    seat_map = parse_input(get_input(11, year=2020))
    solve_first(seat_map)
    solve_second(seat_map)
