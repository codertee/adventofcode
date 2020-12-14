from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    return list(map(int, input_str.splitlines()))


def fuel(mass):
    return mass // 3 - 2


def rocket_fuel(to_lift):
    total = delta = fuel(to_lift)
    while delta := fuel(delta) > 0:
        total += delta
    return total


@aoc_timer(1, 1, 2019)
def solve_first(masses):
    return sum(map(fuel, masses))


@aoc_timer(2, 1, 2019)
def solve_second(masses):
    return sum(map(rocket_fuel, masses))


if __name__ == '__main__':
    masses = parse_input(get_input(1, year=2019))
    solve_first(masses)
    solve_second(masses)

