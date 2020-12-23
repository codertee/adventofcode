from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


class Cup:
    __slots__ = ['v', 'n']

    def __init__(self, val, next_cup=None):
        self.v = val
        self.n = next_cup


def play(cups: list, turns=100):
    max_val = max(cups)
    cup = Cup(cups[-1])
    cups_map = {}
    for val in cups[::-1]:
        cup = cups_map[val] = Cup(val, cup)
    current = cups_map[cups[-1]].n = cup
    for _ in range(turns):
        one, two, three = current.n, current.n.n, current.n.n.n
        selected_val = current.v - 1
        unselectable = {one.v, two.v, three.v, 0}
        while selected_val in unselectable:
            selected_val -= 1
            if selected_val < 1:
                selected_val = max_val
        selected = cups_map[selected_val]
        current.n = three.n
        three.n = selected.n
        selected.n = one
        current = current.n
    return cups_map[1]


@aoc_timer(1, 23, 2020)
def solve_first(cups):
    cup = play(cups)
    res = ''
    for _ in range(len(cups) - 1):
        cup = cup.n
        res += str(cup.v)
    return res
        

@aoc_timer(2, 23, 2020)
def solve_second(cups):
    low, high = max(cups) + 1, 1000001
    cups += list(range(low, high))
    cup = play(cups, 10000000)
    return cup.n.v * cup.n.n.v


def parse_input(input_str):
    return list(map(int, input_str.strip()))


if __name__ == '__main__':
    cups = parse_input(get_input(23, year=2020))
    solve_first(cups)
    solve_second(cups)
