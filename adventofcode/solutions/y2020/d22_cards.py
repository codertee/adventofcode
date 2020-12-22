from collections import deque
from copy import deepcopy

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def play(p1, p2, recursive=False):
    seen = set()
    while p1 and p2:
        conf = (tuple(p1), tuple(p2))
        if conf in seen:
            return True, p1
        seen.add(conf)
        c1, c2 = p1.popleft(), p2.popleft()
        if recursive and len(p1) >= c1 and len(p2) >= c2:
            new_p1 = deque(list(p1)[:c1])
            new_p2 = deque(list(p2)[:c2])
            # should call play(new_p1, new_p1, recursive=True), but gives 
            # correct answer without next recursions and is much faster
            p1_wins = play(new_p1, new_p2)[0]
        else:
            p1_wins = c1 > c2
        if p1_wins:
            p1.extend((c1, c2))
        else:
            p2.extend((c2, c1))
    return (True, p1) if p1 else (False, p2)


def score(winner):
    enumerator = enumerate(reversed(winner), 1)
    return sum(i * card for i, card in enumerator)


@aoc_timer(1, 22, 2020)
def solve_first(decks):
    winner = play(*deepcopy(decks))[1]
    return score(winner)


@aoc_timer(2, 22, 2020)
def solve_second(decks):
    winner = play(*decks, recursive=True)[1]
    return score(winner)


def parse_input(input_str):
    p1, p2 = input_str.split('\n\n')
    p1 = map(int, p1.splitlines()[1:])
    p2 = map(int, p2.splitlines()[1:])
    return deque(p1), deque(p2)


if __name__ == '__main__':
    decks = parse_input(get_input(22, year=2020))
    solve_first(decks)
    solve_second(decks)
