from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


@aoc_timer(1, 14, 2020)
def solve_first(code):
    mem = {}
    for instr, val in code:
        if instr == 'mask':
            mask = val
            continue
        value = bitstring(int(val), len(mask))
        value = (v if m == 'X' else m for v, m in zip(value, mask))
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
        addr_template = ''
        for mask_bit, addr_bit in zip(mask, addr):
            if mask_bit == "0":
                addr_template += addr_bit
            elif mask_bit == "1":
                addr_template += "1"
            else:
                addr_template += "{}"
        floating_length = mask.count('X')
        for f in range(2 ** floating_length):
            addr = addr_template.format(*bitstring(f, floating_length))
            addr = int(addr, 2)
            mem[addr] = int(val)
    return sum(mem.values())


def bitstring(x, l):
    return bin(x)[2:].zfill(l)


def parse(line):
    arg, val = line.split(' = ')
    if arg == 'mask':
        return arg, val
    else:
        return int(arg[4:-1]), val


def parse_input(input_str):
    return list(map(parse, input_str.splitlines()))


if __name__ == '__main__':
    code = parse_input(get_input(14, year=2020))
    solve_first(code)
    solve_second(code)