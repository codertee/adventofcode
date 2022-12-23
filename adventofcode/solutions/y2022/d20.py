from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


class Node(object):
    __slots__ = ['num']

    def __init__(self, line):
        self.num = int(line)


def parse_input(input_str):
    return list(map(Node, input_str.splitlines()))


def solve(nodes, iterations=1):
    length = len(nodes)
    seq = nodes.copy()
    for _ in range(iterations):
        for n in nodes:
            i = seq.index(n)
            new_idx = (i + n.num) % (length - 1)
            seq.insert(new_idx, seq.pop(i))
    zero = next(i for i, n in enumerate(seq) if n.num == 0)
    answer = 0
    for offset in 1000, 2000, 3000:
        i = (zero + offset) % length
        answer += seq[i].num
    return answer


@aoc_timer(1, 20, 2022)
def solve_first(nodes):
    return solve(nodes)


@aoc_timer(2, 20, 2022)
def solve_second(nodes):
    for n in nodes:
        n.num *= 811589153
    return solve(nodes, 10)


if __name__ == '__main__':
    nodes = parse_input(get_input(20, year=2022))
    solve_first(nodes)
    solve_second(nodes)
