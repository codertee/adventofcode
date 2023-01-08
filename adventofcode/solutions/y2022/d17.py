from itertools import count, cycle, starmap
from collections import namedtuple
from operator import lshift, rshift

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


class Rock:
    __slots__ = ['ints', 'len', 'i', 'pos']

    def __init__(self, ints, i, pos=0b0010000):
        self.ints = ints
        self.len = len(self.ints)
        self.i = i
        self.pos = pos
    
    def shift(self, jet):
        op = {'>': rshift, '<': lshift}[jet]
        return Rock([op(i, 1) for i in self.ints], self.i, op(self.pos, 1))
    
    def overlaps(self, pile):
        for i, layer in zip(self.ints, pile):
            if i & layer:
                return True
        return False

    def shiftable(self, jet):
        edge = {'>': 0b0000001, '<': 0b1000000}[jet]
        for i in self.ints:
            if i & edge:
                return False
        return True


ROCKS = (
    Rock((
        0b0011110,), 0),
    Rock((
        0b0001000,
        0b0011100,
        0b0001000), 1),
    Rock((
        0b0000100,
        0b0000100,
        0b0011100), 2),
    Rock((
        0b0010000,
        0b0010000,
        0b0010000,
        0b0010000), 3),
    Rock((
        0b0011000,
        0b0011000), 4)
)


def parse_input(input_str):
    Jet = namedtuple('Jet', ['i', 'dir'])
    return list(starmap(Jet, enumerate(input_str.strip())))


def solve(jets, total=2022):
    Previous = namedtuple('Previous', ['rock', 'height'])
    rocks, jets = cycle(ROCKS), cycle(jets)
    pile = [0] * 10000
    top = len(pile)
    states = {}

    for n_rock in count():
        rock = next(rocks)
        for y in count(top - rock.len - 3):
            jet = next(jets)
            if rock.shiftable(jet.dir):
                shifted = rock.shift(jet.dir)
                if not shifted.overlaps(pile[y:]):
                    rock = shifted
            if rock.overlaps(pile[y + 1:]) or rock.len + y >= len(pile):
                for i in range(rock.len):
                    pile[y + i] |= rock.ints[i]
                break
        top = min(top, y)
        height = len(pile) - top

        state = (jet.i, rock.i, rock.pos)
        if prev := states.get(state):
            rcycle = n_rock - prev.rock
            hcycle = height - prev.height
            diff = total - n_rock - 1
            more, remain = divmod(diff, rcycle)
            if remain == 0: 
                return hcycle * more + height
        else:
            states[state] = Previous(n_rock, height)


@aoc_timer(1, 17, 2022)
def solve_first(jets):
    return solve(jets)


@aoc_timer(2, 17, 2022)
def solve_second(jets):
    return solve(jets, int(1e12))


if __name__ == '__main__':
    jets = parse_input(get_input(17, year=2022))
    solve_first(jets)
    solve_second(jets)
