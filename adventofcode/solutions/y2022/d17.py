from itertools import count, cycle, pairwise, starmap
from collections import namedtuple, defaultdict
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


def drop(rock, jets, pile, top):
    for y in count(top - rock.len - 3):
        jet = next(jets)
        if rock.shiftable(jet.dir):
            shifted = rock.shift(jet.dir)
            if not shifted.overlaps(pile[y:]):
                rock = shifted
        if rock.overlaps(pile[y + 1:]) or rock.len + y >= len(pile):
            for i in range(rock.len):
                pile[y + i] |= rock.ints[i]
            return min(top, y), rock, jet


@aoc_timer(1, 17, 2022)
def solve_first(jets):
    rocks, jets = cycle(ROCKS), cycle(jets)
    pile = [0] * 10000
    top = len(pile)
    for _ in range(2022):
        top, *_ = drop(next(rocks), jets, pile, top)
    return len(pile) - top


@aoc_timer(2, 17, 2022)
def solve_second(jets):
    rocks, jets = cycle(ROCKS), cycle(jets)
    pile = [0] * 10000
    top = len(pile)
    heights, positions = [], []
    cycles = defaultdict(list)
    for n_rock in count():
        top, rock, jet = drop(next(rocks), jets, pile, top)
        height = len(pile) - top
        reps = cycles[(jet.i, rock.i)]
        for start, mid in pairwise(reps):
            if positions[start: mid] == positions[mid:]:
                rcycle = n_rock - mid
                hcycle = height - heights[mid]
                diff = int(1e12) - mid - 1
                more, remain = divmod(diff, rcycle)
                return more * hcycle + heights[mid + remain]
        reps.append(n_rock)
        heights.append(height)
        positions.append(rock.pos)


if __name__ == '__main__':
    jets = parse_input(get_input(17, year=2022))
    solve_first(jets)
    solve_second(jets)
