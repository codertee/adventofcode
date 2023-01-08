from itertools import count, cycle, pairwise, starmap
from collections import namedtuple, defaultdict
from operator import lshift, rshift

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


class Rock:
    __slots__ = ['ints', 'len', 'i', 'pos']

    def __init__(self, ints, i):
        self.ints = ints
        self.len = len(self.ints)
        self.i = i
        self.pos = 0b0010000
    
    def shift(self, direction):
        op = {'>': rshift, '<': lshift}[direction]
        r = Rock([op(i, 1) for i in self.ints], self.i)
        r.pos = op(self.pos, 1)
        return r
    
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


def drop(rock, jets, pile, top):
    top -= (2 + rock.len)
    for y in count(top):
        jet = next(jets)
        if rock.shiftable(jet.dir):
            shifted = rock.shift(jet.dir)
            if not shifted.overlaps(pile[y:]):
                rock = shifted
        if rock.overlaps(pile[y + 1:]) or rock.len + y >= len(pile):
            for i in range(rock.len):
                pile[y + i] = pile[y + i] | rock.ints[i]
            while pile[top] == 0:
                top += 1
            return top - 1, rock, jet


@aoc_timer(1, 17, 2022)
def solve_first(jets):
    rocks, jets = cycle(ROCKS), cycle(jets)
    pile = [0] * 10000
    top = len(pile) - 1
    for _ in range(2022):
        top, *_ = drop(next(rocks), jets, pile, top)
    return len(pile) - top - 1


@aoc_timer(2, 17, 2022)
def solve_second(jets):
    rocks, jets = cycle(ROCKS), cycle(jets)
    pile = [0] * 10000
    top = len(pile) - 1
    positions, heights = [], []
    cycles = defaultdict(list)
    for n_rock in count(1):
        top, rock, jet = drop(next(rocks), jets, pile, top)
        height = len(pile) - top - 1
        heights.append(height)
        positions.append(rock.pos)
        if c := cycles.get((jet.i, rock.i)):
            for start, mid in pairwise(c):
                if positions[start: mid] == positions[mid:]:
                    rcycle = n_rock - mid
                    hcycle = height - heights[mid - 1]
                    more, remain = divmod(int(1e12) - mid, rcycle)
                    return more * hcycle + heights[mid - 1 + remain]
        cycles[(jet.i, rock.i)].append(n_rock)


if __name__ == '__main__':
    jets = parse_input(get_input(17, year=2022))
    solve_first(jets)
    solve_second(jets)
