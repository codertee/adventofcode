from itertools import pairwise
from dataclasses import dataclass

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    moves = []
    for line in input_str.splitlines():
        direction, n = line.split()
        moves.append((direction, int(n)))
    return moves


@dataclass
class Segment:
    x = 0
    y = 0

    def move(self, direction):
        match direction:
            case 'U':
                self.y += 1
            case 'R':
                self.x += 1
            case 'D':
                self.y -= 1
            case 'L':
                self.x -= 1
    
    @staticmethod
    def sign(x):
        return (x > 0) - (x < 0)

    def drag(self, other):
        dx, dy = self.x - other.x, self.y - other.y
        if  abs(dx) > 1 or abs(dy) > 1:
            other.x += self.sign(dx)
            other.y += self.sign(dy)


def solve(moves, length):
    seen = set()
    rope = [Segment() for _ in range(length)]
    for direction, n in moves:
        for _ in range(n):
            rope[0].move(direction)
            for one, other in pairwise(rope):
                one.drag(other)
            tail = rope[-1]
            seen.add((tail.x, tail.y))
    return len(seen)


@aoc_timer(1, 9, 2022)
def solve_first(moves):
    return solve(moves, 2)


@aoc_timer(2, 9, 2022)
def solve_second(moves):
    return solve(moves, 10)


if __name__ == '__main__':
    moves = parse_input(get_input(9, year=2022))
    solve_first(moves)
    solve_second(moves)
