from dataclasses import dataclass
from typing import Union, Callable

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    return input_str.splitlines()


@dataclass
class Computer:
    output: Union[int, str]
    code: list
    process: Callable
    x: int = 1
    clock: int = 1

    def cycle(self):
        self.output += self.process(self.clock, self.x)
        self.clock += 1
    
    def run(self):
        for line in program:
            instr, *arg = line.split()
            self.cycle()
            if instr == "addx":
                self.cycle()
                self.x += int(arg.pop())
        return self.output


@aoc_timer(1, 10, 2022)
def solve_first(program):
    return Computer(
        output=0,
        code=program,
        process=lambda c, x: c * x if c % 40 == 20 else 0
    ).run()


@aoc_timer(2, 10, 2022)
def solve_second(program):
    out = Computer(
        output="",
        code=program,
        process=lambda c, x: "@" if abs((c - 1) % 40 - x) <= 1 else " "
    ).run()
    frame = "\n"
    for i in range(0, len(out), 40):
        frame += out[i: i + 40] + "\n"
    return frame


if __name__ == "__main__":
    program = parse_input(get_input(10, year=2022))
    solve_first(program)
    solve_second(program)
