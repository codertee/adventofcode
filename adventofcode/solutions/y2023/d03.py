import re
from collections import namedtuple
from math import prod

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


Symbol = namedtuple('Symbol', ['val', 'adj'])


class Number:

    def __init__(self, row, c_start, c_end, val):
        self.value = int(val)
        adj = {(row, c_start -1), (row, c_end)}
        for c in range(c_start - 1, c_end + 1):
            adj.add((row + 1, c))
            adj.add((row - 1, c))
        self.box = adj


def parse_input(input_str):
    numbers, symbols = [], {}
    regex = re.compile(r"(?P<number>\d+)|(?P<symbol>[^\d.])")
    for row, line in enumerate(input_str.splitlines()):
        for m in regex.finditer(line):
            number, symbol = m.groups()
            col = m.start()
            if number:
                numbers.append(Number(row, col, m.end(), number))
            elif symbol:
                symbols[row, col] = Symbol(symbol, [])
    return numbers, symbols


@aoc_timer(1, 3, 2023)
def solve_first(numbers: list[Number], symbols: dict[str, Symbol]):
    return sum(n.value for n in numbers if symbols.keys() & n.box)


@aoc_timer(2, 3, 2023)
def solve_second(numbers: list[Number], symbols: dict[str, Symbol]):
    symbols = {c: s for c, s in symbols.items() if s.val == "*"}
    for n in numbers:
        for coords in n.box:
            if s := symbols.get(coords):
                s.adj.append(n.value)
    return sum(prod(s.adj) for s in symbols.values() if len(s.adj) == 2)


if __name__ == "__main__":
    args = parse_input(get_input(3, year=2023))
    solve_first(*args)
    solve_second(*args)
