import re
from collections import defaultdict
from itertools import permutations, product, combinations

from adventofcode.inputs import get_input
from adventofcode.utils import aoc_timer


REGEX = re.compile(
    r"Valve (\w+) has flow rate=(\d+); "
    r"tunnels? leads? to valves? ([\w, ]+)\b")


def parse_input(input_str):
    valves, flows = {}, []
    for m in REGEX.finditer(input_str):
        label, flow, linked = m.groups()
        valves[label] = set(linked.split(", "))
        if flow != "0":
            flows.append((label, int(flow)))
    dists = {}
    for src, dst in product(valves, repeat=2):
        dists[(src, dst)] = 1 if dst in valves[src] else 99999
    for k, i, j in permutations(valves, 3):
        dists[i, j] = min(dists[i, j], dists[i, k] + dists[k, j])
    return flows, dists


def solve(flows: list[tuple[str, int]], distances: dict[tuple, int], total: int):
    queue = [("AA", total, frozenset(), 0)]
    results = defaultdict(int)
    while queue:
        valve, minutes, visited, pressure = queue.pop()
        results[visited] = max(results[visited], pressure)
        for dst, flow in flows:
            remaining = minutes - distances[valve, dst] - 1
            if remaining <= 0 or dst in visited:
                continue
            queue.append((dst, remaining, visited | {dst}, pressure + flow * remaining))
    return results


@aoc_timer(1, 16, 2022)
def solve_first(flows, dists):
    return max(solve(flows, dists, 30).values())


@aoc_timer(2, 16, 2022)
def solve_second(flows, dists):
    combs = combinations(solve(flows, dists, 26).items(), 2) 
    return max(p1 + p2 for (w1, p1), (w2, p2) in combs if not w1 & w2)


if __name__ == "__main__":
    flows, dists = parse_input(get_input(16, year=2022))
    solve_first(flows, dists)
    solve_second(flows, dists)
