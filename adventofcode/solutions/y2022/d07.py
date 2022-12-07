from collections import Counter

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    dirs, cwd = Counter(), []
    for line in input_str.splitlines():
        match line.split():
            case ('$', 'cd', '..'):
                cwd.pop()
            case ('$', 'cd', name):
                cwd.append(name)
            case ('$', 'ls') | ('dir', _):
                continue
            case (size, _):
                size = int(size)
                for i in range(len(cwd)):
                    hashable = tuple(cwd[:i + 1])
                    dirs[hashable] += size
    return dirs


@aoc_timer(1, 7, 2022)
def solve_first(dirs):
    return sum(filter(lambda s: s <= 100000, dirs.values()))


@aoc_timer(2, 7, 2022)
def solve_second(dirs):
    used = dirs[('/',)]
    enough = 30000000 - (70000000 - used)
    return min(filter(lambda s: s >= enough, dirs.values()))


if __name__ == '__main__':
    dirs = parse_input(get_input(7, year=2022))
    solve_first(dirs)
    solve_second(dirs)
