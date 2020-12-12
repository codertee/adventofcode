from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def run(code):
    ptr = 0
    accumulator = 0
    seen = set()
    while True:
        if ptr == len(code):
            return 0, accumulator
        if ptr in seen:
            return 1, accumulator
        seen.add(ptr)
        instr, arg = code[ptr]
        if instr == 'acc':
            accumulator += arg
            ptr += 1
        elif instr == 'jmp':
            ptr += arg
        elif instr == 'nop':
            ptr +=1


def parse(code_line):
    instr, arg = code_line.split()
    return instr, int(arg)


def parse_input(input_str):
    return list(map(parse, input_str.splitlines()))


@aoc_timer(1, 8, 2020)
def solve_first(code):
    return run(code)[1]


@aoc_timer(2, 8, 2020)
def solve_second(code):
    for ptr, (instr, arg) in enumerate(code):
        if instr in {'jmp', 'nop'}:
            if instr == 'jmp':
                code[ptr] = 'nop', arg
            elif instr == 'nop':
                code[ptr] = 'jmp', arg
            retcode, retval = run(code)
            if retcode == 0:
                return retval
            else:
                code[ptr] = instr, arg


if __name__ == '__main__':
    code = parse_input(get_input(8, year=2020))
    solve_first(code.copy())
    solve_second(code)
