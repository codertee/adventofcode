import re

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer

MONKEY_REGEX = re.compile(r"[a-z]{4}: (\d+|[a-z]{4} [-+*/] [a-z]{4})")


def parse_input(input_str):
    monkeys = dict()
    for line in input_str.splitlines():
        if not MONKEY_REGEX.match(line):
            raise Exception("Don't want to eval " + line)
        name, other = line.split(': ')
        monkeys[name] = other.split()
    return monkeys


def expand(monkeys, key):
    match monkeys[key]:
        case [one, op, other]:
            one = expand(monkeys, one)
            other = expand(monkeys, other)
            return "(%s %s %s)" % (one, op, other)
        case [num]:
            return num


@aoc_timer(1, 21, 2022)
def solve_first(monkeys):
    return eval(expand(monkeys, "root"))


@aoc_timer(2, 21, 2022)
def solve_second(monkeys):
    monkeys["root"][1] = "-("
    monkeys["humn"] = ["-1j"]
    complex = eval(expand(monkeys, "root") + ")")
    return round(complex.real / complex.imag)


if __name__ == '__main__':
    monkeys = parse_input(get_input(21, year=2022))
    solve_first(monkeys)
    solve_second(monkeys)
