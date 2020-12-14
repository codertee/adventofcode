from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    # allows to skip 0 with filter(bool, iter)
    input_str = input_str.replace('x', '0')
    earliest, bus_lst = input_str.splitlines()
    bus_lst = list(map(int, bus_lst.split(',')))
    return int(earliest), bus_lst


@aoc_timer(1, 13, 2020)
def solve_first(args):
    earliest, bus_lst = args
    bus_iter = filter(bool, bus_lst)
    wait_for = lambda bus: bus - earliest % bus
    earliest_bus = min(bus_iter, key=wait_for)
    return wait_for(earliest_bus) * earliest_bus


@aoc_timer(2, 13, 2020)
def solve_second(args):
    _, bus_lst = args
    bus_iter = filter(lambda b: b[1], enumerate(bus_lst))
    start, step = next(bus_iter)
    for depart, bus in bus_iter:
        while (start + depart) % bus != 0:
            start += step
        step *= bus
    return start


if __name__ == '__main__':
    args = parse_input(get_input(13, year=2020))
    solve_first(args)
    solve_second(args)
