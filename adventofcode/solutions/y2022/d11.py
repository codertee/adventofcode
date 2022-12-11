import re
from collections import deque
from copy import deepcopy
from functools import partial
from math import lcm
from operator import add, mul

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


REGULAR_MONKEY = re.compile(r"""
  Starting items: (?P<items>[\d, ]+)
  Operation: new = old (?P<op>[*+]) (?P<arg>\d+|old)
  Test: divisible by (?P<test>\d+)
    If true: throw to monkey (?P<true>\d+)
    If false: throw to monkey (?P<false>\d+)""")


class Monkey:
    """field names correspond to regex group names"""
    __slots__ = ('items', 'op', 'test', 'true', 'false', 'inspections')

    def __init__(self, **kw):
        items = kw['items'].split(', ')
        self.items = deque(map(int, items))
        self.test = int(kw['test'])
        self.true = int(kw['true'])
        self.false = int(kw['false'])
        self.inspections = 0
        arg = kw['arg']
        if arg == 'old':
            self.op = lambda x: x * x
        else:
            op = {'*': mul, '+': add}[kw['op']]
            self.op = partial(op, int(arg))


def parse_input(input_str):
    return [
        Monkey(**match.groupdict())
        for match in REGULAR_MONKEY.finditer(input_str)
    ]


def solve(monkeys, N, partfunc):

    for _ in range(N):
        for m in monkeys:
            while m.items:
                item = m.items.popleft()
                item = partfunc(m.op(item))
                other = m.true if item % m.test == 0 else m.false
                monkeys[other].items.append(item)
                m.inspections += 1

    one, other = sorted(m.inspections for m in monkeys)[-2:]
    return one * other


@aoc_timer(1, 11, 2022)
def solve_first(monkeys):
    monkeys = deepcopy(monkeys)
    return solve(monkeys, 20, lambda x: x // 3)


@aoc_timer(2, 11, 2022)
def solve_second(monkeys):
    multiple = lcm(*(m.test for m in monkeys))
    return solve(monkeys, 10000, lambda x: x % multiple)


if __name__ == '__main__':
    monkeys = parse_input(get_input(11, year=2022))
    solve_first(monkeys)
    solve_second(monkeys)
