from itertools import product

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse(line):
    match line.split(' = '):
        case 'mask', val:
            return 'mask', val
        case arg, val:
            return int(arg[4:-1]), int(val)


def parse_input(input_str):
    return list(map(parse, input_str.splitlines()))


def bitstring(x, l):
    return bin(x)[2:].zfill(l)


@aoc_timer(1, 14, 2020)
def solve_first(code):
    mem = {}
    for instr, val in code:
        if instr == 'mask':
            mask = val
            continue
        value = bitstring(val, len(mask))
        value = (m == 'X' and v or m for v, m in zip(value, mask))
        value = int(''.join(value), 2)
        mem[instr] = value
    return sum(mem.values())


@aoc_timer(2, 14, 2020)
def solve_second(code):
    mem = {}
    for instr, val in code:
        if instr == 'mask':
            mask = val
            continue
        addr = bitstring(instr, len(mask))
        template = ''
        for mask_bit, addr_bit in zip(mask, addr):
            charmap = {'0': addr_bit, '1': '1', 'X': '%s'}
            template += charmap[mask_bit]
        for fill in product('01', repeat=mask.count('X')):
            addr = int(template % fill, 2)
            mem[addr] = val
    return sum(mem.values())


if __name__ == '__main__':
    code = parse_input(get_input(14, year=2020))
    solve_first(code)
    solve_second(code)