from collections import Counter

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    dirs = Counter()
    cwd = []
    command = ''
    for line in input_str.splitlines():
        if line.startswith('dir'):
            continue
        if line.startswith('$'):
            _, command, *args = line.split()
            if command == 'cd':
                arg = args.pop()
                if arg == '..':
                    cwd.pop()
                else:
                    cwd.append(arg)
        elif command == 'ls':
            size = int(line.split()[0])
            for i in range(len(cwd)):
                dirs[tuple(cwd[:i + 1])] += size
    return dirs


@aoc_timer(1, 7, 2022)
def solve_first(dirs):
    sizes = dirs.values()
    return sum(filter(lambda s: s <= 100000, sizes))


@aoc_timer(2, 7, 2022)
def solve_second(dirs):
    used = dirs[("/",)]
    free = 70000000 - used
    enough = 30000000 - free
    for size in sorted(dirs.values()):
        if size >= enough:
            return size


if __name__ == '__main__':
    dirs = parse_input(get_input(7, year=2022))
    solve_first(dirs)
    solve_second(dirs)
