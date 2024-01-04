import math
import re
from itertools import cycle, count

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


def parse_input(input_str):
    turns, net_str = input_str.split("\n\n")
    turns = list(map(int, turns.replace("R", "1").replace("L", "0")))
    net = {}
    for l in net_str.splitlines():
        node, *pair = re.findall(r"\w+", l)
        net[node] = pair
    return turns, net


@aoc_timer(1, 8, 2023)
def solve_first(turns: list, net: dict):
    turns, cur = cycle(turns), "AAA"
    for c in count(1):
        cur = net[cur][next(turns)]
        if cur == "ZZZ":
            return c


@aoc_timer(2, 8, 2023)
def solve_second(turns: list, net: dict[str, list]):
    turns, counts = cycle(turns), []
    state = [key for key in net if key.endswith("A")]
    for c in count(1):
        turn = next(turns)
        state = [net[node][turn] for node in state]
        for node in list(state):
            if node.endswith("Z"):
                counts.append(c)
                state.remove(node)
        if not state:
            return math.lcm(*counts)


if __name__ == "__main__":
    turns, net = parse_input(get_input(8, year=2023))
    solve_first(turns, net)
    solve_second(turns, net)
