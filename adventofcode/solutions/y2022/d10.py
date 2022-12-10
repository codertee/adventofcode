from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    return input_str.splitlines()


def run(out, program, process):
    regx, clock = 1, 1

    def cycle():
        nonlocal out, clock
        out += process(clock, regx)
        clock += 1

    for line in program:
        cycle()
        instr, *arg = line.split()
        if instr == "addx":
            cycle()
            regx += int(arg.pop())
    return out


@aoc_timer(1, 10, 2022)
def solve_first(program):
    return run(0, program, lambda c, x: c * x if c % 40 == 20 else 0)


def process_pixel(c, x):
    return "@" if abs((c - 1) % 40 - x) <= 1 else " "


@aoc_timer(2, 10, 2022)
def solve_second(program):
    out = run("", program, process_pixel)
    frame = "\n"
    for i in range(0, len(out), 40):
        frame += out[i: i + 40] + "\n"
    return frame


if __name__ == "__main__":
    program = parse_input(get_input(10, year=2022))
    solve_first(program)
    solve_second(program)
